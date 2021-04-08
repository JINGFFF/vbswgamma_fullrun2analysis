#signal
./make_hist_bkg filelist_dir/tight_for_analysis_electron.txt 1_out_2 2016 electron data signal SingleElectron medium
./make_hist_bkg filelist_dir/loose_for_analysis_electron.txt 1_out_2 2016 electron doublefake signal SingleElectron medium
./make_hist_bkg filelist_dir/tight_for_analysis_electron.txt 1_out_2 2016 electron fakephoton signal SingleElectron medium
./make_hist_bkg filelist_dir/loose_for_analysis_electron.txt 1_out_2 2016 electron fakelepton signal SingleElectron medium
#control
./make_hist_bkg filelist_dir/tight_for_analysis_electron.txt 1_out_2 2016 electron data control SingleElectron medium
./make_hist_bkg filelist_dir/loose_for_analysis_electron.txt 1_out_2 2016 electron doublefake control SingleElectron medium
./make_hist_bkg filelist_dir/tight_for_analysis_electron.txt 1_out_2 2016 electron fakephoton control SingleElectron medium
./make_hist_bkg filelist_dir/loose_for_analysis_electron.txt 1_out_2 2016 electron fakelepton control SingleElectron medium
#signal
./make_hist_bkg filelist_dir/tight_for_analysis_muon.txt 1_out_2 2016 muon data signal SingleMuon medium
./make_hist_bkg filelist_dir/loose_for_analysis_muon.txt 1_out_2 2016 muon doublefake signal SingleMuon medium
./make_hist_bkg filelist_dir/tight_for_analysis_muon.txt 1_out_2 2016 muon fakephoton signal SingleMuon medium
./make_hist_bkg filelist_dir/loose_for_analysis_muon.txt 1_out_2 2016 muon fakelepton signal SingleMuon medium
#control
./make_hist_bkg filelist_dir/tight_for_analysis_muon.txt 1_out_2 2016 muon data control SingleMuon medium
./make_hist_bkg filelist_dir/loose_for_analysis_muon.txt 1_out_2 2016 muon doublefake control SingleMuon medium
./make_hist_bkg filelist_dir/tight_for_analysis_muon.txt 1_out_2 2016 muon fakephoton control SingleMuon medium
./make_hist_bkg filelist_dir/loose_for_analysis_muon.txt 1_out_2 2016 muon fakelepton control SingleMuon medium
