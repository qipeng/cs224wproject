import snap
import random

def addEdgePageRank(G, src, pageRank=None):
    if (not pageRank):
        pageRank = snap.TIntFltH()
        snap.GetPageRank(G, pageRank)

    sample = random.random()
    accumulate = 0

    for n in G.Nodes():
        key = n.GetId()
        if not pageRank.IsKey(key): 
            # This should never happen!
            raise Exception('PageRank Error', 'PageRank accumulation out of range') 
        value = pageRank.GetDat(key)
        accumulate += value
        if (accumulate > sample):
            G.AddEdge(src, key)
            return pageRank

if __name__ == "__main__":
    G = snap.TNGraph.New()
    G.AddNode(0)

    N = 30000
    for i in range(1,N):
        G.AddNode(i)
        # if i < 1000 or i % 1000 == 0:
        #     pageRank = addEdgePageRank(G, i)
        #     pageRank = addEdgePageRank(G, i)
        # else:
        #     addEdgePageRank(G, i, pageRank)
        #     addEdgePageRank(G, i, pageRank)

        addEdgePageRank(G, i)
        addEdgePageRank(G, i)

        if (i%1000==0): print i

    snap.PlotInDegDistr(G, "example", "In-degree Distribution")