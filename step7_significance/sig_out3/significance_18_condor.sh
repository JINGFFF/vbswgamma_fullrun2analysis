source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/filelist_dir* .
./make_hist filelist_dir3/loose_for_analysis_muon.txt $1 2017 muon data signal endcap fakelepton medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2017/step7_significance/sig_out3