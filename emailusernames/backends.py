from wa_user.models import WAUser
from django.contrib.auth.backends import ModelBackend
import traceback, sys

class EmailAuthBackend(ModelBackend):
    """Allow users to log in with their email address"""
    def get_user(self, email):
        for user in WAUser.objects.filter(email=email): return user
        return None

    def authenticate(self, email=None, password=None, **kwargs):
        # Some authenticators expect to authenticate by 'username'
        if email is None:
            email = kwargs.get('username')

        try:
            user = self.get_user(email)
            if user.check_password(password):
                user.backend = "%s.%s" % (self.__module__, self.__class__.__name__)
                return user
        except:
            traceback.print_exc(file=sys.stdout)
            pass
        return None
