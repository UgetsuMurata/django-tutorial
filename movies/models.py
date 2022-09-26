from django.db import models

class Movie(models.Model):
    """
    each variable is a column in database table named Movie
    """
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        """Change object name in database"""
        return f'{self.title} from {self.year}'