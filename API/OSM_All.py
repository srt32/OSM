def main(fileName,schoolName,outputName,OutputFile):
	import sys
	from getDBSchoolData import getDBSchoolData
	from OSMAPICall import OSMAPICall
	from OSMParseForRails import OSMParseForRails

	print "STARTING OSM_ALL"

	left,bot,right,top,outputName,schoolName,schoolID,OutputFile = getDBSchoolData(fileName,schoolName,outputName, OutputFile)
	inputFile,OutputFile = OSMAPICall(left,bot,right,top,outputName,schoolName,schoolID,OutputFile) # need to sync up outputName from above with inputFile from below
	OSMParseForRails(inputFile,OutputFile) # needs to be piped to OutputFile (PROBABLY WITHINT THE FUNCTION)
	# OSMDataParse(inputFile,OutputFileDB) # CODE NEEDS TO BE UPDATED // NEED TO PASS PARAMS THROUGH OTHERS
	# callRailsApp()

	# rake the piped output file in rails app to review DP's
	print "COMPLETED OSM_All"
 	# if __name__ == '__main__':
 	# 	import sys
 	# 	main(sys.argv[1],sys.argv[2])

import sys
main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


# EXAMPLE CALL!
# cd /Users/Simon/campuscene/osm/API
# python OSM_All.py schools_subset.xml "SUNY at Binghamton" testOutput.txt OutputFile.txt

# NOTES:
	# currently does not work with existing schools in CS (data is formatted differently in the around_lats field)