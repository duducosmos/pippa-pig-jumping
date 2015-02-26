# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from  kivy.core.image import Image


class Animation:

    def __init__(self, player):
        """

        """
        self.player = player
        self.animRate = 0
        self.ANIMVELOC = 2
        self.MAXTIMEANIM = 3000
        self.lastPos = "R"

    def __animation(self):

        if(self.player.fimJogo is False):
            if(self.player.jumping is False and self.player.jumped is False):

                if(self.player.velocity_x > 0):
                    frame = (self.animRate // 30) % len(self.player.image_R)
                    self.player.rect.texture = self.player.image_R[frame]
                    self.lastPos = "R"
                elif(self.player.velocity_x < 0):
                    frame = (self.animRate // 30) % len(self.player.image_L)
                    self.player.rect.texture = self.player.image_L[frame]
                    self.lastPos = "L"
                else:
                    if(self.lastPos == "R"):
                        self.player.rect.texture = self.player.image_R[0]
                    else:
                        self.player.rect.texture = self.player.image_L[0]

            else:
                if(self.player.jumping):
                    if(self.lastPos == "R"):
                        frame = (self.animRate // 30) % \
                                len(self.player.image_Jumping_R)
                        self.player.rect.texture = \
                            self.player.image_Jumping_R[frame]
                    elif(self.lastPos == "L"):
                        frame = (self.animRate // 30) % \
                                len(self.player.image_Jumping_L)
                        self.player.rect.texture = \
                            self.player.image_Jumping_L[frame]
        else:
            frame = (self.animRate // 30) % len(self.player.image_fim)
            self.player.rect.texture = self.player.image_fim[frame]

    def update(self):
        if(self.animRate <= self.MAXTIMEANIM):
            if(not self.animRate % 10):
                self.__animation()
            self.animRate += self.ANIMVELOC
        else:
            self.animRate = 0


