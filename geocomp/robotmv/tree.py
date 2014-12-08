#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Árvore binário da busca. Suponho que as keys são
	segmentos
"""

from geocomp.common.segment import Segment
from geocomp.common.prim import *
from minhasPrim import *

"""
DEFINES DE CONTROLE
"""

PINTA = False;


#Deleão antiga de folha
"""
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
"""


class Folha:
	def __init__(self, key):
		self.key = key
		self.red = False



	def delete(self,x):
		s = self.key
		#if(carry is None): return self #Não achou(??)
		if(s is None): 
			print "FOLHA NULL?? QUE. Estava tentando deletar: ", x
			return Folha(None) #wtf
		if(s.init == x.init and s.to == x.to): #Deveria sempre ser True
			print "Ok"
			return Folha(None);
		else:
			print "Deleção falhou, chegou em:", self.key
			return self



	def insert(self,x):		
		s = self.key
		if(s is None): 
			self.key = x
			return self
		else:
			if(right(s.init, s.to, x.init)):
				return InCel(x, Folha(x), Folha(s), True)
			elif(collinear(s.init, s.to, x.init)):
				if(right(s.init, s.to, x.to)):
					return InCel(x, Folha(x), Folha(s), True)
				else:
					return InCel(s, Folha(s), Folha(x), True)
					
			else:
				return InCel(s, Folha(s), Folha(x), True)

	#Deleta a folha mais a direita. E retorna o irmão esquerdo dessa folha
	def delMax(self):
		return Folha(None);
		

	def getMin(self):
		return self.key

	def getMax(self):
		return self.key

	def procuraInter(self, seg):
		x = self.key
		if(x is not None and intersecta(seg,x)): return x
		else: return None

	def __repr__(self, level=0):
		x = self.key
		if(self.key is None): x = "NADA"
		ret = "\t"*level+repr(x)+"\n"
		return ret


	def getProx(self, p):
		return self.key


"""
	#Delete antigo da célula
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
"""


class InCel:
	def __init__(self, key, left, right, red):
		self.r = right
		self.l = left
		self.key = key
		self.red = red



	def delete(self,x):
		s = self.key
		if(s.init == x.init and s.to == x.to): #Achou o nó interno com chave igual
			self.l = self.l.delMax()
			if(isinstance(self.l,Folha) and self.l.key is None): #self.l era folha
				return self.r
			self.key = self.l.getMax()
			return self
		if(right(s.init, s.to, x.to)): # Compara com o fim de X.... pensar melhor depois
			print "TUDO A DIREITA NA DELEÇÃO"
			self.l = self.l.delete(x)
			if(isinstance(self.l, Folha) and self.l.key is None): 
				print "ERRO 1 NO DELETE!!!!!!"
				return self.r; #???
		elif(collinear(s.init, s.to, x.to)):
			print "COLINEAR NA DELEÇÃO"
			if(right(s.init, s.to, x.init)):
				self.l = self.l.delete(x)
				if(isinstance(self.l, Folha) and self.l.key is None): 
					print "ERRO 1 NO DELETE!!!!!!"
					return self.r; #???
			else:
				print "MAOE(????)"
				self.r = self.r.delete(x)
				if(self.r is None): #self.r era a folha;
					return self.l;				
		else:
			print "FAIOU EM TUDO NA DELEÇÃO"
			self.r = self.r.delete(x)
			if(isinstance(self.r,Folha) and self.r.key is None): #self.r era a folha;
				return self.l;
		return self


	def delMax(self):
		self.r = self.r.delMax();
		if(isinstance(self.r, Folha) and self.r.key is None): #self.r era folha
			return self.l;
		return self;

	def getMax(self):
		return self.r.getMax();

	# x é um segmento novo
	def insert(self, x):
		s = self.key;
		if(right(s.init, s.to, x.init)):
			self.l = self.l.insert(x)
		elif(collinear(s.init, s.to, x.init)):
			if(right(s.init, s.to, x.to)): 

				self.l = self.l.insert(x)
			else:
				self.r = self.r.insert(x)
		else:
			self.r = self.r.insert(x)


		# Balanceamento da rubro-negra

		if(self.r.red and not self.l.red): self = self.rotateL()
		if(self.l.red and self.l.l.red): self = self.rotateR()
		if(self.l.red and self.r.red): self.colorFlip()




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

	def getProx(self, p):
		x = self.key
		if(right(x.init, x.to,p)):
			return self.l.getProx(p)
		else:
			return self.r.getProx(p)

	def rotateL(self):
		x = self.r
		self.r = x.l
		x.l = self
		x.red = self.red
		self.red = True
		return x

	def rotateR(self):
		x = self.l
		self.l = x.r
		x.r = h
		x.red = h.red
		h.red = True
		return x

	def colorFlip(self):
		self.red = True
		self.r.red = False
		self.l.red = False

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
		if(PINTA): x.hilight('yellow')
		self.root = self.root.insert(x)
		self.root.red = False
		#print self

	def getMin(self):
		return self.root.getMin()

	def delete(self, x):
		print "Tentando deletar:", x
		idH =  x.plot('red')
		self.root = self.root.delete(x)
		control.sleep()
		x.hide(idH)
		#self.root = self.root.delete(x,None)
		#print self

	def getProx(self,p):
		return self.root.getProx(p)

	def procuraInter(self, seg):
		self.root.procuraInter(seg);

	def __repr__(self):
	 	return self.root.__repr__()



