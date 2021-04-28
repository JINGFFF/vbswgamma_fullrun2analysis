source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_3_4
cd CMSSW_9_3_4/src
cmsenv
cd ../..
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step6_fiducial_xs/scalef .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step6_fiducial_xs/make_hist* .
cp -r /data/pku/home/pengj/testvbs/analysis/analysis2018/step6_fiducial_xs/filelist_dir* .
./make_hist filelist_dir3/loose_for_analysis_muon.txt $1 2018 muon data control barrel doublefake medium T
cp -r $1 /data/pku/home/pengj/testvbs/analysis/analysis2018/step6_fiducial_xs/fiducial_out1
