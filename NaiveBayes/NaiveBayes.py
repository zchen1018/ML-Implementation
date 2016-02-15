# Read names of the features from the Hearder part and data from the Data part
# input: name of the ARFF file
# output: a list of rows and a list of variable names
def load_data(file):
	f = open(file)

	variable_names = [] # A list of variable names
	variable_column = {} # A dictionary for variables
	rows_matrix = [] # A list of each observation

	for line in f:
		line = line.replace('\n', '')
		if line.startswith("%") or line.startswith("@data") or (not line.strip()) \
			or line.startswith("@relation"):
			continue # skip these rows 
		elif line.startswith("@attribute"):
			line_list = line.split(" ", 2) # split into a list of size 3
			
			var_name = line_list[1].replace("'", "")
			variable_names.append(var_name)
			var_value = line_list[2].strip("{ }").replace(" ", "").split(",")
			variable_column[var_name] = var_value
		else: # data line
			rows_matrix.append(line.split(","))

	return rows_matrix, variable_names, variable_column

# calculate the number of the occurence for a given variable
# return a dictionary : {var1: num1, var2: num2, ...}
def countX(data, var_name, var_values_dict, var_names_list) :
	ind = var_names_list.index(var_name) # get the index for the variable
	var_values = var_values_dict[var_name] # all values of the variable
	output = dict((ele, 0) for ele in var_values) # create a list with variable values as keys
	
	for obs in data:
		output[obs[ind]] += 1

	return output


# 
# def bayes_learning(training_set): # training_set is a list of rows
# 	class_labels = set([x['class'] for x in training_set)
# 	# a list to store the learning result 
# 	# each element is of the form [label, {variable_name: var}, conditional_prob]
# 	learning_result = []
# 	for label in class_labels:
# 		data_of_class = [x for x in training_set if x['class'] == label]
# 		for var_name in data_of_class[0].keys()[:-1]:

	

