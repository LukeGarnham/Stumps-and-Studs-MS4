from django.db import models


class Contact(models.Model):

    def __str__(self):
        return self.full_name

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
