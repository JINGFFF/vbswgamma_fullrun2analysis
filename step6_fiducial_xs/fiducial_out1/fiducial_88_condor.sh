source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step6_fiducial_xs/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step6_fiducial_xs/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2017/step6_fiducial_xs/filelist_dir* .
./make_hist_mc filelist_dir3/tight_for_analysis_WW.txt $1 2017 muon mc signal endcap WW medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2017/step6_fiducial_xs/fiducial_out1
