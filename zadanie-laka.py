from turtle import *
from random import *


def hop(szerokosc,wysokosc):
   up() #żeby nie mazal podczas chodzenia
   fd(wysokosc)
   right(90)
   fd(szerokosc)
   left(90)
   down() #tez zeby nie mazac podczas chodzenia

def ini_grafika():
   mode('logo')
   reset()
   speed(0)

def tlo_laki(kolor, tlo):
   bgcolor('sky blue')
   color(kolor, tlo)  #drugi parametr jest do tła
   hop(-window_width()//2,-window_height()//2)
   begin_fill()
   fd(window_height()//3)
   rt(90)
   fd(window_width())
   rt(90)
   fd(window_height()//3)
   rt(90)
   fd(window_width())
   end_fill()
   hop(window_height()//3,0)

#Przeskakuje do pozycji początkowej (bez rysowania linii)
def jump_home():
   up()
   home()
   down()

def paprocie(ilosc_paprotek):
   jump_home()
   hop(-window_width()//2,-window_height()//2)
   for k in range(ilosc_paprotek):
      dx = randint(0,window_width())
      dy = randint(0, window_height()//3)
      bok = randint(20,100)
      hop(dx,dy)
      paprotka(bok)
      hop(-dx,-dy)

def paprotka(r): #r to bok paprotki
    begin_fill()
    color('green')

    rt(-45)
    fd(3*r//8)
    rt(45)
    fd(r//9)
    rt(135)
    fd(3*r//8)
    rt(-135)
    fd(2*r//9)

    rt(-45)
    fd(3*r//10)
    rt(45)
    fd(r//9)
    rt(135)
    fd(3*r//10)
    rt(-135)
    fd(2*r//9)

    rt(-45)
    fd(9*r//40)
    rt(45)
    fd(r//9)
    rt(135)
    fd(9*r//40)
    rt(-135)
    fd(2*r//9)

    rt(90)
    fd(r//9)
    rt(90)
    fd(2*r//9)

    rt(-135)
    fd(9*r//40)
    rt(135)
    fd(r//9)
    rt(45)
    fd(9*r//40)
    rt(-45)
    fd(2*r//9)

    rt(-135)
    fd(3*r//10)
    rt(135)
    fd(r//9)
    rt(45)
    fd(3*r//10)
    rt(-45)
    fd(2*r//9)

    rt(-135)
    fd(3*r//8)
    rt(135)
    fd(r//9)
    rt(45)
    fd(3*r//8)
    rt(45)
    fd(r//9)
    setheading(0)

    end_fill()

def biedronki(ilosc_biedronek):
   jump_home()
   hop(-window_width()//2,-window_height()//2)
   for k in range(ilosc_biedronek):
      dx = randint(0,window_width())
      dy = randint(0, window_height()//3)
      r = randint(10,40)
      angle = randint(0,360)
      hop(dx,dy)
      right(angle)
      biedronka(r)
      rt(-angle)
      up()
      goto(-window_width()//2,-window_height()//2)
      setheading(0)
      down()

def biedronka(r):

    begin_fill() #czarny prostokąt pod biedronką
    color('black')
    for i in range(2):
        fd(2*r)
        rt(90)
        fd(r)
        rt(90)
    end_fill()

    begin_fill()   #czerwony prostokąt na biedronkę
    color('red')
    for i in range(2):
        fd(3*r//2)
        rt(90)
        fd(r)
        rt(90)
    end_fill()


        # kropeczki na biedronce losowe tak jak w przyrodzie
    for i in range(7):
        rx = randint(r//6, 5*r//6)  #takie liczby ze wzgldu na to aby kropki nie wychodzily poza biedronke
        ry = randint(r//6, 0.9*3*r//2)
        hop(rx,ry)
        dot(r//4,'black')
        hop(-rx,-ry)

    #czułki
    hop(r//3,2*r)
    color('black')
    pensize(r//10)
    rt(-45)
    fd(r//2 )
    fd(-r//2)
    pensize(0)
    rt(135)
    fd(r//3)
    rt(-45)
    pensize(r//10)
    fd(r//2)
    fd(-r//2)
    pensize(0)
    setheading(0)

def motylki(ilosc_motylkow):
   jump_home()
   hop(-window_width()//2,-window_height()//2)
   hop(0,window_height()//3)
   for k in range(ilosc_motylkow):
      dx = randint(0,window_width())
      dy = randint(0,2*window_height()//3)
      r = randint(20,80)
      angle = randint(-90,90)
      hop(dx,dy)
      right(angle)
      kolory = ["yellow", "red", "black", "brown", "pink", "silver", "LightCoral", "light slate blue", "steel blue","tan4", "teal"]
      kolor1 = choice(kolory)
      kolor2 = choice(kolory)
      motyl(r//3,kolor1,kolor2)
      left(angle)
      hop(-dx,-dy)

def kwadrat(szerokosc, wysokosc,kolor):
   begin_fill()
   color(kolor, kolor)
   for k in range(2):
      forward(wysokosc)
      right(90)
      forward(szerokosc)
      right(90)
   end_fill()

def motyl(d,kolor1,kolor2):  #d to rozmiar kwadratu skrzydła

    hop(0, 3*d//42)  #lewe skrzydło
    kwadrat(d,d,kolor1)
    hop(d//4,d//4)
    kwadrat(d//2,d//2,kolor2)
    hop(d//4,3*d//4)
    kwadrat(d//2,d//2,kolor2)


    #tuluw
    hop(d//2,-45*d//42)

    # kwadrat(9*d//5,2*d//9,'black')
    begin_fill()
    color('black')
    for i in range(2):
        fd(9*d//5)
        rt(90)
        fd(2*d//9)
        rt(90)
    end_fill()

    hop(d//9,39*d//20)
    dot(d//3,'black')
    hop(d//9,-39*d//20)

    hop(0,3*d//42)         #prawe skrzydło
    kwadrat(d,d,kolor1)
    hop(d//4,d//4)
    kwadrat(d//2,d//2,kolor2)
    hop(-d//4,3*d//4)
    kwadrat(d//2,d//2,kolor2)
    hop(-11*d//9,-21*d//20)

def main():
    ini_grafika()
    tlo_laki('lawn green','lawn green')
    paprocie(20)
    motylki(20)
    biedronki(20)
    done()


main()

