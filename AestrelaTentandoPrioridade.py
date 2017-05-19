from coisasPraAestrela import *

import queue as Q


mapa = """
0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 1 0 0 0
"""

mapa = mapa.strip()

m = [[int(e) for e in linha.split(" ")] for linha in mapa.split("\n")]



def aStar(objetivo, mapa, start): #recebe um objetivo do tipo Node
	node = start
	node.custo = hLR(node, objetivo)
	bordaq = Q.PriorityQueue()
	bordaq.put(node, node.custo)
	borda = [node]
	explorado = []
	while (borda):
		#print(explorado)
		node = bordaq.get()
		if (node.col == objetivo.col) and (node.lin == objetivo.lin):
			return node
		explorado.append(node)
		filhos = pegaFilhos(node, mapa)
		#print(filhos)
		for filho in filhos:
			#print("temfilhos")
			custoFilho = node.custo + filho.custo + hLR(filho, objetivo)
			filho.custo = custoFilho
			if filho not in borda and filho not in explorado:
				#print("appendou")
				bordaq.put(filho, filho.custo)
				borda.append(filho)
			else:
				for e in borda:
					if e.col == filho.col and e.lin == filho.lin and e.custo>custoFilho:
						bordaq.get(e)
						bordaq.put(filho, filho.custo)
						borda.remove(e)
						borda.append(filho)

			

				

obj = Node(lin=1,col=10)
start = Node(lin=0, col=0)

imprimeCaminhoBonito(aStar(obj, m, start), m)
