from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from decouple import config
from verification.utils import generate_token

FRONTEND_URL = config("FRONTEND_URL", default="http://127.0.0.1:8000", cast=str)
EMAIL_VERIFICATION_TOKEN_TTL = config("EMAIL_VERIFICATION_TOKEN_TTL", default=900, cast=int)

@shared_task
def send_verification_email_task(user_id: int, user_full_name: str, user_email: str):
    token = generate_token(user_id)
    verification_link = f"{FRONTEND_URL}/verify-email/{token}/"

    print(user_full_name),

    subject = 'Email Verification'
    context = {'user_full_name': user_full_name, 'verification_link': verification_link}
    
    text_content = ('Email Verification'
               f'Doğrulama kodunuz: \nLink: {verification_link}')

    html_content = render_to_string('email_verify.html', context)
    
    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[user_email]
    )
    msg.attach_alternative(html_content, "text/html")
    return msg.send()