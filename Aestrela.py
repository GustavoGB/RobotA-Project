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

# A*
# recebe um objetivo e um inicio, ambos do tipo Node, uma matriz de 1 e 0s como mapa
def aStar(objetivo, mapa, start): 
	node = start
	node.tamanho = 0 
	borda = [node] #lista onde vao estar as posicoes da fronteira, ordenadas pelo custo (com a heuristica)
	explorado = [] #lista onde vao ficar as posicoes ja exploradas (e com seus 'filhos' na borda)

	while (borda): #roda enquanto ha um elemento na borda
		#print(borda)
		#print("")
		node = borda.pop(0) # pega a posicao de menor custo

		if (node.col == objetivo.col) and (node.lin == objetivo.lin): #acaba a funcao se a posicao eh o objetivo
			return node, borda, explorado

		explorado.append(node)
		filhos = pegaFilhos(node, mapa) #uma lista de posicoes do tipo Node, que fazem fronteira com essa (filhos)

		for filho in filhos:

			custoFilho = node.tamanho + filho.tamanho + hLR(filho, objetivo) #custo do filho = tamanho do caminho ate la + custo dessa posicao + heuristica euclidiana(distancia desse filho ao objetivo)
			filho.custo = custoFilho
			filho.tamanho = node.tamanho + filho.tamanho #camilho ate esse filho

			if filho not in borda and filho not in explorado: 
				#borda.append(filho)
				borda = insere(borda, filho) # insere o filho em sua posicao correta usando uma busca binaria
			else: 
				#se o filho ja esta na borda ou ja foi explorado

				imaior = binarySearch(borda, custoFilho)
				for i in range(imaior, len(borda)): #percorre a borda, se ha um caminho la que passa por esse filho, porem com custo maior, substitui por esse novo
					
					if borda[i].custo>custoFilho and borda[i].col == filho.col and borda[i].lin == filho.lin:
						borda.pop(i)
						#borda.append(filho)
						borda = insere(borda, filho) # insere o filho em sua posicao correta usando uma busca binaria

			borda = sorted(borda, key=lambda lin:lin.custo)

				

obj = Node(lin=1,col=10)
start = Node(lin=0, col=0)

result, bleh, blah = aStar(obj, m, start)

imprimeCaminhoBonito(start, m, obj)
imprimeCaminhoBonito(result, m, obj)

