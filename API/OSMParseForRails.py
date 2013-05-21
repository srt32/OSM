# this files reads in the output file from OSMAPICall.py
# this file outputs a CSV that is compatible to be rake loaded into RAILS app

# NEEDS UPDATE TO PIPE OUTPUT TO 'OutputFile'

def OSMParseForRails(inputFile,OutputFile):
	import xml.etree.ElementTree as ET
	import sys

	print "STARTING OSMParseForRails"
	
	# pipe output to file
	saveout = sys.stdout  
	sys.stdout = open(OutputFile, 'w')
	
	inputFile = open(inputFile)
	delta = 0.0001090911074 # = 40 equator-feet
	# export data from here, http://www.openstreetmap.org/

	tree = ET.parse(inputFile)
	root = tree.getroot()

	# for import to RAILS:  :gmaps, :latitude, :longitude, :name

	print "gmaps, latitude, longitude, name"

	for node in root.findall('node'):
		nid = node.get('id')
		lat = node.get('lat')
		lon = node.get('lon')
		for tag in node.findall('tag'):
			k = tag.get('k')  # needs to find the tag with k="name"
			v = tag.get('v')
			if k == "name":
				Ax = float(lat) - delta
				Ay = float(lon) + delta
				Bx = float(lat) + delta
				By = float(lon) + delta
				Cx = float(lat) + delta
				Cy = float(lon) - delta
				Dx = float(lat) - delta
				Dy = float(lon) - delta
				print "t" + ",",
				print Ax, 
				print ",",
				print Ay, 
				print ",",
				print v
				print "t" + ",",
				print Bx, 
				print ",",
				print By, 
				print ",",
				print v
				print "t" + ",",
				print Cx, 
				print ",",
				print Cy, 
				print ",",
				print v
				print "t" + ",",
				print Dx, 
				print ",",
				print Dy, 
				print ",",
				print v

	# set stdout back to default
	sys.stdout = saveout 

	print "COMPLETED OSMParseForRails"

# if __name__ == '__main__':
# 	import sys
# 	OSMParseForRails(sys.argv[1])