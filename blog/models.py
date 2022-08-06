from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    E_mail=models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Tag(models.Model):
    caption=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.caption}"
class Post(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=200)
    image=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(null=False,db_index=True,unique=True)
    content=models.TextField(validators=[MinLengthValidator(3)])
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tags=models.ManyToManyField(Tag)
    def get_absolute_url(self):
       # return reverse("Bdetail", args=[self.id])
       return reverse("Bdetail", args=[self.slug])
    def __str__(self):
        return f"{self.title} ({self.author})"
        
    
