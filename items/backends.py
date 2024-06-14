
from .models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email_address=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None