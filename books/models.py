from django.db import models


# Custom model manager
class CustomManager(models.Manager):
    def get_books_in_genre(self, genre):
        return self.filter(genre=genre)
    
    
class Books(models.Model):
    title =  models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    published_year = models.IntegerField()
    
    # Associate the custom manager with the model
    new_objects = CustomManager()
    
    def __str__(self):
        return self.title
    