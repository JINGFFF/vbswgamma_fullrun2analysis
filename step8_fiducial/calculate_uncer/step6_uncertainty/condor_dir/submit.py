import os
#print(os.system("ls >>de"))

n=128
year = '2016'
dir1 = '/home/pku/pengj/testvbs/data/fakephoton'
infile =open('condor.sub', 'rw')
#lines = infile.readlines()
out_file_name = year + '_move.sh'
outfile = open(out_file_name, 'w')
#for i in range(0, 2):
#for i in range(0,20000):
for i in range(128):
    print(i)
    #for i in range(0, len(lines)):
    infile =open('condor.sub', 'r+')
    for line in infile:
        print(line)
        if (line.startswith("executable")):
            oldline = line
            newline = "executable   = "+ str(i) +"_concor.sh"  + "\n" 
            line.rstrip().replace('oldLine', 'newLine')
            infile.write(line)

    infile.close()
    #os.system("condor_submit condor.sub") 
