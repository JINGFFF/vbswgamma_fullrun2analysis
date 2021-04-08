TH1D * get_scale_uncertainty_1D(TString which_region, TString outdir, TString which_sample, TString uncertainty_hist_name, TString infilename, TString var_name, double lumi ){

   int scale_weight_index_1, scale_weight_index_2, scale_weight_index_3;

   if(which_sample == "WGJJ"){
      scale_weight_index_1 = 225;
      scale_weight_index_2 = 240;
      scale_weight_index_3 = 255;
   }
   else if(which_sample == "WGJets"){
      scale_weight_index_1 = 0;
      scale_weight_index_2 = 3;
      scale_weight_index_3 = 6;

   }



cout<<"ok0"<<endl;
   TFile*input = new TFile (infilename);
cout<<"ok0"<<endl;



   TCanvas * c1 = new TCanvas(uncertainty_hist_name,uncertainty_hist_name,900,900);

   c1->cd();
   h_up->SetTitle(var_name + "_" + uncertainty_hist_name);
   h_up->Draw("hist");
   h_center->Draw("hist same");
   h_down->Draw("hist same");

   TLegend* leg3 = new TLegend(0.7,0.8,0.88,0.89);
   leg3->AddEntry(h_up,     "up");
   leg3->AddEntry(h_center, "center");
   leg3->AddEntry(h_down,   "down");

   double maximum       = 1.2 * h_up->GetMaximum();
   h_up->SetMaximum(maximum);
   leg3->Draw();

   c1->SaveAs(outdir+"/graph/"+which_sample+"_"+which_region+"_"+uncertainty_hist_name+".png");

   return h_uncertainty;
   input->Close();

