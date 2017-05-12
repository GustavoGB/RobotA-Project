from coisasPraAestrela import *

mapa = """
0 0 0 0 0 0 1 0 0 0 0
1 1 1 0 0 0 1 0 0 1 0
0 0 0 1 1 1 1 0 0 1 0
0 1 1 1 0 0 1 1 0 1 0
0 0 0 0 1 0 0 0 0 1 0
"""

mapa = mapa.strip()

m = [linha.split(" ") for linha in mapa.split("\n")]



def aStar(objetivo, mapa): #recebe um objetivo do tipo Node
	node = Node(lin=0,col=0)
	node.custo = hLR(node, objetivo)
	borda = [node] # la em baixo vai ter um borda = sorted(borda, key = lambda lin:lin.custo)
	explorado = []
	while (borda):
		#print(explorado)
		node = borda.pop(0)
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
				borda.append(filho)
			else:
				for e in borda:
					if e.col == filho.col and e.lin == filho.lin and e.custo>custoFilho:
						borda.remove(e)
						borda.append(filho)

			borda = sorted(borda, key=lambda lin:lin.custo)

				

obj = Node(lin=1,col=10)


imprimeCaminhoBonito(aStar(obj, m), m)
