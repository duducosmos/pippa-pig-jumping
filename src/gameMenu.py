# -*- coding: utf-8 -*-
from kivy.core.window import Window
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
#from kivy.graphics import Rectangle
#from  kivy.core.image import Image


class GameMenu(Widget):

    size = [Window.width, Window.height]

    def startGameMenu(self):
        ypos = Window.height * 0.8
        sizeButton = [50, 50]
        self.playPause = Button(background_normal="./images/botoes/start0.png",
                                background_down="./images/botoes/start1.png",
                                size=sizeButton
                                )
        self.playPause.pos = [10, ypos]
        self.add_widget(self.playPause)

        self.soundControl = Button(
                                background_normal="./images/botoes/sound.png",
                                background_down="./images/botoes/sound0.png",
                                size=sizeButton)
        self.soundControl.pos = [70, ypos]

        self.add_widget(self.soundControl)

        self.restart = Button(background_normal="./images/botoes/restart.png",
                              background_down="./images/botoes/restart0.png",
                              size=sizeButton)

        self.restart.pos = [130, ypos]

        self.add_widget(self.restart)

        self.exit = Button(background_normal="./images/botoes/sair.png",
                           background_down="./images/botoes/sair0.png",
                           size=sizeButton)
        self.exit.pos = [190, ypos]

        self.add_widget(self.exit)

        self.labelPonto = Label(text="Points: ",
                                pos=[Window.width * 0.7, Window.height * 0.8]
                                )
        self.add_widget(self.labelPonto)
        self.labelTime = Label(text="Time: ",
                                pos=[Window.width * 0.7, Window.height * 0.75]
                                )
        self.add_widget(self.labelTime)
