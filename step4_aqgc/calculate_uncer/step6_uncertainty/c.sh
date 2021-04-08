source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/workdir/ana2016/step7_significance/calculate_uncer/step6_uncertainty/scalef .
/data/pku/home/pengj/testvbs/workdir/ana2016/step7_significance/calculate_uncer/step6_uncertainty/make_hist /data/pku/home/pengj/testvbs/workdir/ana2016/step7_significance/calculate_uncer/step6_uncertainty/filelist_dir/tm.txt 1_out_condor 2016 muon data signal barrel SingleMuon medium
cp -r 1_out_condor /data/pku/home/pengj/testvbs/workdir/ana2016/step7_significance/calculate_uncer/step6_uncertainty/1_out_condor
