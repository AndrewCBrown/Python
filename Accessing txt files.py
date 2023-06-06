infile="test.txt"

outfile="newtest.txt"

input_file=open(infile,"r")

output_file=open(outfile,"w")

for line in input_file:
    print(line)
    output_file.write(line)

input_file.close()
output_file.close()

