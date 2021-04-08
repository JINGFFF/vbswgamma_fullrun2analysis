source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step8_fiducial/calculate_uncer/step6_uncertainty/scalef .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step8_fiducial/calculate_uncer/step6_uncertainty/make_hist_bkg_control2 .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step8_fiducial/calculate_uncer/step6_uncertainty/make_hist_control2 .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step8_fiducial/calculate_uncer/step6_uncertainty/make_hist_bkg .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step8_fiducial/calculate_uncer/step6_uncertainty/make_hist .
cp -r /data/pku/home/pengj/testvbs/workdir/ana2018/step8_fiducial/calculate_uncer/step6_uncertainty/filelist_dir2 .
./make_hist_bkg filelist_dir2/loose_for_analysis_electron.txt $1 2018 electron doublefake signal endcap SingleElectron medium
cp -r $1 /data/pku/home/pengj/testvbs/workdir/ana2018/step8_fiducial/calculate_uncer/step6_uncertainty/condor_dir
