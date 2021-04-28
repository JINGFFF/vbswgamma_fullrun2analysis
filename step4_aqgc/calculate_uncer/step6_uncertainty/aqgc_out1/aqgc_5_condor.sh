source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step4_aqgc/calculate_uncer/step6_uncertainty/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step4_aqgc/calculate_uncer/step6_uncertainty/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step4_aqgc/calculate_uncer/step6_uncertainty/filelist_dir* .
./make_hist filelist_dir3/loose_for_analysis_electron.txt $1 2018 electron data aqgc all fakelepton medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2018/step4_aqgc/calculate_uncer/step6_uncertainty/aqgc_out1