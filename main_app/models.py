from django.db import models

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