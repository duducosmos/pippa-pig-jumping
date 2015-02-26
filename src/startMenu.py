# -*- coding: utf-8 -*-
from kivy.core.window import Window
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.popup import Popup
#from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from  kivy.core.image import Image


class StartMenu(Widget):

    size = [Window.width, Window.height]

    def start_menu(self, titulo):
        sizeButton = [50, 50]
        ypos = Window.height * 0.8
        imageTitulo = Image(titulo).texture
        centerImage = Window.width * 0.5 - Window.width * 0.7 / 2
        imageBackground = Image("./images/fundo.png").texture

        with self.canvas:
            self.background = Rectangle(texture=imageBackground,
                                        center=self.center,
                                        size=[Window.width, Window.height]
                                        )
            self.titulo = Rectangle(texture=imageTitulo,
                                    pos=[centerImage, Window.height * 0.4],
                                    size=[Window.width * 0.7,
                                          Window.height * 0.4]
                                    )
            self.pippa = Rectangle(texture=Image(
                                        "./images/botoes/pippa.png").texture,
                                    pos=[Window.width / 2 - 40,
                                         Window.height * 0.05]
                )

        self.soundControl = Button(
                                background_normal="./images/botoes/sound.png",
                                background_down="./images/botoes/sound0.png",
                                size=sizeButton)
        self.soundControl.pos = [10, ypos]

        self.add_widget(self.soundControl)

        self.exit = Button(background_normal="./images/botoes/sair.png",
                           background_down="./images/botoes/sair0.png",
                           size=sizeButton)
        self.exit.pos = [70, ypos]

        self.add_widget(self.exit)

        self.startButton = Button(background_normal="./images/botoes/play.png",
                                  background_down="./images/botoes/play1.png")
        self.startButton.pos = [Window.width / 2 - 40, Window.height * 0.4]
        self.add_widget(self.startButton)
