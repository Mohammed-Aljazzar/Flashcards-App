from django.db import models

# Create your models here.
NUM_BOXES = 5 
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(choices=zip(BOXES, BOXES), default=BOXES[0])        # [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.question

