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
#include "TH2.h"
#include "TStyle.h"
#include <iostream>
#include "TLegend.h"
#include "THStack.h"
using namespace std;

TH1D * get_systematic_jecr_1D(TString which_region, TString outdir, TString which_sample, TString uncertainty_hist_name, TString infilename, TString var_name, double lumi ){
cout<<"ok0"<<endl;
   TFile*input = new TFile (infilename);
cout<<"ok0"<<endl;
   TH1D * h_center   = (TH1D*)input->Get("hist_"+var_name+"_");
   TH1D * h_up       = (TH1D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_up");
   TH1D * h_down     = (TH1D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_down");
   h_center->Scale(lumi);
cout<<"ok1"<<endl;
h_center->Print("all");
cout<<"ok1"<<endl;

   h_up->Scale(lumi);
   h_down->Scale(lumi);

   h_center->SetLineColor(kBlack);
   h_up->SetLineColor(kBlue);
   h_down->SetLineColor(kRed);

   h_center->SetStats(kFALSE);
   h_up->SetStats(kFALSE);
   h_down->SetStats(kFALSE);

   int NbinsX = h_center->GetNbinsX();
   int NbinsY = h_center->GetNbinsY();

   int Nbins = NbinsX*NbinsY;
   TH1D * h_uncertainty = new TH1D("h", "h", Nbins, 0, Nbins);

   double uncertainty[NbinsX*NbinsY];
   double bincontent[NbinsX*NbinsY],bincontent_up[NbinsX*NbinsY],bincontent_down[NbinsX*NbinsY];

   for(int j=0;j<NbinsX;j++){
         bincontent[NbinsY*j] = h_center->GetBinContent(j+1);
         bincontent_up[NbinsY*j] = h_up->GetBinContent(j+1);
         bincontent_down[NbinsY*j] = h_down->GetBinContent(j+1);
         double max;
         if(fabs(bincontent_up[NbinsY*j]-bincontent[NbinsY*j])>fabs(bincontent[NbinsY*j]-bincontent_down[NbinsY*j])){
            max = fabs(bincontent_up[NbinsY*j]-bincontent[NbinsY*j]);
         }
         else {
            max = fabs(bincontent[NbinsY*j]-bincontent_down[NbinsY*j]);
         }

         if(bincontent[NbinsY*j]>0) uncertainty[NbinsY*j] = max/bincontent[NbinsY*j];
         else uncertainty[NbinsY*j] =0;
         h_uncertainty->SetBinContent(NbinsY*j+1,uncertainty[NbinsY*j]);       

   }

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

}

TH1D * get_systematic_uncertainty_1D(TString which_region, TString outdir, TString which_sample, TString uncertainty_hist_name, TString infilename, TString var_name, double lumi){

   TFile*input = new TFile (infilename);
   TH1D * h_center   = (TH1D*)input->Get("hist_"+var_name+"_");
   TH1D * h_up       = (TH1D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_up");
   TH1D * h_down     = (TH1D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_down");

   h_center->Scale(lumi);
   h_up->Scale(lumi);
   h_down->Scale(lumi);

   h_center->SetLineColor(kBlack);
   h_up->SetLineColor(kBlue);
   h_down->SetLineColor(kRed);

   h_center->SetStats(kFALSE);
   h_up->SetStats(kFALSE);
   h_down->SetStats(kFALSE);

   int NbinsX = h_center->GetNbinsX();
   int NbinsY = h_center->GetNbinsY();

   int Nbins = NbinsX*NbinsY;
   TH1D * h_uncertainty = new TH1D("h", "h", Nbins, 0, Nbins);

   double uncertainty[NbinsX*NbinsY];
   double bincontent[NbinsX*NbinsY],bincontent_up[NbinsX*NbinsY],bincontent_down[NbinsX*NbinsY];

   for(int j=0;j<NbinsX;j++){
      for(int k=0;k<NbinsY;k++){
         bincontent[NbinsY*j+k] = h_center->GetBinContent(j+1,k+1);
         bincontent_up[NbinsY*j+k] = h_up->GetBinContent(j+1,k+1);
         bincontent_down[NbinsY*j+k] = h_down->GetBinContent(j+1,k+1);

         if(bincontent[NbinsY*j+k]>0) uncertainty[NbinsY*j+k] = fabs(bincontent_up[NbinsY*j+k] - bincontent_down[NbinsY*j+k])/2/bincontent[NbinsY*j+k];
         else uncertainty[NbinsY*j+k] =0;
         h_uncertainty->SetBinContent(NbinsY*j+k+1,uncertainty[NbinsY*j+k]);
      }
   }


   TCanvas * c1 = new TCanvas(uncertainty_hist_name,uncertainty_hist_name,900,900);

   c1->cd();
   h_up->Draw("hist");
   h_center->Draw("hist same");
   h_down->Draw("hist same");

   TLegend* leg3 = new TLegend(0.7,0.6,0.88,0.89);
   leg3->AddEntry(h_up,     "up");
   leg3->AddEntry(h_center, "center");
   leg3->AddEntry(h_down,   "down");

   double maximum       = 1.3 * h_up->GetMaximum();
   h_up->SetMaximum(maximum);
   leg3->Draw();

   c1->SaveAs(outdir+"/graph/"+which_sample+"_"+which_region+"_"+uncertainty_hist_name+".png");


   return h_uncertainty;
   input->Close();


}





TH1D * get_systematic_jecr_2D(TString which_region, TString outdir, TString which_sample, TString uncertainty_hist_name, TString infilename, TString var_name, double lumi ){
   TFile*input = new TFile (infilename);
   TH2D * h_center   = (TH2D*)input->Get("hist_"+var_name+"_");
   TH2D * h_up       = (TH2D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_up");
   TH2D * h_down     = (TH2D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_down");

   h_center->Scale(lumi);
   h_up->Scale(lumi);
   h_down->Scale(lumi);

   h_center->SetLineColor(kBlack);
   h_up->SetLineColor(kBlue);
   h_down->SetLineColor(kRed);

   h_center->SetStats(kFALSE);
   h_up->SetStats(kFALSE);
   h_down->SetStats(kFALSE);

   int NbinsX = h_center->GetNbinsX();
   int NbinsY = h_center->GetNbinsY();

   int Nbins = NbinsX*NbinsY;
   TH1D * h_uncertainty = new TH1D("h", "h", Nbins, 0, Nbins);

   double uncertainty[NbinsX*NbinsY];
   double bincontent[NbinsX*NbinsY],bincontent_up[NbinsX*NbinsY],bincontent_down[NbinsX*NbinsY];

   for(int j=0;j<NbinsX;j++){
      for(int k=0;k<NbinsY;k++){
         bincontent[NbinsY*j+k] = h_center->GetBinContent(j+1,k+1);
         bincontent_up[NbinsY*j+k] = h_up->GetBinContent(j+1,k+1);
         bincontent_down[NbinsY*j+k] = h_down->GetBinContent(j+1,k+1);
         double max;
         if(fabs(bincontent_up[NbinsY*j+k]-bincontent[NbinsY*j+k])>fabs(bincontent[NbinsY*j+k]-bincontent_down[NbinsY*j+k])){
            max = fabs(bincontent_up[NbinsY*j+k]-bincontent[NbinsY*j+k]);
         }
         else {
            max = fabs(bincontent[NbinsY*j+k]-bincontent_down[NbinsY*j+k]);
         }

         if(bincontent[NbinsY*j+k]>0) uncertainty[NbinsY*j+k] = max/bincontent[NbinsY*j+k];
         else uncertainty[NbinsY*j+k] =0;
         h_uncertainty->SetBinContent(NbinsY*j+k+1,uncertainty[NbinsY*j+k]);       
      }
   }

   TCanvas * c1 = new TCanvas(uncertainty_hist_name,uncertainty_hist_name,900,900);

   c1->cd();
   h_up->Draw("hist");
   h_center->Draw("hist same");
   h_down->Draw("hist same");

   TLegend* leg3 = new TLegend(0.7,0.6,0.88,0.89);
   leg3->AddEntry(h_up,     "up");
   leg3->AddEntry(h_center, "center");
   leg3->AddEntry(h_down,   "down");

   double maximum       = 1.3 * h_up->GetMaximum();
   h_up->SetMaximum(maximum);
   leg3->Draw();

   c1->SaveAs(outdir+"/graph/"+which_sample+"_"+which_region+"_"+uncertainty_hist_name+".png");


   return h_uncertainty;
   input->Close();

}

TH1D * get_systematic_uncertainty_2D(TString which_region, TString outdir, TString which_sample, TString uncertainty_hist_name, TString infilename, TString var_name, double lumi){

   TFile*input = new TFile (infilename);
   TH2D * h_center   = (TH2D*)input->Get("hist_"+var_name+"_");
   TH2D * h_up       = (TH2D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_up");
   TH2D * h_down     = (TH2D*)input->Get("hist_"+var_name+"_"+uncertainty_hist_name+"_down");

   h_center->Scale(lumi);
   h_up->Scale(lumi);
   h_down->Scale(lumi);

   h_center->SetLineColor(kBlack);
   h_up->SetLineColor(kBlue);
   h_down->SetLineColor(kRed);

   h_center->SetStats(kFALSE);
   h_up->SetStats(kFALSE);
   h_down->SetStats(kFALSE);

   int NbinsX = h_center->GetNbinsX();
   int NbinsY = h_center->GetNbinsY();

   int Nbins = NbinsX*NbinsY;
   TH1D * h_uncertainty = new TH1D("h", "h", Nbins, 0, Nbins);

   double uncertainty[NbinsX*NbinsY];
   double bincontent[NbinsX*NbinsY],bincontent_up[NbinsX*NbinsY],bincontent_down[NbinsX*NbinsY];

   for(int j=0;j<NbinsX;j++){
      for(int k=0;k<NbinsY;k++){
         bincontent[NbinsY*j+k] = h_center->GetBinContent(j+1,k+1);
         bincontent_up[NbinsY*j+k] = h_up->GetBinContent(j+1,k+1);
         bincontent_down[NbinsY*j+k] = h_down->GetBinContent(j+1,k+1);

         if(bincontent[NbinsY*j+k]>0) uncertainty[NbinsY*j+k] = fabs(bincontent_up[NbinsY*j+k] - bincontent_down[NbinsY*j+k])/2/bincontent[NbinsY*j+k];
         else uncertainty[NbinsY*j+k] =0;
         h_uncertainty->SetBinContent(NbinsY*j+k+1,uncertainty[NbinsY*j+k]);
      }
   }


   TCanvas * c1 = new TCanvas(uncertainty_hist_name,uncertainty_hist_name,900,900);

   c1->cd();
   h_up->Draw("hist");
   h_center->Draw("hist same");
   h_down->Draw("hist same");

   TLegend* leg3 = new TLegend(0.7,0.6,0.88,0.89);
   leg3->AddEntry(h_up,     "up");
   leg3->AddEntry(h_center, "center");
   leg3->AddEntry(h_down,   "down");

   double maximum       = 1.3 * h_up->GetMaximum();
   h_up->SetMaximum(maximum);
   leg3->Draw();

   c1->SaveAs(outdir+"/graph/"+which_sample+"_"+which_region+"_"+uncertainty_hist_name+".png");

   return h_uncertainty;
   input->Close();


}

