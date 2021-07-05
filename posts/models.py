from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_subtitle = models.CharField(max_length=100)
    post_body = models.TextField()
    post_author = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

class Conversa(models.Model):
    post_body = models.TextField()
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_body





