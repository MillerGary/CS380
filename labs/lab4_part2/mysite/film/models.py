from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    #hold the main of the main actor, max length 250 chars
    main_actor = models.CharField(max_length = 250)

    #holds the name of the film's title, max length 250 chars
    film_title = models.CharField(max_length = 250)

    #holds the name of the film's director, max length 250 chars
    director_name = models.CharField(max_length = 250)

    #holds the film's genre type, max length 250 chars
    genre = models.CharField(max_length = 250)

    # The following is a method of Album class
    def __str__(self):
        # show the film_title, main_actor, director_name
        return self.film_title+ ' - ' +self.main_actor+ ' - ' +self.director_name
    # end of __str__()

    # end of class Album()
