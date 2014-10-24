#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Árvore binário da busca. Suponho que as keys são
	segmentos
"""

from geocomp.common.segment import Segment
from geocomp.common.prim import *




class Folha:
	def __init__(self, key):
		self.key = key



	def delete(self,x,carry):
		s = self.key
		if(s.init == x.init and s.to == x.to): #Deveria sempre ser True
			print "Ok"
		else:
			print "Vish~"
		return carry


	def insert(self,x):
		s = self.key
		if(s is None): 
			self.key = x
			return self
		else:
			if(right_on(s.init, s.to, x.init)):
				return InCel(x, Folha(x), Folha(s))
			else:
				return InCel(s, Folha(s), Folha(x))

	def getMin(self):
		return self.key


class InCel:
	def __init__(self, key, left, right):
		self.r = right
		self.l = left
		self.key = key



	def delete(self, x, carry):
		s = self.key
		if(s.init == x.init and s.to == x.to): #Achou o nó interno com chave igual
			carry = self.r
			self.l = self.l.delete(x, carry)
			return self.l #?
		if(right_on(s.init, s.to, x.to)): # Compara com o fim de X.... pensar melhor depois
			self.l = self.l.delete(x, carry)
		else:
			self.r = self.r.delete(x, carry)
		return self


	# x é um segmento novo
	def insert(self, x):
		s = self.key;
		if(right_on(s.init, s.to, x.init)):
			self.l = self.l.insert(x)
		else:
			self.r = self.r.insert(x)
		return self

	def getMin(self):
		resp = self.l.getMin()
		if(resp is None): 
			return self.key 
			#Ou self.r.getMin().
			#Provavelmente tem o mesmo efeito, mas com possivelmente
			#maior tempo de execução
		else:
			return resp



class Tree:
	def __init__(self):
		self.root = Folha(None)

	def insert(self, x):
		self.root = self.root.insert(x)

	def getMin(self):
		return self.root.getMin()

	def delete(self, x):
		self.root = self.root.delete(x,None)


