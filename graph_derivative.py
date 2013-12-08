from snap import *

def derivative(G1,G2):
	print G1.GetNodes()
	print G1.GetEdges()
	print G2.GetNodes()
	print G2.GetEdges()

	E = []
	for edge in G2.Edges():
		if not G1.IsEdge(edge.GetSrcNId(),edge.GetDstNId(),True):
			E.append((edge.GetSrcNId(),edge.GetDstNId()))

	print 'different edges:', len(E)
	print 'percentage:', float(len(E))/G2.GetEdges()

	return E

if __name__ == "__main__":
	G1 = LoadEdgeList(PNGraph,'../snapshot030701.txt')
	G2 = LoadEdgeList(PNGraph,'../snapshot030801.txt')
	derivative(G1,G2)