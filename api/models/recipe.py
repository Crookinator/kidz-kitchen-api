from django.db import models
from django.contrib.auth import get_user_model

class Recipe(models.Model):
  # define fields
  title = models.CharField(max_length=100)
  cuisine = models.CharField()
  description = models.CharField(max_length=500)
  ingredients = models.CharField(max_length=500)
  instructions = models.CharField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The recipe titled '{self.title}'."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'title': self.title,
       'cuisine': self.cuisine,
        'description': self.description,
        'instructions': self.instructions,
        'ingredients': self.ingredients
    }
