def OSMDataParse(inputFile,OutputFileDB,schoolID):
	import xml.etree.ElementTree as ET
	import sys

	print "STARTING OSMDataParse"

	# for troubleshooting
	print inputFile


	# pipe output to file
	saveout = sys.stdout  
	sys.stdout = open(OutputFileDB, 'w')

	inputFile = open(inputFile)
	delta = 0.0001090911074 # = 40 equator-feet
	# export data from here, http://www.openstreetmap.org/

	tree = ET.parse(inputFile)
	root = tree.getroot()

	# print "University Name (IT IS NOT NECESSARILY THE CORRECT UNIVERSITY):",
	uni = 0
	uni_id = 0
	for node in root.findall('node'):
		uni_id_raw = node.get('id')
		for tag in node.findall('tag'):
			k = tag.get('k')
			v = tag.get('v')
			if k == "amenity" and v == "university":
				uni = 1
			if k == "name" and uni == 1:
				uni_id = uni_id_raw
				# print v
				uni = 0

	# print "Bounds:",
	# for bound in root.iter('bounds'):
	# 	print bound.attrib

	print "schoolID, lat, lon, name, around_latitudes" # headers

	for node in root.findall('node'):
		nid = node.get('id')
		lat = node.get('lat')
		lon = node.get('lon')
		for tag in node.findall('tag'):
			k = tag.get('k')  # needs to find the tag with k="name"
			v = tag.get('v')
			if k == "name" and nid != uni_id:
				print schoolID + "," + lat + "," + lon + "," + v + ",",
				Ax = float(lat) - delta
				Ay = float(lon) + delta
				Bx = float(lat) + delta
				By = float(lon) + delta
				Cx = float(lat) + delta
				Cy = float(lon) - delta
				Dx = float(lat) - delta
				Dy = float(lon) - delta
				around_latitudes = [[Ax, Ay], [Bx, By], [Cx, Cy], [Dx ,Dy]]
				print around_latitudes

	# set stdout back to default
	sys.stdout = saveout 

	print "COMPLETED OSMDataParse"


	# if __name__ == '__main__':
# 	import sys
# 	OSMDataParse(sys.argv[1],sys.argv[2],sys.argv[3])