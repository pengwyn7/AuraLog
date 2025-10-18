from django.shortcuts import render, redirect
from .models import MoodEntry
from datetime import date
from django.db.models import Avg

def home(request):
    if request.method == 'POST':
        mood_score = request.POST.get('mood_score')
        notes = request.POST.get('notes')
        MoodEntry.objects.update_or_create(
            date=date.today(),
            defaults={'mood_score': mood_score, 'notes': notes}
        )
        return redirect('home')

    entries = MoodEntry.objects.all().order_by('-date')
    avg_mood = MoodEntry.objects.aggregate(Avg('mood_score'))['mood_score__avg']
    context = {'entries': entries, 'avg_mood': avg_mood}
    return render(request, 'AuraLog/home.html', context)
