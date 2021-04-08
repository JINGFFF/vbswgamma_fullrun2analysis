import os
#print(os.system("ls >>de"))

n=0
year = '2018'
dir1 = '/home/pku/pengj/testvbs/data/fakephoton'
#infile =open('2.sh', 'r')
infile =open('check.sh', 'r')

lines = infile.readlines()
#out_file_name = year + '_'
#outfile = open(out_file_name, 'w')
#for i in range(0, 2):
#for i in range(0,20000):
for i in range(0, len(lines)):
    x = lines[i].split('\n')
    if "#" in x[0] :
        continue

    out_file_name = str(i) + '_condor.sh'
    outfile = open(out_file_name, 'w')

    outfile.write('source /cvmfs/cms.cern.ch/cmsset_default.sh' + '\n')
    outfile.write('cmsrel CMSSW_9_3_4'+'\n')
    outfile.write('cd CMSSW_9_3_4/src'+'\n')
    outfile.write('cmsenv'+'\n')
    outfile.write('cd ../..'+'\n')
    outfile.write('cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/scalef .'+'\n')
    #outfile.write('cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/make_hist_control .'+'\n')
    outfile.write('cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/make_hist* .'+'\n')
    outfile.write('cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/filelist_dir2 .'+'\n')
    outfile.write(x[0]+'\n')
    outfile.write('cp -r 1_out_4 /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/condor_check'+'\n')

    print(i)
    #print(len(lines))

    outfile.close()

    out_file_name2 = str(i) + '_condor.sub'
    outfile2 = open(out_file_name2, 'w')
    outfile2.write('+AcctGroup = "pku"'+'\n')
    outfile2.write('+AcctGroupUser  = "pengj"'+'\n')
    outfile2.write('executable   = ' + out_file_name +'\n')
    outfile2.write('arguments    ='+'\n')
    outfile2.write('output       = outputfile_'+ str(i)+'\n')
    outfile2.write('error        = errorfile_' + str(i) +'\n')
    outfile2.write('log          = myexe_' + str(i) + '.log'+'\n')
    outfile2.write('request_cpus   = 1'+'\n')
    outfile2.write('request_memory = 2024'+'\n')
    outfile2.write('request_disk   = 20240'+'\n')
    outfile2.write('should_transfer_files = yes'+'\n')
    outfile2.write('queue'+'\n')
    outfile2.close()
    os.system("chmod 777 " + out_file_name)
    os.system("condor_submit " + out_file_name2)

infile.close()
