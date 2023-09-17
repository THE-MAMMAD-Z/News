from django.db import models

class News(models.Model) :
    title=models.CharField(max_length=225)
    image=models.ImageField(upload_to='image/')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    content=models.TextField()
    author=models.CharField(max_length=100)
    category=models.ForeignKey("Category", on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    