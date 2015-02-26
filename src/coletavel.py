# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from  kivy.core.image import Image
from kivy.graphics import Rectangle
from kivy.vector import Vector
from kivy.core.window import Window
from random import randint


class Coletavel(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    coletado = False
    removido = False
    rect = Rectangle()
    size = [Window.height * 0.01, Window.height * 0.01]

    def imageObject(self, image, size):
        imageObj = Image(image).texture
        with self.canvas:
            self.rect = Rectangle(texture=imageObj, size=size)

    def update(self, diff):
        self.velocity_x = diff

        if(self.coletado is True):
            if(self.removido is False):
                self.pos = [self.pos[0] + Window.width, randint(150, 250)]
                self.coletado = False
            else:
                self.pos = [0, -50]

        self.move()

        self.rect.pos = self.pos

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        maxDist = (150)
        if(self.pos[0] <= -maxDist and self.velocity_x < 0):
            self.pos = [self.pos[0] + 2 * Window.width, randint(150, 250)]
