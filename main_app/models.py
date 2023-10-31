from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Lesson(models.Model):
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=200, default="Lesson X")
    description = models.TextField(default="Enter description")
    vimeo_id = models.CharField(max_length=30, default="000000000")
    secondary_vimeo_id = models.CharField(max_length=30, default="999999999999")
    length = models.IntegerField(default=5)  # rounded minutes
    thumbnail_id = models.IntegerField(default=100)
    has_file = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number}. {self.title}"

    class Meta:
        ordering = ["number"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)