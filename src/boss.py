# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from  kivy.core.image import Image
from kivy.graphics import Rectangle
from kivy.core.window import Window
from constants import BOSSVELOCX
from kivy.core.audio import SoundLoader


class Boss(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    refPos_x = NumericProperty(0)
    refPos_y = NumericProperty(0)
    refPos = ReferenceListProperty(refPos_x, refPos_y)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    image_R = []
    image_L = []
    image_fim = []
    image_Jumping = []
    animRate = 0

    coletado = False
    removido = False

    rect = Rectangle()

    jumping = False
    jumped = False
    fimJogo = False

    maxRight = 100
    minRight = 0
    timeAir = 0
    maxTimeAir = 200

    player = None
    uivar = True
    moving = False

    uivarSound = SoundLoader.load("./sounds/lobo_uivar.wav")

    def __init__(self, **kwargs):
        super(Boss, self).__init__(**kwargs)
        self.startImage()
        self.startCanvas()

    def startCanvas(self):

        with self.canvas:
            self.rect = Rectangle(texture=self.image_R[0], size=self.size)

    def startImage(self):
        myimage = Image("./images/loboSheetR.png").texture

        #0
        self.image_R.append(myimage.get_region(150 * 7, 0, 150, 170))

        #4
        self.image_R.append(myimage.get_region(150 * 2, 0, 150, 170))

        #7
        self.image_R.append(myimage.get_region(150 * 5, 0, 150, 170))

        #6
        self.image_R.append(myimage.get_region(150 * 3, 0, 150, 170))

        #2
        self.image_R.append(myimage.get_region(150 * 6, 0, 150, 170))

        #4
        self.image_R.append(myimage.get_region(150 * 3, 0, 150, 170))

        self.image_fim.append(myimage.get_region(150 * 8, 0, 150, 170))
        self.image_fim.append(myimage.get_region(150 * 9, 0, 150, 170))
        self.image_fim.append(myimage.get_region(150 * 10, 0, 150, 170))

        myimage = Image("./images/loboSheetL.png").texture

        #7
        self.image_L.append(myimage.get_region(150 * 7, 0, 150, 170))

        #4
        self.image_L.append(myimage.get_region(150 * 2, 0, 150, 170))

        #7
        self.image_L.append(myimage.get_region(150 * 5, 0, 150, 170))

        #6
        self.image_L.append(myimage.get_region(150 * 3, 0, 150, 170))

        #2
        self.image_L.append(myimage.get_region(150 * 6, 0, 150, 170))

        #4
        self.image_L.append(myimage.get_region(150 * 3, 0, 150, 170))

    def startPlayer(self, player):
        self.player = player

    def __update(self, diff):

        if(self.player):
            dist = self.pos[0] - self.player.pos[0]
            if(abs(dist) < 800):
                self.moving = True

                if(self.uivar is True and self.uivarSound.state == "stop"):
                    self.uivarSound.play()
                    self.uivar = False

            if(self.moving is True
               and dist <= 1400 and dist >= - 1400 and self.velocity_x < 0):
                self.velocity_x = - BOSSVELOCX
            elif(dist < - 1400 and self.velocity_x < 0):
                self.velocity_x = BOSSVELOCX + diff
                self.uivar = True
            elif(dist > 1400 and self.velocity_x > 0):
                self.velocity_x = - BOSSVELOCX - diff
                self.uivar = True

            if(self.moving is False):
                self.velocity_x = diff

        if(self.coletado is True):
            if(self.removido is False):
                self.pos = [self.pos[0] + Window.width, 10]
                self.coletado = False
            else:
                self.pos = [0, -50]

        self.move()

        self.rect.pos = self.pos

    def __isAlive(self, diff):
        if(self.fimJogo is True):
            dist = self.pos[0] - self.player.pos[0]
            if(abs(dist) > 1400):
                self.fimJogo = False
            self.velocity_x = diff
            self.move()
            self.rect.pos = self.pos
        else:
            self.__update(diff)

    def update(self, diff):
        self.__isAlive(diff)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos