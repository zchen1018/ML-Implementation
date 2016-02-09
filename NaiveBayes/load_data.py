# Read names of the features from the Hearder part and data from the Data part
# input: name of the ARFF file
# output: a list of rows and a list of variable names
def load_data(file):
	f = open(file)
	variable_names = []

	rows_list = [] # add each row to the list and convert it to a DataFrame

	for line in f:
		if line.startswith("%") or line.startswith("@data") or (not line.strip()) \
			or line.startswith("@relation"):
			continue
		elif line.startswith("@attribute"):
			line_list = line.split(" ")
			variable_names.append(line_list[1].replace("'", ""))
		else:
			row_dict = {}
			obs_list = line.split(",")
			for i in range(len(variable_names)):
				#print "now processing the row " + str(variable_names[i])
				row_dict[variable_names[i]] = obs_list[i].replace('\n', '')

			rows_list.append(row_dict)

	return rows_list, variable_names

