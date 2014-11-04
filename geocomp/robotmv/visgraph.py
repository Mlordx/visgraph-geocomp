#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Algoritmo de Grafo de Visibilidade"""


from geocomp.common.polygon import Polygon
from geocomp.common.point import Point
from geocomp.common import control
from geocomp.common.segment import Segment
from geocomp.common.guiprim import *
from geocomp import config
from tree import Tree
from minhasPrim import *


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

	#poligs.pop(0) #Tira o robo da lista de polígonos
	pontos = []
	for i in range(len(poligs)):
		poligs[i] = Polygon(poligs[i])
		poligs[i].hilight()
		pontos.extend(poligs[i].to_list())


	probo.prev = probo.next = probo

	print poligs
	#print compara(pontos[3], pontos[1])
	compara = criaCompara(probo)
	pontos.sort(cmp = compara, reverse = True)

	

#	for i in range (len(pontos)):
#		pontos[i].hilight('yellow')
#		probo.lineto(pontos[i], 'blue');
#		control.sleep()
#		probo.remove_lineto(pontos[i])
#		pontos[i].hilight('red')

	pi = pontos[len(pontos)-5]
	pontos.append(probo)


	compara = criaCompara(pi)
	pontos.sort(cmp = compara, reverse = True)
	for i in range (len(pontos)):
		pontos[i].hilight('yellow')
		pi.lineto(pontos[i], 'blue');
		control.sleep()
		pi.remove_lineto(pontos[i])
		pontos[i].hilight('red')
	print "PRE-PA-RA"
	print compara(pontos[len(pontos)-2],pontos[len(pontos)-1])
	print "HUEEEEEEEE"

	
#	W = verticesVisiveis(pi, poligs)
#	for i in range(len(W)):
#		print pi, W[i]
#		pi.lineto(W[i], 'blue')
#	print "oie"

	for pi in pontos:
		W = verticesVisiveis(pi, poligs)
		for i in range(len(W)):
			pi.lineto(W[i], 'blue')
	#Vamos tentar ver os vértices visiveis a partir do robo

	#definir os segmentos que intersectam px->inf+
#	tree1 = Tree()
#	for i in range(len(poligs)):
#		listaPs = poligs[i].to_list()
#		n = len(listaPs)
#		for j in range(n):
#			a = listaPs[j]; b = listaPs[(j+1)%n];
#			if(passaEixoX(a, b, probo)):
#				if(compara(a, b) == 1): tree1.insert(Segment(a,b));
#				else: tree1.insert(Segment(b,a));
#				a.lineto(b, 'yellow')
				





	

	#poligTeste1.hilight();

"""
	# Desenho o primeiro poligono...seria bom se parar isso em outra
	# função depois
	for i in range(len(poligs[1])-1):
		poligs[1][i].lineto(poligs[1][i+1])
	poligs[1][len(poligs[1])-1].lineto(poligs[1][0])

"""


"""

	Testa se o segmento a-b intersecta o segmento
	p.x-inf+

"""

def passaEixoX(a,b,p):
	#Acerta quem é a e b para acertarmos a orientação
	if(a.y < b.y):
		aux = a; a = b; b = aux;
	elif(a.y == b.y):
		if(a.x > b.x):
			aux = a; a = b; b = aux;

	#print "Analisando (%d, %d)->(%d, %d) para (%d, %d)"% (a.x, a.y, b.x, b.y, p.x, p.y)

	if(a.y > p.y and b.y <= p.y and right(a,b,p)):
		return True #cruza o eixo p.x-inf+
	else: return False






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
			print "Caso degenerado"
			if( (p.x < a.x) != (p.x < b.x) ):
				if(p.x < a.x): return 1
				else: return -1 #??
			else: #Ve pela distancia (???)
				da = dist2(a,p); db = dist2(b,p);
				if( da < db ): return 1
				elif( da > db): return -1
				else: return 0
		if( ((p.y >= a.y) == (p.y >= b.y))): #Estão no mesmo hemisfério
			print "Caso 1"
			if( left(p,a,b) ): return -1
			elif( collinear(a, b, p) ):
				da = dist2(a,p); db = dist2(b,p);
				if( da < db ): return 1
				elif( da > db): return -1
				else: return 0
			else: return 1 # b esta a direita de p->a
		else: #a e b estão em lados diferentes da bola
			print "Caso2"
			if( a.y <= p.y ): return 1;
			else: return -1
	return menor


"""
A função recebe uma arvore T, um vetor de pontos ordenados
S, ponto de referencia p, e o índice i do ponto que queremos analisar.

Suponho que o teste ja foi feito para S[0..i-1]


"""

def visivel(T, S, p, i):
	print "TESTANDO VISIBILIDADE"
	a = S[i]
	a.visivel = False #Até que se prove o contrário

	if( a is p):
		a.visivel = True
		return a.visivel

	#Testa se a reta p->s[i] passa por dentro do polígono
	# de p.
	if(p.prev != p): #p está em algum polígono
		if(noCone(p.prev,p,p.next,a) ):
			a.visivel = False
			print "Falhou no cone"
			return a.visivel


	if(i == 0 or not collinear(p, S[i-1], a)):
		segMin = T.getMin()
		if(segMin is None): 
			a.visivel = True
			print "Seg min é null"
			return a.visivel
		print "Testando intersec com min"
		segMin.hilight('blue')
		print segMin
		control.sleep()
		segMin.hilight('yellow')
		a.visivel = not intersectaProp(segMin, Segment(p,a)) 
	elif( not S[i-1].visivel ):
		print "Anterior não é visível"
		a.visivel = False
	else: 
		if(S[i-1].prev != S[i-1]): #S[i-1] esta em um polígono
			if(noCone(S[i-1].prev, S[i-1], S[i-1].next, a)): #############################
				a.visivel = False
				print "Falhou no cone 2"
				return a.visivel

		seg2 = T.procuraInter(Segment(S[i-1],a))
		print "Testando o segmento do meio"
		a.visivel = (seg2 is None)
	return a.visivel


def verticesVisiveis(p, poligs):
	pontos = []
	for i in range(len(poligs)):
		pontos.extend(poligs[i].to_list())
	compara = criaCompara(p)

	#Intersecta p.x -> inf+
	T = Tree();

	pontos.sort(cmp = compara, reverse = True)
	for i in range(len(poligs)):
		listaPs = poligs[i].to_list()
		n = len(listaPs)
		for j in range(n):
			a = listaPs[j]; b = listaPs[(j+1)%n];
			if(passaEixoX(a, b, p)):
				if(left_on(p,b,a)): T.insert(Segment(a,b));
				else: T.insert(Segment(b,a));

	#Começa o role
	W = []; 
	for i in range(len(pontos)):
		a = pontos[i]
		p.lineto(a, 'white')
		a.hilight('blue')
		control.sleep()
		a.unhilight()
		if(visivel(T, pontos, p, i)): 
			print "VISIVEL"
			if(a is not p):
				W.append(a)
				p.lineto(a, 'blue')
		else: p.remove_lineto(a)
		b = a.prev; c = a.next;
		
		print "Vish ", i, pontos[i]
		if(left_on(p,a,b)): T.delete(Segment(b,a))
		else: T.insert(Segment(a,b))
		if(left_on(p,a,c)): T.delete(Segment(c,a))
		else: T.insert(Segment(a,c))
	#	print "Oie~", i

	return W

				
			




	
