# this script will take the school_DB dump and parse it to pull out the around_latitudes, name, id 
	# for the input school name -- Example = "University of Denver"
# this data is then passed to OSMAPICall.py

def OSMParse():
	import xml.etree.ElementTree as ET
	import sys
	intputFile = open(sys.argv[1])

	tree = ET.parse(intputFile)
	root = tree.getroot()

	print "University Name (IT IS NOT NECESSARILY THE CORRECT UNIVERSITY):",
	uni = 0
	for node in root.findall('node'):
		uni_id_raw = node.get('id')
		for tag in node.findall('tag'):
			k = tag.get('k')
			v = tag.get('v')
			if k == "amenity" and v == "university":
				uni = 1
			if k == "name" and uni == 1:
				uni_id = uni_id_raw
				print v
				uni = 0

	for node in root.findall('node'):
		nid = node.get('id')
		lat = node.get('lat')
		lon = node.get('lon')
		for tag in node.findall('tag'):
			k = tag.get('k')  # needs to find the tag with k="name"
			v = tag.get('v')
			if k == "name" and nid != uni_id:
				print lat + "," + lon + "," + v + ",",
				Ax = float(lat) - delta

if __name__ == '__main__':
	OSMParse()