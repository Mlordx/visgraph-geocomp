#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Algoritmo de Grafo de Visibilidade"""


from geocomp.common.polygon import Polygon
from geocomp.common.point import Point
from geocomp.common import control
from geocomp.common import prim
from geocomp import config


"""Função do algoritmo em si. Supomos aqui que:

-> Os primeiros pontos são o polígono que definem o robo. O
	polígono acaba no momento em que se repete o primeiro ponto.
	Se os 2 primeiros pontos forem iguais, o robo é um robo pontual
	definido por esse ponto repetido.

-> Os outros polígonos, limitados da mesma forma, serão os obstáculos
	do robo. 


"""

def visGraphAlg(l):
	print "HUE2"
	poligs = leEntrada(l)

	robo = poligs[0]
	if(len(robo) == 1):
		print "Robo ponto na posicao ", robo[0] 
		probo = robo[0]
		probo.hilight('green')
	else:
		print "Busca de rotas para robos não pontuais não implementado ainda"



	poligTeste1 = Polygon(poligs[1])
	#poligTeste1.hilight();

"""
	# Desenho o primeiro poligono...seria bom se parar isso em outra
	# função depois
	for i in range(len(poligs[1])-1):
		poligs[1][i].lineto(poligs[1][i+1])
	poligs[1][len(poligs[1])-1].lineto(poligs[1][0])

"""




def leEntrada(l):
	poligs = []
	temp = []
	for i in range(len(l)):
		if( len(temp) == 0 ): 
			temp.append(l[i])
		elif( l[i].x == temp[0].x and l[i].y == temp[0].y ):
			poligs.append(temp)
			temp = []
		else:
			temp.append(l[i])
	return poligs


	
