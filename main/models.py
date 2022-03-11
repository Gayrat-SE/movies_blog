from datetime import date
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        
        
class Actor(models.Model):
    name = models.CharField("name", max_length=100)
    age = models.PositiveSmallIntegerField("age", default=0)
    description = models.TextField("description")
    image = models.ImageField("image", upload_to="actors/")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "actor and director"
        verbose_name_plural = "actors and directors"
        
class Genre(models.Model):
    name = models.CharField("name",max_length=70)
    description = models.TextField("description")
    url = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        
class Movie(models.Model):
    title = models.CharField("title", max_length=100 )
    tagline = models.CharField("tagline", max_length=100)
    description = models.TextField("description")
    poster = models.ImageField("poster", upload_to = "movies/")
    year = models.PositiveSmallIntegerField("year of premiered", default=2019)
    country = models.CharField("country", max_length=70)
    directors = models.ManyToManyField(Actor, verbose_name="directors", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actorss", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    world_premier = models.DateField("premierd_date", default=date.today)
    budget = models.PositiveIntegerField("budget", default=0, help_text="In dollars")
    fees_in_usa = models.PositiveIntegerField("fees in usa", default=0, help_text="in dollars")
    fees_over_world = models.PositiveIntegerField("fees all over the world", default=0, help_text="in dollars")
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.Set_Null, null=True)
    url = models.