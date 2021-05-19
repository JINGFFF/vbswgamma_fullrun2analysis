source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/filelist_dir* .
./make_hist filelist_dir/tight_for_fakephoton_WJets.txt $1 2016 mc all fake WJets medium 4 10
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/test_closure