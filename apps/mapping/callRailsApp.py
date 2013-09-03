def callRailsApp(OutputFile):
	print "STARTING callRailsApp -- MAKE SURE RAILS SERVER IS RUNNING IN SEPERATE PROCESS & DB TABLE IS EMPTY"
	import subprocess
	import os

	print "# find file path"
	file_path = os.path.realpath(OutputFile)
	print file_path

	print "# need to cd to correct directory -- /Users/Simon/campuscene/osm/apps/mapping"
	#subprocess.call("pwd", shell=True)
	os.chdir("/Users/Simon/campuscene/Apps/osm/apps/mapping")
	#subprocess.call("pwd", shell=True)
	pwd = os.getcwd()
	print "pwd is " + pwd

	print "# start server - rails s [FOR TIME BEING, ASSUME SERVER IS RUNNING IN OTHER PROCESS]"
	#subprocess.call("rails s", shell=True)

	print "# copy output file to local dir (pass name through function)"
	cmd_string = "cp " + file_path + " " + pwd + "/" + OutputFile
	print "cmd_string is " + cmd_string
	os.system(cmd_string)

	print "# run rake task (with correct inputs) -- rake csv_model_import[bunnies.csv,Datapoint]"
	cmd_string = "rake csv_model_import[" + OutputFile + ",Datapoint]"
	print "rake command string is " + cmd_string
	os.system(cmd_string)


	print "COMPLETED callRailsApp"

if __name__ == '__main__':
	import sys
	callRailsApp(sys.argv[1])