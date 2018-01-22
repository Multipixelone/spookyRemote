#!/usr/bin/env python
# Made by Multipixelone
# Main Script
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Sounds/myFile.wav")
pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#   continue
