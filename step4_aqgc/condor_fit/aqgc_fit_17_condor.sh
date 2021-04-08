source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step4_aqgc/scalef .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step4_aqgc/fit_ratio .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step4_aqgc/filelist_dir .
./fit_ratio filelist_dir/tight_for_analysis_WGJJ_aqgc.txt $1 2018 muon mc wgaqgc medium 4
cp -r $1 /data/pku/home/pengj/testvbs/workdir/ana2018/step4_aqgc/condor_fit
