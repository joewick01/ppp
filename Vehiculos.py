# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:26:21 2020

@author: Joewick01
"""

class Vehiculo(): #clase nodriza (superclase)

    def __init__(self, color, ruedas, marca, modelo):
        self.color = color
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return "color {}, {} ruedas, marca {}, modelo {} ".format( self.color, self.ruedas, self.marca, self.modelo )


class Coche(Vehiculo): #clase hija (subclase)

    def __init__(self, color, ruedas, velocidad, cilindrada, marca, modelo):
        super().__init__(color, ruedas, marca, modelo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc,".format(
            self.velocidad, self.cilindrada)




class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga, marca, modelo):
        super().__init__(color, ruedas, velocidad, cilindrada, marca, modelo)
        self.carga = carga
        
        

    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)


class tractocamion(Camioneta):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga, marca, modelo):
        super().__init__(color, ruedas, velocidad, cilindrada, carga, marca, modelo)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo, marca, modelo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada) 


# def catalogar(vehiculos):
#    for v in vehiculos:
#        print(type(v).__name__, v)

def catalogar(vehiculos, ruedas=None):

    # Primera pasada, mostrar recuento
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas: 
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))

    # Segunda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)


lista = [
    Coche("azul", 4, 150, 1200, "dodge", "Spirit"),
    Camioneta("blanco", 4, 100, 1300, 1500, "ford", "carry all" ),
    tractocamion("rojo",10, 95, 15000, 20000, "kenworth", "T880" ),
    Bicicleta("verde", 2, "urbana", "alubike", "raptor"),
    Motocicleta("negro", 2, "deportiva", 180, 900)]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)
catalogar(lista, 10)
