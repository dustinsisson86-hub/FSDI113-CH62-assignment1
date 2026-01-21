from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    class Meta:
        verbose_name = "Statuses"
        verbose_name_plural = "Statuses"
    name = models.CharField(max_length=128, unique=True, help_text="Enter the status name (e.g., Published, Draft, Archived).")
    description = models.CharField(max_length=256, help_text="Write a brief description of the status.")

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING,
    )

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

