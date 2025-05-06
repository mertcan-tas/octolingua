from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

from verification.tasks import send_verification_email_task
from verification.utils import verify_token

from verification.models import AccountVerification
from account.models import User

class SendVerificationEmailView(APIView):
    permission_classes = [IsAuthenticated]
    
    @method_decorator(ratelimit(key='user', rate='5/h', method='POST'))
    def post(self, request):
        user = request.user

        if user.verification.email_verified:
            return Response(
                {"detail": "Email already verified"}, 
                status=status.HTTP_409_CONFLICT
            )
        
        send_verification_email_task.delay(
            user_full_name=user.profile.full_name,
            user_id=user.id,
            user_email=user.email
        )
        
        return Response(
            {"success": True},
            status=status.HTTP_202_ACCEPTED
        )
        

class VerifyEmailAPIView(APIView):
    permission_classes = [AllowAny]
    
    @method_decorator(ratelimit(key='ip', rate='5/h', method='GET'))
    def get(self, request, token: str):
        try:
            user_id = verify_token(token)
            if user_id is None:
                return Response(
                    {'detail': 'Invalid or expired token'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            user = User.objects.select_related('verification').get(id=user_id)
            
            if user.verification.email_verified:
                return Response(
                    {"detail": "Email already verified"}, 
                    status=status.HTTP_409_CONFLICT
                )
            
            user.verification.verify_email()
            return Response({"detail": "Email successfully verified"})
            
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except AccountVerification.DoesNotExist:
            return Response(
                {"detail": "Verification record not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"detail": "Verification failed"}, #{str(e)} 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )