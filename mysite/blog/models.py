from django.db import models

class post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    cover_image = models.ImageField(upload_to='post_covers/', blank=True, null=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

def __str__(self):
    return self.title
