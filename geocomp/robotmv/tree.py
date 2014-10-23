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
			#maior
		else:
			return resp



class Tree:
	def __init__(self):
		self.root = Leave(None)

	def insert(self, x):
		self.root = self.root.insert(x)

	def getMin(self):
		return self.root.getMin()


