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

TH1D * get_systematic_jecr_in_1D(TString which_region, TString outdir, TString which_sample, TString uncertainty_hist_name, TString infilename, TString var_name, double lumi ){
cout<<"ok0"<<endl;
   TFile*input = new TFile (infilename);
cout<<"ok0"<<endl;
   TH1D * h_center   = (TH1D*)input->Get("hist_in_");
   TH1D * h_up       = (TH1D*)input->Get("hist_in_"+uncertainty_hist_name+"_up");
   TH1D * h_down     = (TH1D*)input->Get("hist_in_"+uncertainty_hist_name+"_down");
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

   TCanvas * c1 = new TCanvas(uncertainty_hist_name,uncertainty_hist_name,900,600);
	TPad*    fPads1 = new TPad("pad1", "", 0.00, 0.4, 0.99, 0.99);
	TPad*    fPads2 = new TPad("pad2", "", 0.00, 0.00, 0.99, 0.4);
	fPads1->SetBottomMargin(0);
	fPads2->SetTopMargin(0);
	fPads2->SetBottomMargin(0.4);
	fPads1->Draw();
	fPads2->Draw();
	fPads1->cd();
    fPads2->SetGridy();
    fPads1->SetGridx();
   //c1->cd();
   h_up->SetTitle(uncertainty_hist_name);
   h_up->SetLineWidth(2);
   h_center->SetLineWidth(2);
   h_down->SetLineWidth(2);

   h_up->Draw("hist");
   h_center->Draw("hist same");
   h_down->Draw("hist same");

   TLegend* leg3 = new TLegend(0.7,0.7,0.9,0.9);
   leg3->AddEntry(h_up,     "up");
   leg3->AddEntry(h_center, "center");
   leg3->AddEntry(h_down,   "down");

   double maximum       = 1.2 * h_up->GetMaximum();
   //h_up->SetMaximum(maximum);
   leg3->Draw();
	fPads1->Update();
	fPads2->cd();

	TH1D*nominal=(TH1D*)h_center->Clone("nominal");
	TH1D*nomNoErr=(TH1D*)nominal->Clone("nomNoErr");
	for (int i = 1; i<= nomNoErr->GetNbinsX(); ++i){nomNoErr->SetBinError(i,0);}
	TH1D*tmp_h_up=(TH1D*)h_up->Clone();
	TH1D*tmp_h_down=(TH1D*)h_down->Clone();
   nominal->SetTitle("");

	tmp_h_up->Divide(nominal);
	tmp_h_down->Divide(nominal);
	nominal->Divide(nomNoErr);
	nominal->SetFillStyle(3001);
	nominal->SetFillColor(16);
        nominal->GetYaxis()->SetLabelSize(0.1);
        nominal->GetYaxis()->SetNdivisions(404);
        nominal->GetXaxis()->SetTitle(var_name+" [GeV]");
        nominal->GetXaxis()->SetLabelSize(0.1);
        nominal->GetXaxis()->SetTitleFont(12);
        nominal->GetXaxis()->SetTitleSize(0.2);
cout<<tmp_h_down->GetMinimum()-0.1<<" "<<tmp_h_up->GetMaximum()+0.05<<endl;
	nominal->GetYaxis()->SetRangeUser(tmp_h_down->GetMinimum()-0.1,tmp_h_up->GetMaximum()+0.05);
	nominal->Draw("EP");
	tmp_h_up->Draw("same hist ][");
	tmp_h_down->Draw("same hist ][");
	fPads2->Update();
   c1->SaveAs(outdir+"/graph/"+which_sample+"_"+which_region+"_"+uncertainty_hist_name+".png");

   return h_uncertainty;
   input->Close();

}

TH1D * get_systematic_uncertainty_in_1D(TString which_region, TString outdir, TString which_sample, TString uncertainty_hist_name, TString infilename, TString var_name, double lumi){

   TFile*input = new TFile (infilename);
   TH1D * h_center   = (TH1D*)input->Get("hist_in_");
   TH1D * h_up       = (TH1D*)input->Get("hist_in_"+uncertainty_hist_name+"_up");
   TH1D * h_down     = (TH1D*)input->Get("hist_in_"+uncertainty_hist_name+"_down");

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
    TPad*    fPads1 = new TPad("pad1", "", 0.00, 0.4, 0.99, 0.99);
    TPad*    fPads2 = new TPad("pad2", "", 0.00, 0.00, 0.99, 0.4);
    fPads1->SetBottomMargin(0);
    fPads2->SetTopMargin(0);
    fPads2->SetBottomMargin(0.4);
    fPads1->Draw();
    fPads2->Draw();
    fPads1->cd();
    fPads2->SetGridy();
    fPads1->SetGridx();
   //c1->cd();
   h_up->Draw("hist");
   h_center->Draw("hist same");
   h_down->Draw("hist same");
   h_up->SetLineWidth(2);
   h_center->SetLineWidth(2);
   h_down->SetLineWidth(2);

   TLegend* leg3 = new TLegend(0.7,0.7,0.9,0.9);
   leg3->AddEntry(h_up,     "up");
   leg3->AddEntry(h_center, "center");
   leg3->AddEntry(h_down,   "down");

   double maximum       = 1.3 * h_up->GetMaximum();
   //h_up->SetMaximum(maximum);
   leg3->Draw();


    fPads1->Update();
    fPads2->cd();

    TH1D*nominal=(TH1D*)h_center->Clone("nominal");
    TH1D*nomNoErr=(TH1D*)nominal->Clone("nomNoErr");
    for (int i = 1; i<= nomNoErr->GetNbinsX(); ++i){nomNoErr->SetBinError(i,0);}
    TH1D*tmp_h_up=(TH1D*)h_up->Clone();
    TH1D*tmp_h_down=(TH1D*)h_down->Clone();
   nominal->SetTitle("");

    tmp_h_up->Divide(nominal);
    tmp_h_down->Divide(nominal);
    nominal->Divide(nomNoErr);
    nominal->SetFillStyle(3001);
    nominal->SetFillColor(16);
        nominal->GetYaxis()->SetLabelSize(0.1);
        nominal->GetYaxis()->SetNdivisions(404);
        nominal->GetXaxis()->SetTitle(var_name+" [GeV]");
        nominal->GetXaxis()->SetLabelSize(0.1);
        nominal->GetXaxis()->SetTitleFont(12);
        nominal->GetXaxis()->SetTitleSize(0.2);
cout<<tmp_h_down->GetMinimum()-0.1<<" "<<tmp_h_up->GetMaximum()+0.05<<endl;
    nominal->GetYaxis()->SetRangeUser(tmp_h_down->GetMinimum()-0.1,tmp_h_up->GetMaximum()+0.05);
    nominal->Draw("EP");
    tmp_h_up->Draw("same hist ][");
    tmp_h_down->Draw("same hist ][");
    fPads2->Update();

   c1->SaveAs(outdir+"/graph/"+which_sample+"_"+which_region+"_"+uncertainty_hist_name+".png");


   return h_uncertainty;
   input->Close();


}

