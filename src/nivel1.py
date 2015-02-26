# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle
from  kivy.core.image import Image

from mundo import Mundo
from random import randint
from coletavel import Coletavel
from animation import Animation


class Nivel1(Mundo):
    #21600

    def __init__(self, player, backgroundImage, boss=None, tamanhoFase=21600,
                      **kwargs):
        super(Nivel1, self).__init__(**kwargs)

        self.start_background()

        self.player = player
        self.boss = boss

        if(self.boss):
            self.boss.startPlayer(self.player)

        if(self.player):
            self.player.velocity_x = 3
            self.playerAnim = Animation(self.player)
        else:
            self.playerAnim = None

        if(self.boss):
            self.bossAnim = Animation(self.boss)
        else:
            self.bossAnim = None

        self.somColetado = SoundLoader.load("./sounds/smw_coin.wav")
        self.soundOn = True

        self.fimNivel = False
        self.nivelPerdido = False
        self.pontos = 0
        self.tamanhoFase = tamanhoFase
        self.walked = 0
        self.timeGame = 30

        self.bolinhos = []
        self.extraTime = []
        self.__startBolinhos()
        self.__startExtraTime()

        with self.canvas:
            self.casinha = Rectangle(texture=Image("./images/casa.png").texture,
                                size=[Window.width * 0.5, Window.height * 0.7],
                                pos=[tamanhoFase + 300, 10]
                                )

    def __startBolinhos(self):

        r = list(range(0, Window.width, 200))

        for i in range(len(r)):
            tmp = Coletavel()
            tmp.velocity_x = 0.5
            tmp.imageObject(image="./images/cupcake.png",
                                 size=[40, 40])
            tmp.pos = [randint(r[i] - 100, r[i]), randint(100, 250)]

            self.add_widget(tmp)
            self.bolinhos.append(tmp)

    def colideBolinhos(self, diff):
        for k in self.bolinhos:
            if(self.player):
                if(k.collide_widget(self.player)):
                    if(self.soundOn):
                        self.somColetado.play()
                    k.coletado = True
                    self.pontos += 1
            k.update(diff)

    def colideTempo(self, diff):
        for k in self.extraTime:
            if(self.player):
                if(k.collide_widget(self.player)):
                    if(self.soundOn):
                        self.somColetado.play()
                    k.coletado = True
                    k.removido = True
                    self.timeGame += 30
            if(k.pos[0] < -1):
                k.removido = True
                k.coletado = True
            k.update(diff)

    def colidBoss(self):
        if(self.boss):
            if(self.boss.collide_widget(self.player)):
                if(self.boss.fimJogo is False):
                    if(self.player.pos[1] >= self.boss.height * 3 / 4):
                        self.boss.pos[0] -= 200
                        self.boss.fimJogo = True
                        self.boss.velocity_x = 0
                    else:
                        self.boss.velocity_x = 0
                        self.nivelPerdido = True

    def __startExtraTime(self):
        lastPos = self.tamanhoFase / 3

        for i in range(3):
            tmp = Coletavel()
            tmp.imageObject(image="./images/tempo.png", size=[40, 40])
            tmp.pos = [(1 + i) * lastPos, randint(100, 250)]
            self.add_widget(tmp)
            self.extraTime.append(tmp)

    def playerWindowDiff(self):

        diff = 0

        if(self.player.pos[0] <= 120):
                self.player.pos[0] = 120
        elif(self.player.pos[0] >= (Window.width / 2)):
            diff = - (self.player.pos[0] - (Window.width / 2))
            self.player.pos[0] = (Window.width / 2)

        return diff

    def update(self):
        diff = -3

        if(self.player):
            self.player.move()
            self.player.updateJump()
            diff = self.playerWindowDiff()
            self.playerAnim.update()

        if(self.boss):
            self.boss.soundOn = self.soundOn
            self.boss.update(diff)
            self.bossAnim.update()

        self.walked += - diff
        if(self.walked >= self.tamanhoFase):
            self.fimNivel = True

        self.casinha.pos = [self.casinha.pos[0] + diff, 10]

        self.update_background(diff)
        self.colideBolinhos(diff)
        self.colideTempo(diff)
        self.colidBoss()
