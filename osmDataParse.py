intputFile = 'cornell.osm'

import xml.etree.ElementTree as ET
tree = ET.parse(intputFile)
root = tree.getroot()

print "University Name (IT IS NOT NECESSARILY THE CORRECT UNIVERSITY):",
uni = 0
for node in root.findall('node'):
	for tag in node.findall('tag'):
		k = tag.get('k')  # needs to find the tag with k="name"
		v = tag.get('v')
		if k == "amenity" and v == "university":
			uni = 1
		if k == "name" and uni == 1:
			print v
			uni = 0

print "Bounds:",
for bound in root.iter('bounds'):
	print bound.attrib

print "lat, lon, name"

for node in root.findall('node'):
	lat = node.get('lat')
	lon = node.get('lon')
	# print nid, lat, lon
	for tag in node.findall('tag'):
		k = tag.get('k')  # needs to find the tag with k="name"
		v = tag.get('v')
		if k == "name":
			print lat + "," + lon + "," + v

# give out binary if building or not
# list out the amenity too if present 
	# could grab library, for example
	# if amenity is not present, set to administrative

# build out `around_latitudes` in this format (20 meters maybe?)
	# [[42.3723963154471, -71.11918887731053], [42.373081932395664, -71.11877045270421], [42.37300267070331, -71.11804625627019], [42.372103043484294, -71.11860952016332]]