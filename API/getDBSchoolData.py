# this script will take the school_DB dump and parse it to pull out the around_latitudes, name, id 
	# for the input school name -- Example = "University of Denver"
# this data is then passed to OSMAPICall.py
def getDBSchoolData(fileName,schoolName,outputName,OutputFile,OutputFileDB):
	print "STARTING getDBSchoolData"
	import sys
	import re
	import xml.etree.ElementTree as ET
	intputFile = open(sys.argv[1])

	tree = ET.parse(intputFile)
	root = tree.getroot()

	outputnName = outputName

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
				# print name,
			if target == 1 and key == "around_latitudes":
				school_id = school_id_local
				# print school_id,
				around_lats = value
				# print around_lats
				target = 0

	# format output for global vars
	# parse the results into "left,bot,right,top,schoolName,schoolID" using around_lats, name, school_id
	lats_list = around_lats.split('],')
	A = lats_list[0]
	A = re.sub('[[]', '', A)
	A = re.sub('[]]', '', A)
	A = A.split(',')
	top = A[0]
	print "top is " + top

	B = lats_list[1]
	B = re.sub('[[]', '', B)
	B = re.sub('[]]', '', B)
	B = B.split(',')
	right = B[1]
	print "right is " + right

	C = lats_list[2]
	C = re.sub('[[]', '', C)
	C = re.sub('[]]', '', C)
	C = C.lstrip()
	C = C.split(',')
	bot = C[0]
	print "bot is " + bot

	D = lats_list[3]
	D = re.sub('[[]', '', D)
	D = re.sub('[]]', '', D)
	D = D.split(',')
	left = D[1]
	print "left is " + left

	schoolName = schoolName 
	print "school name is " + schoolName
	schoolID = school_id 
	print "school id is " + schoolID

	print "COMPLETED getDBSchoolData"
	return (left,bot,right,top,outputName,schoolName,schoolID,OutputFile,OutputFileDB)

	if __name__ == '__main__':
 		import sys
 		getDBSchoolData(sys.argv[1],sys.argv[2])