from django.core.mail import send_mail
import random
from django.conf import settings
from apps.users.models import User


def send_opt_via_email(email):
    subject = "Your account verification email"
    opt = random.randint(1000, 9999)
    message = f"Your code is {opt}"
    from_email = settings.EMAIL_HOST
    to_email = [email]

    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email)

    user_obj = User.objects.get(email=email)
    user_obj.opt = opt
    user_obj.save()

