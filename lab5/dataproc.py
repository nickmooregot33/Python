def get_data(filename):
	with open(filename,'r') as datalist:
		print('Using file %s'%filename)
		data = datalist.read().splitlines()
	
	set = []
	print data[0]
	for line in data[1:]:
		set.append(float(line))
	datalist.close()
	
	return set
	
def normalize(dataset):
	minimum = min(dataset)
	maximum = max(dataset)
	data_range = maximum - minimum
	newdata = []
	for value in dataset:
		newdata.append((value-minimum)/data_range)
	return newdata

print "Opening file"
data = get_data('data1.txt')
print "Done"
#print data
print "Normalizing data"

norm_data = normalize(data)
print "Done"
print min(norm_data)==0.0
print max(norm_data) == 1.0
print norm_data[0] == 0.003017004936917169

