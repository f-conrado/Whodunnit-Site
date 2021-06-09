from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_body = models.TextField()
    def __str__(self):
        return self.post_title


