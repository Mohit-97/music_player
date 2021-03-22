from django.urls import path

from player.views import (
    MusicListView, MusicPlayView, MusicPauseView, MusicUnPauseView,
    NextSongView, PreviousSongView
)

urlpatterns = [
    path('list/', MusicListView, name="music_list"),
    path('play/<str:name>/', MusicPlayView, name="play_music"),
    path('pause/', MusicPauseView, name="pause_music"),
    path('unpause/', MusicUnPauseView, name="unpause_music"),
    path('nextsong/', NextSongView, name="next_song"),
    path('prevsong/', PreviousSongView, name="previous_song"),
]
