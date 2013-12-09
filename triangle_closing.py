from snap import *
import random,collections
import graph_derivative


def create_test_graph(num_nodes,num_edges,test_edge_prob):
	G2 = GenRndGnm(PNGraph,num_nodes,num_edges)
	E = []
	for edge in G2.Edges():
		if random.random() > 1- test_edge_prob:
			E.append((edge.GetSrcNId(),edge.GetDstNId()))
	print 'total' ,len(E), 'edges'
	return G2, E

# suppose we have done subtraction between two close snapshots
# G2 is the later snapshot
# E is the set of edges that are in G2 but not in G1
# This function evaluates the triangle closing model on G2 and E
def count_triangles(G2,E):
	dist_counter = collections.Counter()
	tri_type_counter = collections.Counter()
	# Do for every new edge
	for src,dst in E:
		# check reciprocal
		if G2.GetNI(src).IsInNId(dst):
			dist_counter[1] += 1
			continue
		# check triangles
		type_name = collections.Counter()
		# check outgoing 
		for outNode in G2.GetNI(src).GetOutEdges():
			if G2.GetNI(outNode).IsOutNId(dst):
				type_name["1"] += 1
			if G2.GetNI(outNode).IsInNId(dst):
				type_name["2"] += 1

		# check incoming 
		for inNode in G2.GetNI(src).GetInEdges():
			if G2.GetNI(inNode).IsOutNId(dst):
				type_name["3"] += 1
			if G2.GetNI(inNode).IsInNId(dst):
				type_name["4"] += 1
		if type_name.keys():
			tri_type_counter["+".join(sorted(type_name.keys()))] += 1
			dist_counter[2] += 1
			continue
		dist_counter['3+'] += 1

	seperated_counter = collections.Counter()
	seperated_counter[1] = tri_type_counter['1'] + tri_type_counter['1+2'] + tri_type_counter['1+3'] + tri_type_counter['1+4'] + tri_type_counter['1+2+3'] + tri_type_counter['1+2+4'] + tri_type_counter['1+3+4'] + tri_type_counter['1+2+3+4']
	seperated_counter[2] = tri_type_counter['2'] + tri_type_counter['1+2'] + tri_type_counter['2+3'] + tri_type_counter['2+4'] + tri_type_counter['1+2+3'] + tri_type_counter['1+2+4'] + tri_type_counter['2+3+4'] + tri_type_counter['1+2+3+4']
	seperated_counter[3] = tri_type_counter['3'] + tri_type_counter['1+3'] + tri_type_counter['2+3'] + tri_type_counter['3+4'] + tri_type_counter['1+2+3'] + tri_type_counter['1+3+4'] + tri_type_counter['2+3+4'] + tri_type_counter['1+2+3+4']
	seperated_counter[4] = tri_type_counter['4'] + tri_type_counter['1+4'] + tri_type_counter['2+4'] + tri_type_counter['3+4'] + tri_type_counter['1+2+4'] + tri_type_counter['1+3+4'] + tri_type_counter['2+3+4'] + tri_type_counter['1+2+3+4']

	print 'distances: ', dist_counter
	print 'triangle types: ', tri_type_counter
	print 'seperated triangle types: ', seperated_counter
	return dist_counter,tri_type_counter,seperated_counter

if __name__ == "__main__":
	# G,E = create_test_graph(100,1000,0.05)
	G1 = LoadEdgeList(PNGraph,'../wiki_week/ssredirect050704.txt')
	G2 = LoadEdgeList(PNGraph,'../wiki_week/ssredirect050707.txt')
	E = graph_derivative.derivative(G1,G2)
	count_triangles(G2,E)
