#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Árvore binário da busca. Suponho que as keys são
	segmentos
"""

from geocomp.common.segment import Segment
from geocomp.common.prim import *
from minhasPrim import *




class Folha:
	def __init__(self, key):
		self.key = key


		#Cheio das pogz
	def delete(self,x,carry):
		s = self.key
		#if(carry is None): return self #Não achou(??)
		if(s is None): return Folha(None) #wtf
		if(s.init == x.init and s.to == x.to): #Deveria sempre ser True
			print "Ok"
		else:
			print "Vish~"
		if(carry is None): return Folha(None)
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

	def procuraInter(self, seg):
		x = self.key
		if(x is not None and intersecta(seg,x)): return x
		else: return None

	def __repr__(self, level=0):
		x = self.key
		if(self.key is None): x = "NADA"
		ret = "\t"*level+repr(self.key)+"\n"
		return ret


class InCel:
	def __init__(self, key, left, right):
		self.r = right
		self.l = left
		self.key = key



	def delete(self, x, carry): #############################################
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
		if(right(s.init, s.to, x.init)):
			self.l = self.l.insert(x)
		elif(collinear(s.init, s.to, x.init)):
			if(right(s.init, s.to, x.init)):
				self.l = self.l.insert(x)
			else:
				self.r = self.r.insert(x)
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

	def procuraInter(self, seg):
		x = self.key
		if(intersecta(seg,x)): return x
		else:
			if(right(x.init, x.to, seg.init)):
				return self.l.procuraInter(seg)
			else:
				return self.r.procuraInter(seg)

	def __repr__(self, level=0):
		ret = "\t"*level+repr(self.key)+"\n"
		ret += self.l.__repr__(level+1)
		ret += self.r.__repr__(level+1)
		return ret




class Tree:
	def __init__(self):
		self.root = Folha(None)

	def insert(self, x):
		print "Entrando2: ", x
		x.hilight('yellow')
		self.root = self.root.insert(x)
		#print self

	def getMin(self):
		return self.root.getMin()

	def delete(self, x):
		print "Tentando deletar:", x
		x.plot('red')
		self.root = self.root.delete(x,None)
		#print self

	def procuraInter(self, seg):
		self.root.procuraInter(seg);

	def __repr__(self):
	 	return self.root.__repr__()



