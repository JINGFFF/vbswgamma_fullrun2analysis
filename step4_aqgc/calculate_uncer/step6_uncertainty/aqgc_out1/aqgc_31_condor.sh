source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step4_aqgc/calculate_uncer/step6_uncertainty/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step4_aqgc/calculate_uncer/step6_uncertainty/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step4_aqgc/calculate_uncer/step6_uncertainty/filelist_dir* .
./make_hist_mc filelist_dir3/tight_for_analysis_ST_tbarW.txt $1 2016 muon mc aqgc all ST_tbarW medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2016/step4_aqgc/calculate_uncer/step6_uncertainty/aqgc_out1
