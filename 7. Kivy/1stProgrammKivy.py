#!/usr/bin/python3
# https://kivy.org/#home
#1 Напишем первую программу на киви, которая просто создаст пустое окно программы и кнопку. А так же заставим сделать так чтоб двигалась палцами по экрану кнопка.
from kivy.app import App
from kivy.uix.button import Button # 6 Вернем кнопки
from kivy.uix.codeinput import CodeInput # 15 Хотим что то написать в поле
from pygments.lexers import HtmlLexer # 16 
from kivy.config import Config # 18 хотим изменить экран
Config.set('graphics','resizable','0') # 19 Окно должно менять размер
Config.set('graphics','width','700')
Config.set('graphics','height','400')
from kivy.uix.floatlayout import FloatLayout# 20 Хотим чтобы кнопка не занимала весь экран и находилась по центру
from kivy.uix.scatter import Scatter # 23 Хотим сделать, на подобие Сенсора, то есть палцами по экрану двигать эту кнопку
class MyApp(App): #2 Создаем класс, который назовем как MyApp, и он будет производным от App
    # pass # 3 и пока, он будет пустым
    def build(self): # 7 Создаем метод build
        #return Button() # 8 Пустая кнопка
        """9 при вводе мы получаем уже кнопку,занимающая ввесь экран, который при клике на экран меняет цвет, Здесь можно получить инфу:
        https://kivy.org/doc/stable/api-kivy.uix.button.html?highlight=uix#module-kivy.uix.button"""
        #return CodeInput(Lexer=HtmlLexer())# 17 на экране будет поле, в котором можно написать например html код
        s=Scatter() # 24
        fl=FloatLayout(size=(300,300))# 21
        s.add_widget(fl) # 25
        """return Button(text="eto moiya pervaiya knopka", 
                font_size=30,
                on_press=self.btn_press,
                background_color=[1,0,0,1], 
                background_normal='') # 10 Добавим текст и чтоб было какое-то событие у кнопки красно яркого цвета"""
        fl.add_widget(Button( text="eto moiya pervaiya knopka",
                              font_size=16,
                              on_press=self.btn_press,
                              background_color=[1,0,0,1],
                              background_normal='',
                              size_hint=(.5, .25),
                              pos=(640/2-160, 480/2-(480*.25/2)))); # 22 позиция кнопки
        #return fl
        return s
        """Сolor mainya proga kotoraya otvechet za cvet"""
    def btn_press(self, instance): # 11 Экземпляр кнопки
        print("Knopka najata") # 12 Выводим на консоли это
        instance.text="meniya najali"# 13 после того как кнопку  нажали, можем поменять текст
if __name__ == "__main__": # 4 После этого мы проверяем, что текущий модуль у нас - main
    MyApp().run() # 5 и если это так, то мы создаем экземпляр класса MyApp и сразу запускаем метод run
