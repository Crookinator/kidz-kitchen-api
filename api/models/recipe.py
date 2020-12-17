from django.db import models
from django.contrib.auth import get_user_model

class Recipe(models.Model):
  # define fields
  title = models.CharField(max_length=100)
  cuisine = models.CharField()
  favorite = models.BooleanField()
  description = models.CharField(max_length=200)
  ingredients = models.CharField(max_length=200)
  instructions = models.CharField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The recipe titled '{self.title}' is {self.color} in color. It is {self.ripe} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'title': self.title,
       'cuisine': self.cuisine
        'favorite': self.favorite,
        'description': self.description,
        'instructions': self.instructions,
        ingredients': self.ingredients'
    }
