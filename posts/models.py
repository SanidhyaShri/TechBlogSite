from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()

    # Linking Post to User via author.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Adding date and time of the post when they published.
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# For adding Like feature on posts.

from django.contrib.auth.models import User

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"


#  For adding Comment feature.

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.title}"
