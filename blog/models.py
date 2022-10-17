from django.db import models
# from django.utils.text import slugify 
from django.contrib.auth.models import User

# my photo
class BookPhoto(models.Model):
     title = models.CharField(max_length=255,blank=True,null=True)
     description = models.TextField(blank=True,null=True)
     img  = models.ImageField(upload_to='book_photos/',blank=True,null=True)


# book photo 
class MyPhoto(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    how_iam = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField()
    Signature = models.CharField(max_length=255,blank=True,null=True)
    img  = models.ImageField(upload_to='my_photos/',blank=True,null=True)  
    date        = models.DateTimeField(auto_now_add=True)   


class Pictures(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
   
    # title       = models.CharField(max_length=200,blank=True,null=True)
    # slug        = models.SlugField(unique=True,blank=True,null=True)
    img         = models.ImageField(upload_to='images/',blank=True,null=True)
    status      = models.CharField(max_length=10, choices=options, default='published')
    date        = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-date',)
    def __str__(self):
        return f'the : {self.img}'

    # def save(self,*args,**kwargs):
    #     self.slug  = slugify(self.title)
    #     super(Pictures,self).save(*args,**kwargs)

   
class NameOfWeb(models.Model):
    name = models.CharField(max_length=255)
    bold_title = models.CharField(max_length=255)
    description = models.TextField()
    small_note = models.CharField(max_length=255)