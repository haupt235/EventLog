def library_creator(data_input): 
	
	file = open(data_input, "r+")

	lines = file.readlines()

	event = []
	index = []

	for line in lines:
		if len(line) > 5:
			if line[4] == 'r' or line[4] =='c' or line[4] == 's' or line[4] == 't':
				n = line
	print(n)



	read until event log
