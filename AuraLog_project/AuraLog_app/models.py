from django.db import models
from datetime import date

class MoodEntry(models.Model):
    date = models.DateField(default=date.today, unique=True)
    mood_score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - Mood {self.mood_score}"
