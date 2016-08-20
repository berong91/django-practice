from __future__ import unicode_literals

from django.db import models


class Rating(models.Model):
    # Define rating types and value
    CLEAN = "clean"
    LOW = "low-risk"
    MEDIUM = "medium-risk"
    HIGH = "high-risk"
    MALICIOUS = "malicious"
    EVENT_TYPES = (
        (CLEAN, "Alert"),
        (LOW, "Low Risk"),
        (MEDIUM, "Medium Risk"),
        (HIGH, "High Risk"),
        (MALICIOUS, "Malicious"),
    )
    
    # map ratings to colours
    COLOUR = {
        CLEAN:      "66ff33",
        LOW:        "FF6A00",
        MEDIUM:     "FF0000",
        HIGH:       "FFE800",
        MALICIOUS:  "999966",
    }
    
    ratingType = models.CharField(max_length=16, choices=EVENT_TYPES, default=MALICIOUS)

    @property
    def colour(self):
        """
        Return the hexadecimal colour of this rating
        """
        self.COLOUR[self.ratingType]


class Source(models.Model):
    source_name = models.CharField(max_length=255) # the file name of a source
    date = models.DateTimeField('date detected')


class Record(models.Model):
    date = models.DateTimeField('date published')
    filename = models.CharField(max_length=255)
    action = models.CharField(max_length=50)
    submitType = models.CharField(max_length=50)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

