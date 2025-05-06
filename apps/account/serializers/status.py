from rest_framework import serializers

class VerificationStatusSerializer(serializers.Serializer):
    completed = serializers.BooleanField()

class VerificationStatusSerializer(serializers.Serializer):
    has_about = VerificationStatusSerializer()
    has_avatar = VerificationStatusSerializer()
    valid_name = VerificationStatusSerializer()
    valid_email = VerificationStatusSerializer()
    valid_phone = VerificationStatusSerializer()
    
    @classmethod
    def get_verification_status_for_user(cls, user):
        """
        Creates and validates verification status data for a given user.
        """
        profile = user.profile
        
        verification_data = {
            "has_about": {
                "completed": profile.has_about
            },
            "has_avatar": {
                "completed": profile.has_avatar
            },
            "valid_name": {
                "completed": profile.valid_name
            },
            "valid_email": {
                "completed": user.verification.email_verified
            },
            "valid_phone": {
                "completed": user.verification.phone_verified
            },
        }
        
        serializer = cls(data=verification_data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data