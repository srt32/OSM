def callRailsApp(OutputFileDB):
	print "STARTING callRailsApp"

	print "# need to cd to correct directory -- /Users/Simon/campuscene/osm/apps/mapping"

	print "# start server - rails s"

	print "# copy output file to local dir (pass name through function)"

	print "# run rake task (with correct inputs) -- rake csv_model_import[bunnies.csv,Datapoint]"

	print "COMPLETED callRailsApp"

if __name__ == '__main__':
	import sys
	callRailsApp(sys.argv[1])