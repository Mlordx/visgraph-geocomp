#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Algoritmo de Grafo de Visibilidade"""


from geocomp.common.polygon import Polygon
from geocomp.common.point import Point
from geocomp.common import control
from geocomp.common.guiprim import *
from geocomp import config
from tree import Tree


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

	poligs.pop(0) #Tira o robo da lista de polígonos
	pontos = []
	for i in range(len(poligs)):
		poligs[i] = Polygon(poligs[i])
		poligs[i].hilight()
		pontos.extend(poligs[i].to_list())

	print pontos
	#print compara(pontos[3], pontos[1])
	pontos.sort(criaCompara(probo), reverse = True)
	print pontos

	for i in range(len(pontos)):
		pontos[i].hilight('blue')
		control.sleep()
		pontos[i].hilight('red')





	

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


# Cria uma função para comparação angular ao redor do ponto p
def criaCompara(p):
	def menor(a, b):
		if( (p.y == a.y) and (p.y == b.y) ):
			if( (p.x < a.x) != (p.x < b.x) ):
				if(p.x < a.x): return 1
				else: return -1 #??
			else: #Ve pela distancia (???)
				a = dist2(a,p); db = dist2(b,p);
				if( da < db ): return 1
				elif( da > db): return -1
				else: return 0
		if( ((p.x <= a.y) == (p.y <= b.y))): #Estão no mesmo hemisfério
			if( left(p,a,b) ): return -1
			elif( collinear(a, b, p) ):
				da = dist2(a,p); db = dist2(b,p);
				if( da < db ): return 1
				elif( da > db): return -1
				else: return 0
			else: return 1 # b esta a direita de p->a
		else: #a e b estão em lados diferentes da bola
			if( a.y < p.y ): return 1;
			else: return -1
	return menor


	
