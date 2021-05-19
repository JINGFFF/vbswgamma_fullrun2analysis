source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/filelist_dir* .
./make_hist filelist_dir/lep.txt $1 2016 data all data data_lepton medium 4 7
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2016/step2_fake_photon/test_sideband