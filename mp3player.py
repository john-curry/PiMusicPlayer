#!/usr/bin/python
import os
import os.path
import pygame as pg
from pygame import mixer as mx
from screen import my_screen

ms = my_screen()

mx.init(22050, -16, 2, 4096)

music = "/var/music/"

for filename in sorted(os.listdir(music)):
  if filename.endswith(".mp3"):
    p = os.path.join(music, filename)
    ms.message(filename) 
    mx.music.load(p)
    mx.music.play()
    while mx.music.get_busy() == True:
      continue
