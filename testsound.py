#!/usr/bin/env python
# Made by Multipixelone
# Main Script
import pyglet

music = pyglet.resource.media('test.wav')
music.play()

pyglet.app.run()
