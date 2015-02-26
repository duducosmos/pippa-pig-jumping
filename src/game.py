# -*- coding: utf-8 -*-
"""
Main Game Loop
"""

__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window
import pygame

from startMenu import StartMenu
from gameMenu import GameMenu
from nivel1 import Nivel1
from player import Player
from boss import Boss
from endGameMenu import EndGameMenu, GameOverMenu
from constants import PLAYER_VX0


try:
    import android
except ImportError:
    android = None


class MyGame(Widget):

    menu = ObjectProperty(None)
    gameMenu = ObjectProperty(None)
    player = ObjectProperty(None)
    boss = ObjectProperty(None)
    endGameMenu = ObjectProperty(None)
    gameOverMenu = ObjectProperty(None)

    #Sons
    musicaTema = ObjectProperty(None)
    gameOverSound = ObjectProperty(None)
    gameWinSound = ObjectProperty(None)

    gamePause = True
    currentTime = NumericProperty(0)
    timeGame = NumericProperty(30)
    soundOn = True
    temaPlaying = False
    niveis = []
    nivelCorrente = 0

    if(android):
        android.init()
        android.accelerometer_enable(True)
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    def start_menu(self):
        self.menu = StartMenu()
        self.menu.start_menu("./images/titulo.png")
        self.menu.startButton.bind(on_release=self.__removeStartMenu)
        self.menu.soundControl.bind(on_press=self.__soundOnOff)
        self.menu.exit.bind(on_press=self.__exit)
        self.add_widget(self.menu)
        self.gameMenu = GameMenu()
        self.gameMenu.startGameMenu()
        self.gameMenu.playPause.bind(on_press=self.__playPause)
        self.gameMenu.soundControl.bind(on_press=self.__soundOnOff)
        self.gameMenu.exit.bind(on_press=self.__exit)
        self.gameMenu.restart.bind(on_press=self.__restarCurrentLevelMenu)
        self.endGameMenu = EndGameMenu()
        self.endGameMenu.restart.bind(on_press=self.__restartCurrentLevel)
        self.gameOverMenu = GameOverMenu()
        self.gameOverMenu.restart.bind(on_press=self.__restartCurrentLevelOver)

    def __restartCurrentLevelOver(self, instance):

        if(self.gameOverSound.state == "play"):
            self.gameOverSound.stop()
        if(self.gameWinSound.state == "play"):
            self.gameWinSound.stop()

        self.player = Player()
        self.player.pos = [200, 10]
        self.lobo = Boss()

        self.niveis[self.nivelCorrente] = None
        self.niveis[self.nivelCorrente] = Nivel1(player=self.player,
                                  backgroundImage="./images/fundo.png",
                                  boss=self.lobo
                                  )

        self.niveis[0].soundOn = self.soundOn
        self.lobo.pos = [self.niveis[0].tamanhoFase / 3, 10]

        self.add_widget(self.niveis[0])
        self.add_widget(self.player)
        self.add_widget(self.lobo)
        self.add_widget(self.gameMenu)
        self.remove_widget(self.gameOverMenu)
        self.gamePause = False

    def __restarCurrentLevelMenu(self, instance):
        self.remove_widget(self.niveis[self.nivelCorrente])
        self.remove_widget(self.gameMenu)
        self.remove_widget(self.player)
        self.remove_widget(self.lobo)
        self.__restartCurrentLevel(instance)

    def __restartCurrentLevel(self, instance):

        if(self.gameOverSound.state == "play"):
            self.gameOverSound.stop()
        if(self.gameWinSound.state == "play"):
            self.gameWinSound.stop()

        self.player = Player()
        self.lobo = Boss()

        self.player.pos = [200, 10]
        self.niveis[self.nivelCorrente] = None
        self.niveis[self.nivelCorrente] = Nivel1(player=self.player,
                                  backgroundImage="./images/fundo.png",
                                  boss=self.lobo
                                  )

        self.niveis[0].soundOn = self.soundOn
        self.lobo.pos = [self.niveis[0].tamanhoFase / 3, 10]

        self.add_widget(self.niveis[0])
        self.add_widget(self.player)
        self.add_widget(self.lobo)
        self.add_widget(self.gameMenu)
        self.remove_widget(self.endGameMenu)
        self.gamePause = False

    def __startNiveis(self):
        self.player = Player()
        self.lobo = Boss()
        self.player.pos = [200, 10]

        self.niveis.append(Nivel1(player=self.player,
                                  backgroundImage="./images/fundo.png",
                                  boss=self.lobo
                                  ))
        self.lobo.pos = [self.niveis[0].tamanhoFase / 3, 10]

        self.niveis[0].soundOn = self.soundOn

        self.add_widget(self.niveis[0])
        self.add_widget(self.player)
        self.add_widget(self.lobo)

    def __removeStartMenu(self, instance):
        self.gamePause = False
        self.remove_widget(self.menu)
        self.__startNiveis()
        self.add_widget(self.gameMenu)

    def __addStartMenu(self, instance):
        self.add_widget(self.menu)

    def __playPause(self, instance):
        if(self.gamePause is True):
            self.gamePause = False
            self.gameMenu.playPause.background_normal = \
                    "./images/botoes/start0.png"
        else:
            self.gamePause = True
            self.gameMenu.playPause.background_normal = \
                     "./images/botoes/pause0.png"

    def __soundOnOff(self, instance):
        if(self.soundOn is True):
            self.soundOn = False
            self.gameMenu.soundControl.background_normal = \
                    "./images/botoes/mute.png"
            if(self.menu):
                self.menu.soundControl.background_normal = \
                    "./images/botoes/mute.png"
        else:
            self.soundOn = True
            self.gameMenu.soundControl.background_normal = \
                    "./images/botoes/sound.png"
            if(self.menu):
                self.menu.soundControl.background_normal = \
                    "./images/botoes/sound.png"

    def __exit(self, instance):
        import sys
        sys.exit()

    def on_touch_move(self, touch):
        if(touch.y < Window.height * 0.8 - 100):
            if(self.player):
                self.player.jump()

    def updateNivel(self, dt):
        self.niveis[self.nivelCorrente].soundOn = self.soundOn
        self.niveis[self.nivelCorrente].update()

        self.gameMenu.labelPonto.text = "Points: " + \
                        str(self.niveis[self.nivelCorrente].pontos)

        self.gameMenu.labelTime.text = "Time: " + \
                                str(self.niveis[self.nivelCorrente].timeGame)

        self.currentTime += 1
        if(self.currentTime >= 60):
            self.currentTime = 0
            self.niveis[self.nivelCorrente].timeGame -= 1

        if(self.niveis[self.nivelCorrente].fimNivel):
            if(self.soundOn):
                self.gameWinSound.play()
            self.gamePause = True
            self.remove_widget(self.niveis[self.nivelCorrente])
            self.remove_widget(self.gameMenu)
            self.remove_widget(self.player)
            self.remove_widget(self.lobo)
            self.endGameMenu.label.text = "Points: " \
                    + str(self.niveis[self.nivelCorrente].pontos)
            self.add_widget(self.endGameMenu)

        if(self.niveis[self.nivelCorrente].timeGame <= 0 or
            self.niveis[self.nivelCorrente].nivelPerdido is True):
            if(self.soundOn):
                self.gameOverSound.play()
            self.gamePause = True
            self.remove_widget(self.niveis[self.nivelCorrente])
            self.remove_widget(self.gameMenu)
            self.remove_widget(self.player)
            self.remove_widget(self.lobo)
            self.gameOverMenu.label.text = "Points: " \
                    + str(self.niveis[self.nivelCorrente].pontos)
            self.add_widget(self.gameOverMenu)

    def __movingPlayerAndroid(self):
        if(android):
            accelerometer = android.accelerometer_reading()
            if(accelerometer[1] < -3 and self.player.jumping is False):
                self.player.velocity_x = -PLAYER_VX0
            elif(accelerometer[1] > 3 and self.player.jumping is False):
                self.player.velocity_x = PLAYER_VX0
            else:
                if(self.player.jumping is False):
                    self.player.velocity_x = 0

    def update(self, dt):

        if(android):
            if android.check_pause():
                if(self.musicaTema.state == "play"):
                    self.musicaTema.stop()
                android.wait_for_resume()

        if(self.soundOn is True):
            if(self.musicaTema.state == "stop"):
                self.musicaTema.play()
                self.musicaTema.volume = 0.3
        else:
            if(self.musicaTema.state == "play"):
                self.musicaTema.stop()
                self.musicaTema.volume = 0.3

        if(self.gamePause is not True):
            self.__movingPlayerAndroid()
            self.updateNivel(dt)
