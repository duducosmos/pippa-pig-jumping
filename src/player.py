# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from  kivy.core.image import Image
from kivy.graphics import Rectangle

from constants import PLAYER_VY0, GRAVITY, PLAYER_VX0, PLAYER_VXJUMPING


class Player(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    image_R = []
    image_L = []
    image_fim = []
    image_Jumping_L = []
    image_Jumping_R = []
    jumping = False
    jumped = False
    fimJogo = False
    maxRight = 100
    minRight = 0
    timeAir = 0
    maxTimeAir = 200
    animRate = 0
    timeGame = 0

    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.startImage()
        self.startCanvas()

    def startCanvas(self):

        with self.canvas:
            self.rect = Rectangle(texture=self.image_R[0], size=self.size)

    def startImage(self):
        myimage = Image("./images/pippaSheet.png").texture

        #0
        self.image_R.append(myimage.get_region(0, 0, 150, 170))

        #4
        self.image_R.append(myimage.get_region(150 * 3, 0, 150, 170))

        #7
        self.image_R.append(myimage.get_region(150 * 6, 0, 150, 170))

        #6
        self.image_R.append(myimage.get_region(150 * 5, 0, 150, 170))

        #2
        self.image_R.append(myimage.get_region(150 * 4, 0, 150, 170))

        #4
        self.image_R.append(myimage.get_region(150 * 5, 0, 150, 170))

        self.image_Jumping_R.append(myimage.get_region(150 * 1, 0, 150, 170))
        self.image_Jumping_R.append(myimage.get_region(150 * 2, 0, 150, 170))

        myimage = Image("./images/pippaSheetL.png").texture

        #7
        self.image_L.append(myimage.get_region(150 * 7, 0, 150, 170))

        #4
        self.image_L.append(myimage.get_region(150 * 2, 0, 150, 170))

        #7
        self.image_L.append(myimage.get_region(150 * 5, 0, 150, 170))

        #6
        self.image_L.append(myimage.get_region(150 * 4, 0, 150, 170))

        #2
        self.image_L.append(myimage.get_region(150 * 3, 0, 150, 170))

        #4
        self.image_L.append(myimage.get_region(150 * 4, 0, 150, 170))

        self.image_Jumping_L.append(myimage.get_region(150 * 0, 0, 150, 170))
        self.image_Jumping_L.append(myimage.get_region(150 * 1, 0, 150, 170))

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.rect.pos = self.pos

    def jump(self):
        self.jumped = True
        if(self.pos[1] <= 40):
            self.velocity_y = PLAYER_VY0
            self.jumping = True

    def updateJump(self):

        if(self.jumped):
            self.jumped = False

        if(self.jumping):
            self.timeAir += 1
            if(self.timeAir == 2):
                self.timeGame += 1
                self.timeAir = 0

            self.velocity_y -= GRAVITY * self.timeGame
            if(self.velocity_x > 0):
                self.velocity_x = PLAYER_VXJUMPING
            else:
                self.velocity_x = - PLAYER_VXJUMPING

            if(self.velocity_y + self.pos[1] < 0):
                self.pos[1] = 10
                self.velocity_y = 0
                self.timeAir = 0
                self.timeGame = 0
                self.jumping = False
                if(self.velocity_x > 0):
                    self.velocity_x = PLAYER_VX0
                else:
                    self.velocity_x = - PLAYER_VX0