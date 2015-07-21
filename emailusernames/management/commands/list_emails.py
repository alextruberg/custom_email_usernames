from django.core.management.commands import loaddata
from wa_user.models import WAUser

class Command(loaddata.Command):
    def handle(self, *args, **kwargs):
        all_emails = []
        for user in WAUser.objects.all():
            if user.email.lower() in all_emails:
                print "duplicate: " + user.email
            all_emails.append(user.email.lower())
        print len(all_emails)
