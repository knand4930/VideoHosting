import uuid
from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='videos/')
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/videos/{self.id}/'

    def get_download_url(self):
        return f'/videos/{self.id}/download/'

    def get_embed_url(self):
        return f'/videos/{self.id}/embed/'
