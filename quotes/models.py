from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    author_discription = models.CharField(max_length=150)
    author_url = models.CharField(max_length=150)
    author_image = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    list_display = ('name', 'author_discription', 'author_url')


class Categories(models.Model):
    name = models.CharField(max_length=30)
    cat_id = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    list_display = ('cat_id', 'name')


class Quote(models.Model):
     author = models.ForeignKey(Author)
     category = models.ForeignKey(Categories)
     quote_id = models.IntegerField(default=0)
     quote_discription = models.CharField(max_length=1000)

     def __str__(self):              # __unicode__ on Python 2
        return self.quote_discription

     list_display = ('author', 'category','quote_id','quote_discription')
