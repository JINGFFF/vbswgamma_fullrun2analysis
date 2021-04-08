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

   system("mkdir -p " + outdir);
   system("mkdir -p " + outdir+"/graph");

   int k=1;
   int n = 0;
 
   TString infilename= inputdir + "/" + which_year + "_" + which_channel +  "_" + which_type + "_" + which_region + "_"+barrel_or_endcap+"_" +  which_btag_workpoint + "_btag_" + which_sample + "_uncertainty.root";

   

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
   outFile.open(outdir + "/" + which_type + "_" + which_sample+"_" + which_region+"_"+which_channel+".py", ios::out);
   int i;
   
   TString var_name = argv[10];
   TString uncertainty_hist_name = "JEC";
cout<<"JEC"<<endl;
   TH1D * tmp1 = get_systematic_jecr_1D(which_region, outdir, which_type, which_sample, uncertainty_hist_name, infilename, var_name, lumi);
   tmp1->Print("all");
   outFile<<which_sample<<"_JEC = [";
   for ( i = 1; i <= tmp1->GetNbinsX(); i++ ){
      if(i==tmp1->GetNbinsX())outFile<<1+tmp1->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp1->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp2 = get_systematic_jecr_1D(which_region, outdir, which_type, which_sample, "JER", infilename, var_name, lumi);
cout<<"JER"<<endl;
   tmp2->Print("all");
   outFile<<which_sample<<"_JER = [";
   for ( i = 1; i <= tmp2->GetNbinsX(); i++ ){
      if(i==tmp2->GetNbinsX())outFile<<1+tmp2->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp2->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp3 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "photon_ID", infilename, var_name, lumi);
   tmp3->Print("all");
   outFile<<which_sample<<"_photon_ID = [";
   for ( i = 1; i <= tmp3->GetNbinsX(); i++ ){
      if(i==tmp3->GetNbinsX())outFile<<1+tmp3->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp3->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp4 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "electron_ID", infilename, var_name, lumi);
   tmp4->Print("all");
   outFile<<which_sample<<"_electron_ID = [";
   for ( i = 1; i <= tmp4->GetNbinsX(); i++ ){
      if(i==tmp4->GetNbinsX())outFile<<1+tmp4->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp4->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp5 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "electron_Reco", infilename, var_name, lumi);
   tmp5->Print("all");
   outFile<<which_sample<<"_electron_Reco = [";
   for (i = 1; i <= tmp5->GetNbinsX(); i++ ){
      if(i==tmp5->GetNbinsX())outFile<<1+tmp5->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp5->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp6 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "electron_HLT", infilename, var_name, lumi);
   tmp6->Print("all");
   outFile<<which_sample<<"_electron_HLT = [";
   for (i = 1; i <= tmp6->GetNbinsX(); i++ ){
      if(i==tmp6->GetNbinsX())outFile<<1+tmp6->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp6->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp7 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "muon_ID", infilename, var_name, lumi);
   tmp7->Print("all");
   outFile<<which_sample<<"_muon_ID = [";
   for (i = 1; i <= tmp7->GetNbinsX(); i++ ){
      if(i==tmp7->GetNbinsX())outFile<<1+tmp7->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp7->GetBinContent(i)<<",";
   }
   i =1;

   TH1D * tmp8 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "muon_iso", infilename, var_name, lumi);
   tmp8->Print("all");
   outFile<<which_sample<<"_muon_iso = [";
   for (i = 1; i <= tmp8->GetNbinsX(); i++ ){
      if(i==tmp8->GetNbinsX())outFile<<1+tmp8->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp8->GetBinContent(i)<<",";
   }

   TH1D * tmp9 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "muon_HLT", infilename, var_name, lumi);
   tmp9->Print("all");
   outFile<<which_sample<<"_muon_HLT = [";
   for (i = 1; i <= tmp9->GetNbinsX(); i++ ){
      if(i==tmp9->GetNbinsX())outFile<<1+tmp9->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp9->GetBinContent(i)<<",";
   }

   TH1D * tmp10 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "fakephoton", infilename, var_name, lumi);
   tmp10->Print("all");
   outFile<<which_sample<<"_fakephoton = [";
   for (i = 1; i <= tmp10->GetNbinsX(); i++ ){
      if(i==tmp10->GetNbinsX())outFile<<1+tmp10->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp10->GetBinContent(i)<<",";
   }

   TH1D * tmp11 = get_systematic_uncertainty_1D(which_region, outdir, which_type, which_sample, "fakelepton", infilename, var_name, lumi);
   tmp11->Print("all");
   outFile<<which_sample<<"_fakelepton = [";
   for (i = 1; i <= tmp11->GetNbinsX(); i++ ){
      if(i==tmp11->GetNbinsX())outFile<<1+tmp11->GetBinContent(i)<<"]"<<endl;
      else outFile<<1+tmp11->GetBinContent(i)<<",";
   }

   return 0;
}
