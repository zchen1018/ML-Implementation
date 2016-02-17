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
# using Laplace estimates with pseudocounts = 1
# return a dictionary : {var1: num1, var2: num2, ...}
def countX(data, var_name, var_values_dict, var_names_list, pseudocount = 1) :
	ind = var_names_list.index(var_name) # get the index for the variable
	var_values = var_values_dict[var_name] # all values of the variable
	output = dict((ele, pseudocount) for ele in var_values) # create a list with variable values as keys
	
	for obs in data:
		output[obs[ind]] += 1

	return output

# Learning the frequency for each variable
# output: a list of dictionary, each is the adjusted frequency for each variable value
def count_frequency(data, var_values_dict, var_names_list) :
	freq_result = [] # a list for frequency of each variable
	for var in var_names_list[:-1]: # not include the class variable
		freq_result.append(countX(data, var, var_values_dict, var_names_list))

	return freq_result

# Estimate the probabilty for the class variable
def class_prob(data, var_values_dict, var_names_list):
	count = countX(data, 'class', var_values_dict, var_names_list, 0) # no pseudocount
	sample_size = float(sum(count.values()))
	for x in count:
		count[x] /= sample_size
	return count

# Estimate conditional probability P(X = x | y) for each x
# output: a list of conditioanl prob estimate for each class in target variable
def conditional_prob(data, var_values_dict, var_names_list):
	freq_list = []
	name = var_names_list[-1] # Assume that the target variable is always the last variable in the data
	target = var_values_dict[name]
	for target_var in target:
		# Find the data of the specific class value
		class_data = []
		for obs in data:
			if obs[-1] == target_var:
				class_data.append(obs)

		freq_list.append(count_frequency(class_data, var_values_dict, var_names_list))

	for freq in freq_list: # freq is a list of frequency dictionaries for each variable
		for x in freq: # x is a frequence dictionary for a variable
	 		group_sum = float(sum(x.values())) 
	 		for temp in x:
	 			x[temp] /= group_sum # update the requence with the probability

	return freq_list

# The output of class_prob() and conditional_prob() are basically the learning result
# from the data
# To wrap up the learning phase
data, var_names_list, var_values_dict = load_data("lymph_train.arff")

Y_prob = class_prob(data, var_values_dict, var_names_list)
X_cond_prob = conditional_prob(data, var_values_dict, var_names_list)

	

