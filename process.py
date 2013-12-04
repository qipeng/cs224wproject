import snap
import os
import sys

def write(v):
    sys.stdout.write(v)
    sys.stdout.flush()

filenames = []
y = 1; m = 2;
while (y < 6) or ((y == 6) and (m <= 8)):
    # filenames.append("ssredirect/ssredirect%02d%02d01.txt" % (y, m))
    filenames.append("snapshot/snapshot%02d%02d01.txt" % (y, m))
    m += 1
    if (m > 12):
        m = 1; y += 1

print "Filename\t#Nodes\t#Edges\tDiameter\t#LargestSCC\t#LargestWCC\tMaxInDeg\tMaxOutDeg"

for filename in filenames:
    if (not os.path.exists(filename)): continue
    G = snap.LoadEdgeList(snap.PNGraph, filename, 0, 1)
    if (G == None): G = snap.TNGraph.New();

    G.AddNode(0)

    # nodefilename = filename[0:-4]+"n"+filename[-4:]
    # with open(nodefilename) as nodefile:
    #     for line in nodefile:
    #         nid = int(line)
    #         if (not G.IsNode(nid)): G.AddNode(nid)

    write(filename + "\t")
    write(str(G.GetNodes()) + "\t")
    write(str(G.GetEdges()) + "\t")
    write(str(snap.GetBfsFullDiam(G, 20)))
    write("\t" + str(snap.GetMxScc(G).GetNodes() * 1.0 / G.GetNodes()))
    write("\t" + str(snap.GetMxWccSz(G)))
    write("\t" + str(G.GetNI(snap.GetMxInDegNId(G)).GetInDeg()))
    write("\t" + str(G.GetNI(snap.GetMxOutDegNId(G)).GetOutDeg()))
    write("\n")