from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Messages'

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
