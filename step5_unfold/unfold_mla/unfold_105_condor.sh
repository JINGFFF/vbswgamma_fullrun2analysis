source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/filelist_dir* .
./make_hist_mla_mc filelist_dir3/tight_for_analysis_ZG.txt $1 2018 electron mc control barrel ZG medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/unfold_mla
