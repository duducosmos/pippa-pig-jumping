# -*- coding: utf-8 -*-
__author = "Eduardo S. Pereira"
__empresa = "Jabuticaba Digital Studio"
__data = "25/06/2014"
__email = "jabuticabads@gmail.com"

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.core.audio import SoundLoader

from game import MyGame
from mundo import Mundo

Factory.register("Mundo", Mundo)


class MyGameApp(App):
    title = "Pippa Pig Jumping"

    def on_pause(self):
        return True

    def build(self):
        game = MyGame()
        game.musicaTema = SoundLoader.load("./sounds/peppaTema.wav")
        game.gameOverSound = SoundLoader.load("./sounds/Sad_Trombone.wav")
        game.gameWinSound = SoundLoader.load("./sounds/KidsCheering.wav")
        game.start_menu()
        game.musicaTema.play()

        Clock.schedule_interval(game.update, 1.0 / 60)

        return game

if __name__ in ('__android__', '__main__'):
    MyGameApp().run()
