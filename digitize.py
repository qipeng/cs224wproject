from datetime import datetime
import calendar
from time import time

keyid = 0

def normalizeName(link):
    link = link.replace(" ", "_");
    link = link.capitalize();
    return link

def getKey(vmap, vkey):
    global keyid
    try:
        return vmap[vkey]
    except KeyError:
        keyid += 1
        vmap[vkey] = keyid
        fout.write(str(keyid)+"\t"+vkey+"\n")
        return keyid

def parseTime(strTime):
    t = datetime.strptime(strTime, "%Y-%m-%dT%H:%M:%SZ")
    return calendar.timegm(t.utctimetuple())

directory = "/Users/magician/Downloads/"

filename = directory + "title50000"
vocab = {}

currline = 0
fout = open(directory + "timed_edgelist.wiki", "w")
fout2 = open(directory + "vocab.wiki", "w")
t0 = time();

with open(filename) as f:
    for line in f:
        currline = currline + 1
        if currline % 1000 == 0:
            print "[INFO] Processing line", currline

        if (line.startswith("titl ")):
            currfilename = line[5:-1]
            print "[INFO] Processing file:", currfilename
            currfilekey = getKey(vocab, normalizeName(currfilename))
            fout.write("S " + str(currfilekey) + "\n")
            print "[INFO] Elapsed Time:", time()-t0
        elif (line.startswith("time ")):
            currtime = line[5:-1]
            timestamp = parseTime(currtime)
            fout.write("T " + str(timestamp) + "\n")
        elif (line.startswith("link ")):
            currlinks = line[5:-1]
            currlinks = currlinks.split('\t')
            fout.write("D ")
            for link in currlinks:
                if (link == ""): continue
                key = getKey(vocab, normalizeName(link))
                fout.write(str(key) + " ")
            fout.write("\n")

fout.close()
fout2.close()