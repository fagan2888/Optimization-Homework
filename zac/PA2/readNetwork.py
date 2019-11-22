#read the file
f = open('facebook_combined.txt', 'r')
G = {}
# Loop over lines and extract variables of interest
for line in f:
		line = line.strip()
		#print(line)
		nodes = line.split(' ')
		G[(int(nodes[0]), int(nodes[1]))]=1
f.close()
print('Finished reading the file')
