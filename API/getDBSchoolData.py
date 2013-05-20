# this script will take the school_DB dump and parse it to pull out the around_latitudes, name, id 
	# for the input school name -- Example = "University of Denver"
# this data is then passed to OSMAPICall.py

def OSMParse(fileName,schoolName):
	import xml.etree.ElementTree as ET
	intputFile = open(sys.argv[1])

	tree = ET.parse(intputFile)
	root = tree.getroot()

	target = 0
	for row in root.findall('row'):
		for field in row.findall('field'):
			key = field.get('name')
			value = field.text
			if key == "id":
				school_id_local = value
			if value == schoolName and key == "title":
				target = 1
				name = str(value)
				print name,
			if target == 1 and key == "around_latitudes":
				school_id = school_id_local
				print school_id,
				around_lats = value
				print around_lats
				target = 0

# parse the results into "left,bot,right,top,outputName,schoolName,schoolID"

if __name__ == '__main__':
	import sys
	OSMParse(sys.argv[1],sys.argv[2])