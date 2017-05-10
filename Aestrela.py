from coisasPraAestrela import *

mapa = """
0 0 0 0 0 0 1
1 1 1 0 0 0 1
0 0 0 1 1 1 0
"""

mapa = mapa.strip()

m = [linha.split(" ") for linha in mapa.split("\n")]

print(m)


def aStar(objetivo): #recebe um objetivo do tipo Node
	no = Node()
	borda = [no] # la em baixo vai ter um borda = sorted(borda, key = lambda x:x.custo)
	explorado = []
	while (borda):
		no = borda.pop([0])
		if (no.y == objetivo.y) and (no.x == objetivo.x):
			return no

	