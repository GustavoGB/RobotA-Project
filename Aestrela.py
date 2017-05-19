from coisasPraAestrela import *

mapa = """
0 0 0 0 0 0 1 0 0 0 0
1 1 1 0 0 0 1 0 0 1 0
0 0 0 1 1 1 1 0 0 1 0
0 1 1 1 0 0 1 1 0 1 0
0 0 0 0 1 0 0 0 0 1 0
"""

mapa = mapa.strip()

m = [[int(e) for e in linha.split(" ")] for linha in mapa.split("\n")]



def aStar(objetivo, mapa, start): #recebe um objetivo do tipo Node
	node = start
	node.custo = hLR(node, objetivo)
	borda = [node] # la em baixo vai ter um borda = sorted(borda, key = lambda lin:lin.custo)
	explorado = []
	while (borda):
		#print(explorado)
		node = borda.pop(0)
		if (node.col == objetivo.col) and (node.lin == objetivo.lin):
			return node, borda, explorado
		explorado.append(node)
		filhos = pegaFilhos(node, mapa)
		#print(filhos)
		for filho in filhos:
			#print("temfilhos")
			custoFilho = node.custo + filho.custo + hLR(filho, objetivo)
			filho.custo = custoFilho
			if filho not in borda and filho not in explorado:
				#print("appendou")
				#borda.append(filho)
				borda = insere(borda, filho)
			else:
				imaior = binarySearch(borda, custoFilho)
				for i in range(imaior, len(borda)):
					if borda[i].custo>custoFilho and borda[i].col == filho.col and borda[i].lin == filho.lin:
						borda.pop(i)
						#borda.append(filho)
						borda = insere(borda, filho)

			#borda = sorted(borda, key=lambda lin:lin.custo)

				

obj = Node(lin=1,col=10)
start = Node(lin=0, col=0)

#imprimeCaminhoBonito(aStar(obj, m, start), m)

