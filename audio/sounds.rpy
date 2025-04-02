## Sound Definitions

define audio.walkie_beep = "audio/walkie_beep.mp3"
define audio.door_chime = "audio/door_open.mp3"
define clock_tick = "audio/clock_tick.mp3"
define audio.store_ambience = "audio/store_ambience.mp3"

init python:
    def play_store_sounds():
        renpy.music.play("audio/store_ambience.mp3", channel="background", loop=True, fadeout=1.0)
        renpy.music.queue("audio/clock_tick.mp3", channel="sound", loop=True, tight=True)		Get-Content "C:\Users\me\bby day one beta\bby day one beta\game\audio\sounds.rpy" | Select-String "define audio|play|queue"