# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.core.window import Window
from background import Fundo
from  kivy.core.image import Image


class Mundo(Widget):

    soundOn = True

    def __init__(self, **kwargs):
        super(Mundo, self).__init__(**kwargs)
        self.start_background()

    def start_background(self):
        fundo = Image("./images/ForestBackground/fundo.png").texture
        nuvens = Image("./images/ForestBackground/nuvens.png").texture
        arvore1 = Image("./images/ForestBackground/arvores1.png").texture
        arvore2 = Image("./images/ForestBackground/arvores2.png").texture
        arvore3 = Image("./images/ForestBackground/arvores3.png").texture
        #flores = Image("./images/ForestBackground/flores.png").texture

        self.background = [Fundo(fundo), Fundo(nuvens), Fundo(arvore1),
                           Fundo(arvore2), Fundo(arvore3)
                           #Fundo(flores)
                           ]

        self.background2 = [Fundo(fundo, pos=[Window.width, self.pos[1]]),
                            Fundo(nuvens, pos=[Window.width, self.pos[1]]),
                            Fundo(arvore1, pos=[Window.width, self.pos[1]]),
                            Fundo(arvore2, pos=[Window.width, self.pos[1]]),
                            Fundo(arvore3, pos=[Window.width, self.pos[1]])
                            #Fundo(flores, pos=[Window.width, self.pos[1]])
                            ]

        for k in range(len(self.background)):
            self.add_widget(self.background[k])
            self.add_widget(self.background2[k])

        for k in self.background2:
            k.pos = [Window.width, 0]

    def update_background(self, diff):

        velocit_back = lambda x: (float(diff) /
                                        float(len(self.background) - 1)) * x

        i = 0

        for k in range(len(self.background)):
            self.background[k].velocity_x = velocit_back(i)
            self.background[k].move()
            self.background2[k].velocity_x = velocit_back(i)
            self.background2[k].move()
            i += 1

    def update(self, diff):
        self.update_background(diff)
