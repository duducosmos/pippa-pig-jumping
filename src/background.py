# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.core.window import Window

from kivy.graphics import Rectangle


class Fundo(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    rect = None

    def __init__(self, image, pos=None, **kwargs):
        super(Fundo, self).__init__(**kwargs)

        if(pos is None):
            pos = self.pos

        self.start(image, pos)

    def start(self, image, pos):
        with self.canvas:
            self.rect = Rectangle(texture=image,
                                  size=[Window.width, Window.height],
                                  pos=pos)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        maxDist = Window.width
        if(self.pos[0] <= -maxDist and self.velocity_x < 0):
            self.pos[0] += 2 * maxDist
        elif(self.pos[0] >= maxDist and self.velocity_x > 0):
            self.pos[0] -= 2 * maxDist

        self.rect.pos = self.pos
