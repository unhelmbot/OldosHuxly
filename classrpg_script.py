#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Юлия
#
# Created:     17.05.2018
# Copyright:   (c) Юлия 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import random
class heroesx():
    def __init__ (self,dmg,hp,name,race,lvl,history):
        global dmg,hp,name,race,atributs,history
        self.dmg = dmg
        self.hp = hp
        self.name = name
        self.race = race
        self.lvl = lvl
        self.atributs = atributs
        self.history = history
    def heroesout(self):
        print("Hero name=",self.name)
        print("Damage=",self.dmg)
        print("Hp=",self.hp)
class lvl():
    def __init__(self):


    def lvlinfo(5lvl,10lvl,15lvl,20lvl,25lvl,30lvl,35lvl,40lvl,45lvl,50lvl,55lvl,60lvl):
        5lvl = 'exp100'
        10lvl = 'exp150'
        15lvl = 'exp200'
        20lvl = 'exp250'
        25lvl = 'exp300'
        30lvl = 'exp350'
        35lvl = 'exp400'
        40lvl = 'exp450'
        45lvl = 'exp500'
        50lvl = 'exp550'
        55lvl = 'exp600'
        60lvl = 'exp650'





class atributsx():
    def __init__(self,power,intellect,charism,agility,resistance,speed):
        self.power = power
        self.intellect = intellect
        self.charism = charism
        self.agility = agility
        self.resistance = resistance
        self.speed = speed
    def atributsinfo(power,intellect,charism,agility,resistance,speed):
        power = 'Power get you powerful (+1lvl - melee damage +1)'
        intellect = 'Intellect makes you smarter (+1lvl - +5% exp. for all)'
        charism = 'charism makes you richer(+1lvl - -5% of the item price and +2lvl - +100 money for money loot (from 1000))'
        agility = 'agility makes you more focused and cunning (+1lvl - range damage +1 and with 5 lvl gives you a chance to put extra attack(+2lvl - +2 point of dodge)'
        resistance = 'resistance makes you more protected from melee attacks(+1lvl = -5% from enemy damage)'
        speed = 'speed makes you more faster (+1lvl - +1 move on the map)'



    def atribout():



class racex():


