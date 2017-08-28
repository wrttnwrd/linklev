''' Takes badlinks file, compares to every link in a site links file, outputs result to an output file.
Link files should have line-break-separated list of links. Output is TSV '''
import sys
import Levenshtein as lev

if len(sys.argv) == 5:
    badlinksfile = sys.argv[1]
    sitelinksfile = sys.argv[2]
    outputfile = sys.argv[3]
    precision = int(sys.argv[4])
    badlinks = open(badlinksfile,'r').readlines()
    badlinks.sort()
    sitelinks = open(sitelinksfile,'r').readlines()
    resultlist = []

    outfile = open(outputfile,'w')
    outfile.close()
    outfile = open(outputfile,'a')
    for b in badlinks:
        b = b.strip()
        resultlist = []
        for s in sitelinks:
            s = s.strip()
            dislist = []
            dis = lev.distance(b,s)
            if dis <= precision:
                dislist.append(b)
                dislist.append(s)
                dislist.append(dis)
                resultlist.append(dislist)
            else:
                r = sorted(resultlist, key=lambda x: x[2])
                for rs in r[:5]:
                    thisline = ('\t'.join(map(str,rs)))
                    thisline = thisline + "\n"
                    outfile.write(thisline)
                break


    outfile.close()
    sys.exit()

    r = sorted(resultlist, key=lambda x: x[2])


else:
    print "USAGE: linklev.py [bad links filename] [site links filename] [output filename] [precision] (precision = max edit distance)"
