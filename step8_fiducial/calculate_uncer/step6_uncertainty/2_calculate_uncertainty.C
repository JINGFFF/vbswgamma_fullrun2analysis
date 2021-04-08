#include <algorithm>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
#include "TCanvas.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2D.h"
#include "TF1.h"
#include "TLatex.h"
#include "TMath.h"
#include "TROOT.h"
#include "TTree.h"
#include <TString.h>
#include <TLegend.h>
#include <THStack.h>
#include "plugin2/cal_uncertainty_systematic.h"
#include "plugin2/cal_uncertainty_systematic_in.h"
#include "plugin2/cal_uncertainty_systematic_out.h"

using namespace std;

/*
 * input file list
 * type data: fake, true
 * channel: muon or electron
 */
int main(int argc, char** argv){
   TString inputdir = argv[1];
   TString outdir = argv[2];
   TString which_year = argv[3]; // 2016,2017,2018
   TString which_type = argv[4]; //data, fakelepton, fakephoton, doublefake, mc
   TString which_region = argv[5]; // aqgc, signal, control
   TString which_sample = argv[6]; // SingleMuon, ...
   TString which_channel = argv[7];
   TString barrel_or_endcap = argv[8]; // barrel or endcap

   TString which_btag_workpoint = argv[9]; // tight, medium, loose ...
   TString var_name = argv[10];
   system("mkdir -p " + outdir);
   system("mkdir -p " + outdir+"/graph");

   int k=1;
   int n = 0;
 
   TString infilename= inputdir + "/" + which_year + "_" + which_channel +  "_" + which_type + "_" + which_region + "_"+barrel_or_endcap+"_" +  which_btag_workpoint + "_btag_" + which_sample + "_uncertainty.root";

      TString uncertainty_hist_name = "JEC";


   double lumi;
   if(which_year == "2016") {
      lumi = 35.92;
      //LUMI = "35.92";
   }
   if(which_year == "2017") {
      lumi = 41.50;
      //LUMI = "41.50";
   }
   if(which_year == "2018") {
      lumi = 59.74;
      //LUMI = "59.74";
   }

   if(which_type !="mc") lumi = 1.;
   ofstream outFile;  
   outFile.open(outdir + "/" + which_sample+"_" + which_region+"_"+which_channel+".py", ios::out);
   int i;

   if(which_sample == "WGJJ"){
   //in
   TH1D * tmp_in1 = get_systematic_jecr_in_1D(which_region, outdir, which_sample, uncertainty_hist_name, infilename, var_name, lumi);
   tmp_in1->Print("all");
   outFile<<which_sample<<"_in_JEC = [";
   for ( i = 1; i <= tmp_in1->GetNbinsX(); i++ ){
      if(i==tmp_in1->GetNbinsX())outFile<<1+tmp_in1->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in1->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_in2 = get_systematic_jecr_in_1D(which_region, outdir, which_sample, "JER", infilename, var_name, lumi);
cout<<"JER"<<endl;
   tmp_in2->Print("all");
   outFile<<which_sample<<"_in_JER = [";
   for ( i = 1; i <= tmp_in2->GetNbinsX(); i++ ){
      if(i==tmp_in2->GetNbinsX())outFile<<1+tmp_in2->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in2->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_in3 = get_systematic_uncertainty_in_1D(which_region, outdir, which_sample, "photon_ID", infilename, var_name, lumi);
   tmp_in3->Print("all");
   outFile<<which_sample<<"_in_photon_ID = [";
   for ( i = 1; i <= tmp_in3->GetNbinsX(); i++ ){
      if(i==tmp_in3->GetNbinsX())outFile<<1+tmp_in3->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in3->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_in4 = get_systematic_uncertainty_in_1D(which_region, outdir, which_sample, "electron_ID", infilename, var_name, lumi);
   tmp_in4->Print("all");
   outFile<<which_sample<<"_in_electron_ID = [";
   for ( i = 1; i <= tmp_in4->GetNbinsX(); i++ ){
      if(i==tmp_in4->GetNbinsX())outFile<<1+tmp_in4->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in4->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_in5 = get_systematic_uncertainty_in_1D(which_region, outdir, which_sample, "electron_Reco", infilename, var_name, lumi);
   tmp_in5->Print("all");
   outFile<<which_sample<<"_in_electron_Reco = [";
   for (i = 1; i <= tmp_in5->GetNbinsX(); i++ ){
      if(i==tmp_in5->GetNbinsX())outFile<<1+tmp_in5->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in5->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_in6 = get_systematic_uncertainty_in_1D(which_region, outdir, which_sample, "electron_HLT", infilename, var_name, lumi);
   tmp_in6->Print("all");
   outFile<<which_sample<<"_in_electron_HLT = [";
   for (i = 1; i <= tmp_in6->GetNbinsX(); i++ ){
      if(i==tmp_in6->GetNbinsX())outFile<<1+tmp_in6->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in6->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_in7 = get_systematic_uncertainty_in_1D(which_region, outdir, which_sample, "muon_ID", infilename, var_name, lumi);
   tmp_in7->Print("all");
   outFile<<which_sample<<"_in_muon_ID = [";
   for (i = 1; i <= tmp_in7->GetNbinsX(); i++ ){
      if(i==tmp_in7->GetNbinsX())outFile<<1+tmp_in7->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in7->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_in8 = get_systematic_uncertainty_in_1D(which_region, outdir, which_sample, "muon_iso", infilename, var_name, lumi);
   tmp_in8->Print("all");
   outFile<<which_sample<<"_in_muon_iso = [";
   for (i = 1; i <= tmp_in8->GetNbinsX(); i++ ){
      if(i==tmp_in8->GetNbinsX())outFile<<1+tmp_in8->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in8->GetBinContent(i)<<",";
   }

   TH1D * tmp_in9 = get_systematic_uncertainty_in_1D(which_region, outdir, which_sample, "muon_HLT", infilename, var_name, lumi);
   tmp_in9->Print("all");
   outFile<<which_sample<<"_in_muon_HLT = [";
   for (i = 1; i <= tmp_in9->GetNbinsX(); i++ ){
      if(i==tmp_in9->GetNbinsX())outFile<<1+tmp_in9->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_in9->GetBinContent(i)<<",";
   }

   // out
   TH1D * tmp_out1 = get_systematic_jecr_out_1D(which_region, outdir, which_sample, uncertainty_hist_name, infilename, var_name, lumi);
   tmp_out1->Print("all");
   outFile<<which_sample<<"_out_JEC = [";
   for ( i = 1; i <= tmp_out1->GetNbinsX(); i++ ){
      if(i==tmp_out1->GetNbinsX())outFile<<1+tmp_out1->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out1->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_out2 = get_systematic_jecr_out_1D(which_region, outdir, which_sample, "JER", infilename, var_name, lumi);
cout<<"JER"<<endl;
   tmp_out2->Print("all");
   outFile<<which_sample<<"_out_JER = [";
   for ( i = 1; i <= tmp_out2->GetNbinsX(); i++ ){
      if(i==tmp_out2->GetNbinsX())outFile<<1+tmp_out2->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out2->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_out3 = get_systematic_uncertainty_out_1D(which_region, outdir, which_sample, "photon_ID", infilename, var_name, lumi);
   tmp_out3->Print("all");
   outFile<<which_sample<<"_out_photon_ID = [";
   for ( i = 1; i <= tmp_out3->GetNbinsX(); i++ ){
      if(i==tmp_out3->GetNbinsX())outFile<<1+tmp_out3->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out3->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_out4 = get_systematic_uncertainty_out_1D(which_region, outdir, which_sample, "electron_ID", infilename, var_name, lumi);
   tmp_out4->Print("all");
   outFile<<which_sample<<"_out_electron_ID = [";
   for ( i = 1; i <= tmp_out4->GetNbinsX(); i++ ){
      if(i==tmp_out4->GetNbinsX())outFile<<1+tmp_out4->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out4->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_out5 = get_systematic_uncertainty_out_1D(which_region, outdir, which_sample, "electron_Reco", infilename, var_name, lumi);
   tmp_out5->Print("all");
   outFile<<which_sample<<"_out_electron_Reco = [";
   for (i = 1; i <= tmp_out5->GetNbinsX(); i++ ){
      if(i==tmp_out5->GetNbinsX())outFile<<1+tmp_out5->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out5->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_out6 = get_systematic_uncertainty_out_1D(which_region, outdir, which_sample, "electron_HLT", infilename, var_name, lumi);
   tmp_out6->Print("all");
   outFile<<which_sample<<"_out_electron_HLT = [";
   for (i = 1; i <= tmp_out6->GetNbinsX(); i++ ){
      if(i==tmp_out6->GetNbinsX())outFile<<1+tmp_out6->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out6->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_out7 = get_systematic_uncertainty_out_1D(which_region, outdir, which_sample, "muon_ID", infilename, var_name, lumi);
   tmp_out7->Print("all");
   outFile<<which_sample<<"_out_muon_ID = [";
   for (i = 1; i <= tmp_out7->GetNbinsX(); i++ ){
      if(i==tmp_out7->GetNbinsX())outFile<<1+tmp_out7->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out7->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp_out8 = get_systematic_uncertainty_out_1D(which_region, outdir, which_sample, "muon_iso", infilename, var_name, lumi);
   tmp_out8->Print("all");
   outFile<<which_sample<<"_out_muon_iso = [";
   for (i = 1; i <= tmp_out8->GetNbinsX(); i++ ){
      if(i==tmp_out8->GetNbinsX())outFile<<1+tmp_out8->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out8->GetBinContent(i)<<",";
   }

   TH1D * tmp_out9 = get_systematic_uncertainty_out_1D(which_region, outdir, which_sample, "muon_HLT", infilename, var_name, lumi);
   tmp_out9->Print("all");
   outFile<<which_sample<<"_out_muon_HLT = [";
   for (i = 1; i <= tmp_out9->GetNbinsX(); i++ ){
      if(i==tmp_out9->GetNbinsX())outFile<<1+tmp_out9->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp_out9->GetBinContent(i)<<",";
   }





   }
   
   //TString var_name = argv[10];
   //TString uncertainty_hist_name = "JEC";
cout<<"JEC"<<endl;
   TH1D * tmp1 = get_systematic_jecr_1D(which_region, outdir, which_sample, uncertainty_hist_name, infilename, var_name, lumi);
   tmp1->Print("all");
   outFile<<which_sample<<"_JEC = [";
   for ( i = 1; i <= tmp1->GetNbinsX(); i++ ){
      if(i==tmp1->GetNbinsX())outFile<<1+tmp1->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp1->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp2 = get_systematic_jecr_1D(which_region, outdir, which_sample, "JER", infilename, var_name, lumi);
cout<<"JER"<<endl;
   tmp2->Print("all");
   outFile<<which_sample<<"_JER = [";
   for ( i = 1; i <= tmp2->GetNbinsX(); i++ ){
      if(i==tmp2->GetNbinsX())outFile<<1+tmp2->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp2->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp3 = get_systematic_uncertainty_1D(which_region, outdir, which_sample, "photon_ID", infilename, var_name, lumi);
   tmp3->Print("all");
   outFile<<which_sample<<"_photon_ID = [";
   for ( i = 1; i <= tmp3->GetNbinsX(); i++ ){
      if(i==tmp3->GetNbinsX())outFile<<1+tmp3->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp3->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp4 = get_systematic_uncertainty_1D(which_region, outdir, which_sample, "electron_ID", infilename, var_name, lumi);
   tmp4->Print("all");
   outFile<<which_sample<<"_electron_ID = [";
   for ( i = 1; i <= tmp4->GetNbinsX(); i++ ){
      if(i==tmp4->GetNbinsX())outFile<<1+tmp4->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp4->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp5 = get_systematic_uncertainty_1D(which_region, outdir, which_sample, "electron_Reco", infilename, var_name, lumi);
   tmp5->Print("all");
   outFile<<which_sample<<"_electron_Reco = [";
   for (i = 1; i <= tmp5->GetNbinsX(); i++ ){
      if(i==tmp5->GetNbinsX())outFile<<1+tmp5->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp5->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp6 = get_systematic_uncertainty_1D(which_region, outdir, which_sample, "electron_HLT", infilename, var_name, lumi);
   tmp6->Print("all");
   outFile<<which_sample<<"_electron_HLT = [";
   for (i = 1; i <= tmp6->GetNbinsX(); i++ ){
      if(i==tmp6->GetNbinsX())outFile<<1+tmp6->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp6->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp7 = get_systematic_uncertainty_1D(which_region, outdir, which_sample, "muon_ID", infilename, var_name, lumi);
   tmp7->Print("all");
   outFile<<which_sample<<"_muon_ID = [";
   for (i = 1; i <= tmp7->GetNbinsX(); i++ ){
      if(i==tmp7->GetNbinsX())outFile<<1+tmp7->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp7->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp8 = get_systematic_uncertainty_1D(which_region, outdir, which_sample, "muon_iso", infilename, var_name, lumi);
   tmp8->Print("all");
   outFile<<which_sample<<"_muon_iso = [";
   for (i = 1; i <= tmp8->GetNbinsX(); i++ ){
      if(i==tmp8->GetNbinsX())outFile<<1+tmp8->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp8->GetBinContent(i)<<",";
   }

   TH1D * tmp9 = get_systematic_uncertainty_1D(which_region, outdir, which_sample, "muon_HLT", infilename, var_name, lumi);
   tmp9->Print("all");
   outFile<<which_sample<<"_muon_HLT = [";
   for (i = 1; i <= tmp9->GetNbinsX(); i++ ){
      if(i==tmp9->GetNbinsX())outFile<<1+tmp9->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp9->GetBinContent(i)<<",";
   }

   return 0;
}
