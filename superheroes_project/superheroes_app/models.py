from django.db import models


# Create your models here.
class SuperHeroes(models.Model):
    """
    The constructor that builds what a Superhero object is. Will be used in conjunction with the most
    up-to-date database in MySQL server for this app.
    """
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=100)

    def __str__(self):
        """A string that will contain the current superheroes following characteristics: name,
        alter ego, primary and secondary abilities, as well as their catchphrase.
        :returns: self.name, self.alter_ego, self.primary_ability, self. secondary_ability, self.catchphrase
        in a concatenated string."""
        return f"{self.name} {self.alter_ego} {self.primary_ability} " \
               f"{self.secondary_ability} {self.catchphrase}"
