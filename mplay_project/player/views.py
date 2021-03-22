import os

from os import listdir
from os.path import isfile, join

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from .utils import (
    play_song, pause_song, unpause_song, play_next_song,
    play_previous_song
)


def HomeView(request):
    """
    View for Home page of app.
    """
    return render(request, 'homepage.html', {})


def MusicListView(request):
    """
    View for music listing.
    """
    context = dict()
    media_path = settings.MEDIA_ROOT
    music_files = { os.path.splitext(f)[0]: f for f in listdir(media_path)}
    context['music_files'] = music_files
    return render(request, 'song_list.html', context)


def MusicPlayView(request, *args, **kwargs):
    """
    View for music playback and controls.
    """
    name = kwargs.get('name')
    media_path = settings.MEDIA_ROOT
    file_path = join(media_path, name)
    print(file_path)
    if isfile(file_path):
        play_song(file_path)
        return render(request, "song_playback.html", {})
    else:
        return HttpResponse("<html><head></head><body>Not Found</body></html>")

def MusicPauseView(request):
    pause_song()
    return HttpResponse("<html><head></head><body>Paused</body></html>")

def MusicUnPauseView(request):
    unpause_song()
    return HttpResponse("<html><head></head><body>Resumed</body></html>")

def NextSongView(request):
    play_next_song()
    return HttpResponse("<html><head></head><body>Next Song Played</body></html>")

def PreviousSongView(request):
    play_previous_song()
    return HttpResponse("<html><head></head><body>Previous Song Played</body></html>")

# # Create your views here.
