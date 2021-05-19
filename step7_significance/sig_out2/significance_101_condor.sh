source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/filelist_dir* .
./make_hist_mc filelist_dir3/tight_for_analysis_WGJJ_d0.txt $1 2017 electron mc control barrel WGJJ medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/sig_out2
