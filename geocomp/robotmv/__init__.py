# -*- coding: utf-8 -*-
"""Algoritmos para o problema do Plano de Locomoção de Robôs,:

~Falta definição do problema~

Algoritmos disponíveis:
- Grafo de visibilidade
"""

import visgraph

# cada entrada deve ter:
#  [ 'nome-do-modulo', 'nome-da-funcao', 'nome do algoritmo' ]
children = ( 
	( 'visgraph', 'visGraphAlg', 'Grafo de visibilidade' ),
	
)

#children = algorithms

#__all__ = [ 'graham', 'gift' ]
__all__ = map (lambda a: a[0], children)
