void plot(){
   TFile *file18 =new TFile("testfakepho2/2018_muon_data_signal_barrel_fakephoton.root");
   TH1D *h18 = (TH1D*) file18->Get("mjj");
   h18->SetLineColor(kRed);
   h18->SetStats(0);
   //h18->Scale(1./h18->GetSum());
   h18->SetXTitle("M_{jj} [GeV]");
   h18->Draw("hist");

   TFile *file17 =new TFile("/home/pku/pengj/testvbs/analysis/analysis2017/step7_significance/testfakepho2/2017_muon_data_signal_barrel_fakephoton.root");
                             ///home/pku/pengj/testvbs/analysis/analysis2017/step7_significance/testfakepho2/2017_muon_data_signal_barrel_data.root
   TH1D *h17 = (TH1D*) file17->Get("mjj");
   h17->SetLineColor(kBlue);
   h17->SetStats(0);
   //h17->Scale(1./h17->GetSum());
   h17->Draw("hist same");

   TLegend * leg = new TLegend(0.63, 0.68, 0.88, 0.88);
   leg->SetFillStyle(0);
   leg->SetLineColor(0);
   leg->SetFillColor(10);
   leg->SetBorderSize(0);
   //leg.SetHeader(str(pt_down) + "GeV<p_{T}^{#gamma}<"+ str(pt_up) + "GeV", "c");
   leg->AddEntry(h17, "2017", "L");
   leg->AddEntry(h18, "2018", "L");
   leg->Draw("same");

}
