void test(){
   TFile * data1 = TFile::Open("1_out_1/2016_muon_data_signal_barrel_medium_btag_SingleMuon_uncertainty.root");
TH1D* DATA1 = (TH1D*)data1->Get("hist_");
DATA1->Print();
cout<<DATA1->GetSum()<<endl;

}
