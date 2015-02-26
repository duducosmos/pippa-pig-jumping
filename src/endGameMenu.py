# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"
from kivy.core.window import Window
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from  kivy.core.image import Image


class EndGameMenu(Widget):
    size = [Window.width, Window.height]

    def __init__(self, win=True, **kwargs):
        super(EndGameMenu, self).__init__(**kwargs)
        self.__start(win=win)

    def __start(self, win=True):
        sizeButton = [60, 60]
        centerImage = Window.width * 0.5 - Window.width * 0.7 / 2

        with self.canvas:
            self.background = Rectangle(
                                    texture=Image("./images/fundo.png").texture,
                                        center=self.center,
                                        size=[Window.width, Window.height]
                                        )
            if(win is True):
                self.winGame = Rectangle(
                                texture=Image("./images/win.png").texture,
                                pos=[centerImage, Window.height * 0.4],
                                size=[Window.width * 0.7,
                                          Window.height * 0.4]
                                )

        self.restart = Button(background_normal="./images/botoes/restart.png",
                              background_down="./images/botoes/restart0.png",
                              size=sizeButton)

        self.label = Label(text="Fim",
                    pos=[Window.width / 2 - 65, Window.height * 0.4])
        self.add_widget(self.label)

        self.restart.pos = [Window.width / 2 - 65, Window.height * 0.3]

        self.add_widget(self.restart)

        self.exit = Button(background_normal="./images/botoes/sair.png",
                           background_down="./images/botoes/sair0.png",
                           size=sizeButton)
        self.exit.bind(on_press=self.__exit)

        self.exit.pos = [Window.width / 2 + 5, Window.height * 0.3]

        self.add_widget(self.exit)

    def __exit(self, instance):
        import sys
        sys.exit()


class GameOverMenu(EndGameMenu):

    def __init__(self, **kwargs):
        super(GameOverMenu, self).__init__(win=False, **kwargs)
        centerImage = Window.width * 0.5 - Window.width * 0.7 / 2
        self.winGame = None

        with self.canvas:
            self.winGame = Rectangle(
                                texture=Image("./images/tryAgain.png").texture,
                                pos=[centerImage, Window.height * 0.4],
                                size=[Window.width * 0.7,
                                          Window.height * 0.4]
                                )
