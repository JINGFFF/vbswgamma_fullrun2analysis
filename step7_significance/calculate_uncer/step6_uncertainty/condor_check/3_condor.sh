source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/scalef .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/make_hist* .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/filelist_dir2 .
./make_hist_without_opt filelist_dir2/tight_for_analysis_WGJets_new.txt 1_out_4 2018 electron mc signal endcap WGJets medium
cp -r 1_out_4 /data/pku/home/pengj/testvbs/workdir/ana2018/step7_significance/calculate_uncer/step6_uncertainty/condor_check
