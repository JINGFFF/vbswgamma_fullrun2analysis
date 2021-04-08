source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/scalef .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/make_hist2 .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/filelist_dir .
./make_hist2 filelist_dir/tight_for_fakephoton_lepton.txt $1 2018 data all data data_lepton medium 4 7
cp -r $1 /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/condor_dir
