from NaiveBayes import load_data

# Estimated probability of P(x_i, x_j, y)
# output: A list of estimated joint probability
def tan_prob(X_i, X_j, Y, data, var_names_list, var_values_dict, pseudocount = 1):
	output = []

	ind_i = var_names_list.index(X_i)
	ind_j = var_names_list.index(X_j)
	ind_Y = var_names_list.index(Y)

	for x_i in var_values_dict[X_i]:
		for x_j in var_values_dict[X_j]:
			for y in var_values_dict[Y]:
				temp = pseudocount 
				for obs in data:
					if (obs[ind_i] == x_i \
					and obs[ind_j] == x_j \
					and obs[ind_Y] == y) :
						temp += 1

				output.append(temp)

	return output




# Function to calculate the conditional mutual information between X_i and X_j
# conditional mutual information is used to calculate edge weights
# It's a measure of how much information X_i provides about X_j when the value of Y is known

if __name__ == '__main__':
	#read in the data
	
	data, var_names_list, var_values_dict = load_data("lymph_train.arff")

	print tan_prob('extravasates', 'bl_of_lymph_s', 'class', data, var_names_list, var_values_dict)
