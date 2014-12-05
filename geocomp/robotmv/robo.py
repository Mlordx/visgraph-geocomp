#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Classe que define o robo


"""

#from geocomp.common.segment import Segment
#from geocomp.common.prim import *
from geocomp.common.control import *
from geocomp.common.point import Point
from minhasPrim import *
from geocomp.common.polygon import Polygon



class Robo:
        """
          Recebe a lista de pontos do robo, definindo ele como
          um polígono simples em ordem anti-horária
        """
        
        def __init__(self, pontos):
		  self.pontos = pontos

        """
        def plot(self, xoff, yoff, color=config.COLOR_POINT):
                pontos = self.getPontos(xoff, yoff)
                for p in pontos:
                        p.plot()
                        
        """             

        """

        Devolve um polígono de R(xoff, yoff)

        """
                

        def getPontos(self, xoff, yoff):
            lista2 = []
            for p in self.pontos:
                    lista2.append(Point(p.x + xoff, p.y + yoff))
            return (lista2)

        """

        Recebe um poligono que define um obstáculo.

        Retorn um poligono representando a soma de minkowski
        entre o poligono e -R(0,0)

        """


        def deformaPolig(self, polig):
            pontosNeg = [Point(-p.x, -p.y) for p in self.pontos]
            #  j = len(self.pontos)-1;
            #  for i in range(len(self.pontos)):
            #          p = self.pontos[i]
            #          pontosNeg[j-i] = Point(-p.x, -p.y)
            return somaMinkowski(pontosNeg, polig)


