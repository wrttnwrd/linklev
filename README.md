# linklev
Quick-and-dirty matching of broken links to working links using Levenshtein distance. I built it to help with a site migration.

USAGE: linklev.py [bad links filename] [site links filename] [output filename] [precision]

bad links: Any list of broken links
site links: List of all URLs on site
output file = results
precision: Maximum edit distance

Currently stores the top 5 matches for each link.

This tool works best if you have similar URLs. If you've completely rewritten URL structure,
