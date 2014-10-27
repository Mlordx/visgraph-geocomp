#!/usr/bin/env python
# -*- coding: utf-8 -*-


from geocomp.common.point import Point
from geocomp.common import control
from geocomp.common.segment import Segment
from geocomp.common.prim import *


def intersectaProp(seg1, seg2):
	a = seg1.init; b = seg1.to; c = seg2.init; d = seg2.to;
	if(collinear(a,b,c) or collinear(a,b,d) or collinear(c,d,a) or collinear(c,d,b)):
			return False
	else:
		return ( (left(a,b,c) ^ left(a,b,d)) and (left(c,d,a) ^ left(c,d,b)) )

def intersecta(seg1, seg2):
	if(intersectaProp(seg1,seg2)): return True
	a = seg1.init; b = seg1.to; c = seg2.init; d = seg2.to;
	return (entre(seg1, c) or entre(seg1, d) or entre(seg2, a) or entre(seg2, b))


def entre(seg1, c):
	a = seg1.init; b = seg1.to;
	if(not collinear(a,b,c)): return False
	if(a.x != b.x):
		return ((a.x <= c.x and c.x <= b.x) or (b.x <= c.x and c.x <= a.x))
	else:
		return ((a.y <= c.y and c.y <= b.y) or (b.y <= c.y and c.y <= a.y))

#Teste se o ponto d esta no cone definido por a->b->c

def noCone(a, b, c, d):
	if(left_on(a,b,c)): #convexo
		return (left(b,d,a) and left(d,b,c))
	else:
		return not (left_on(d,b,a) and left_on(b,d,c))

