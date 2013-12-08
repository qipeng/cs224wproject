from snap import *

G1 = LoadEdgeList(PNGraph,'../snapshot030701.txt')
G2 = LoadEdgeList(PNGraph,'../snapshot030801.txt')

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
