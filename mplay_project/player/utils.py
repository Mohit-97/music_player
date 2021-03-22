import os
import random

from os import listdir
from os.path import isfile, join
from pygame import mixer
from pydub import AudioSegment

from django.conf import settings

current_song = ""
previous_song = []
playing_song = False
mixer.init()

def convert_mp3_to_ogg(file_path):
    to_path = file_path.rsplit( ".", 1 )[ 0 ] + ".ogg"

    AudioSegment.from_file(
        file_path
    ).export(
        to_path,format='ogg'
    )
    os.remove(file_path)

    return to_path

def play_song(file_path):
    global current_song
    global playing_song

    if file_path.rsplit( ".", 1 )[1] != "ogg":
        file_path = convert_mp3_to_ogg(file_path)

    if playing_song:
        pause_song()

    mixer.music.load(file_path)
    current_song = file_path
    playing_song = True
    mixer.music.play()


def pause_song():
    mixer.music.pause()

def unpause_song():
    mixer.music.unpause()

def play_next_song():
    global previous_song

    previous_song.append(current_song)
    media_path = settings.MEDIA_ROOT
    music_files = [f for f in listdir(media_path) if isfile(join(media_path, f))]
    eligible_songs = list(set(music_files) - set([current_song]))
    random.shuffle(eligible_songs)

    random_song = media_path + '/' + eligible_songs[0]
    pause_song()
    play_song(random_song)


def play_previous_song():
    global previous_song
    global current_song

    if prev_song:
        prev_song = previous_song.pop()
        pause_song()
        play_song(prev_song)






