from django.shortcuts import render

# Create your views here.
from .models import Topic


def index(request):
    return render(request, "learning_logs/index.html")


def topics(request):
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.order_by(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {"topics": topics, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)
