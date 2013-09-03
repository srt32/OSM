# this script is fed data from getDBSChoolData.py (around_lat, id, name)
# this data is then passed to OSMDataParse.py, which will need to output a CSV (to be uploaded)

# EXAMPLE CALL -- python subProcessTest.py 11.54 48.14 11.543 48.145 testAPIOutput_2.txt

# get the bounds from it and pass it to OSM_API_Call
def OSMAPICall(left,bot,right,top,outputName,schoolName,schoolID,OutputFile):
	import subprocess
	print "STARTING OSMAPICall"

	fileName = str(outputName) # "testAPIOutput_2.txt" 
	o_file = open(fileName, "w")

	left = str(left).lstrip(' ') 
	bottom = str(bot).lstrip(' ')
	right = str(right).lstrip(' ')
	top = str(top).lstrip(' ')

	print "BLAH" + left + "BLAH"

	link = "http://api.openstreetmap.org/api/0.6/map?bbox=" + left + "," + top + "," + right + "," + bottom

	cmdCall = "curl " + '"' + link + '"'

	print "The API call requested is " + cmdCall

	subprocess.call(cmdCall, shell=True, stdout = o_file)
	# print "Data output to " + str(fileName)

	return outputName,OutputFile

	print "COMPLETED OSMAPICall"

# if __name__ == '__main__':
# 	import sys
# 	OSMAPICall(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], "<schoolName>", "<schoolID>")