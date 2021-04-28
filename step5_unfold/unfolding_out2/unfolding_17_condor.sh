source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/filelist_dir* .
./make_hist filelist_dir3/tight_for_analysis_muon.txt $1 2018 muon data signal endcap fakephoton medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2018/step5_unfold/unfolding_out2
