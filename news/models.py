from django.db import models
from django.contrib.auth.models import User

class News(models.Model) :
    title=models.CharField(max_length=225)
    image=models.ImageField(upload_to='image/')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    content=models.TextField()
    author=models.CharField(max_length=100)
    category=models.ManyToManyField("Category")
    tags = models.ManyToManyField("Tag")
    views_count = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = "News"
        ordering = ["-created_time"]
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    Active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-created_time']



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)  # Assuming you have a Post model

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"
    


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


