from snap import *
from graph_derivative import *

if __name__ == "__main__":
    G1 = LoadEdgeList(PNGraph,'../code/ssredirect/ssredirect030701.txt')
    G2 = LoadEdgeList(PNGraph,'../code/ssredirect/ssredirect030801.txt')
    dE = derivative(G1,G2)

    pageRank = TIntFltH()
    GetPageRank(G2, pageRank)

    fid = open('pr_vs_deg_in.txt','w')

    for e in dE:
        fid.write(str(G2.GetNI(e[1]).GetInDeg())+" "+str(pageRank.GetDat(e[1]))+"\n")

    fid.close()

    fid = open('pr_vs_deg_out.txt','w')

    for e in dE:
        fid.write(str(G2.GetNI(e[0]).GetOutDeg())+" "+str(pageRank.GetDat(e[0]))+"\n")

    fid.close()

    fid = open('pr_vs_deg.txt','w')

    for e in dE:
        fid.write(str(G2.GetNI(e[1]).GetDeg())+" "+str(pageRank.GetDat(e[1]))+"\n")

    fid.close()

    fid = open('pr_vs_deg_all.txt','w')

    for n in G2.Nodes():
    	nid = n.GetId()
        fid.write(str(n.GetDeg())+" "+str(pageRank.GetDat(nid))+"\n")

    fid.close()
