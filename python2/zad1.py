import sys
read1 = sys.argv[1]
write1 = sys.argv[2]
with open(read1, 'r') as f:
	data = f.read()
print('Data from file:\n{}'.format(data))
with open (write1, 'w') as f:
	f.write(data)


