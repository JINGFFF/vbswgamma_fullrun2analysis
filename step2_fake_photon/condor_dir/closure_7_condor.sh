source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/scalef .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/make_hist2 .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/filelist_dir .
./make_hist2 filelist_dir/tight_for_fakephoton_WJets_2j.txt $1 2018 mc all real_fake W2Jets medium 4 10
cp -r $1 /data/pku/home/pengj/testvbs/workdir/ana2018/step2_fake_photon/condor_dir
