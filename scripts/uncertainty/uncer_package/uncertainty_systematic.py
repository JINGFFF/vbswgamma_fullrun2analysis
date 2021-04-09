#!/usr/bin/env python
#import sys
#import os
#import re
#from uncertainty_unfold import *
import ROOT
from ROOT import gROOT, TCanvas, TPad, TFile, TH1, TH2D, TF1, TLatex, TMath, TROOT, TTree, TString, TH2, TStyle, TLegend, THStack

def get_systematic_1D(which_region, outdir, which_sample, uncertainty_hist_name, infilename, var_name, lumi ):
    f_in = TFile.Open(infilename)
    h_center   = f_in.Get("hist_")
    h_up       = f_in.Get("hist_"+uncertainty_hist_name+"_up")
    h_down     = f_in.Get("hist_"+uncertainty_hist_name+"_down")
    h_center.Scale(lumi)
    #h_center.Print("all")

    h_up.Scale(lumi)
    h_down.Scale(lumi)

    h_center.SetLineColor(1)
    h_up.SetLineColor(4)
    h_down.SetLineColor(2)

    h_center.SetStats(0)
    h_up.SetStats(0)
    h_down.SetStats(0)

    NbinsX = h_center.GetNbinsX()
    NbinsY = h_center.GetNbinsY()

    Nbins = NbinsX*NbinsY
    h_uncertainty = []

    uncertainty = 0
    for j in range(NbinsX) :
        uncertainty = 0
        if(h_center.GetBinContent(j+1) > 0) :
            uncertainty = abs(h_up.GetBinContent(j+1) - h_down.GetBinContent(j+1))/(2*h_center.GetBinContent(j+1))
        h_uncertainty.append(uncertainty)       


    c1 = TCanvas(uncertainty_hist_name,uncertainty_hist_name,900,600)
    fPads1 = TPad("pad1", "", 0.00, 0.4, 0.99, 0.99)
    fPads2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.4)
    fPads1.SetBottomMargin(0)
    fPads2.SetTopMargin(0)
    fPads2.SetBottomMargin(0.4)
    c1.cd()
    fPads1.Draw()
    fPads2.Draw()
    fPads1.cd()
    fPads2.SetGridy()
    fPads1.SetGridx()
  
    h_up.SetTitle(uncertainty_hist_name)
    h_up.SetLineWidth(2)
    h_center.SetLineWidth(2)
    h_down.SetLineWidth(2)

    h_up.Draw("hist")
    h_center.Draw("hist same")
    h_down.Draw("hist same")

    leg3 = TLegend(0.7,0.7,0.9,0.9)
    leg3.AddEntry(h_up,     "up")
    leg3.AddEntry(h_center, "center")
    leg3.AddEntry(h_down,   "down")

    maximum = 1.2 * h_up.GetMaximum()
    leg3.Draw()
    fPads1.Update()
    fPads2.cd()

    nominal  = h_center.Clone("nominal")
    nomNoErr = nominal.Clone("nomNoErr")
    for i in range(nomNoErr.GetNbinsX()) :
        nomNoErr.SetBinError(i+1,0)
    tmp_h_up   = h_up.Clone()
    tmp_h_down = h_down.Clone()
    nominal.SetTitle("")

    tmp_h_up.Divide(nominal)
    tmp_h_down.Divide(nominal)
    nominal.Divide(nomNoErr)
    nominal.SetFillStyle(3001)
    nominal.SetFillColor(16)
    nominal.GetYaxis().SetLabelSize(0.1)
    nominal.GetYaxis().SetNdivisions(404)
    nominal.GetXaxis().SetTitle(var_name+" [GeV]")
    nominal.GetXaxis().SetLabelSize(0.1)
    nominal.GetXaxis().SetTitleFont(12)
    nominal.GetXaxis().SetTitleSize(0.2)
    #cout<<tmp_h_down->GetMinimum()-0.1<<" "<<tmp_h_up->GetMaximum()+0.05<<endl
    #nominal.GetYaxis().SetRangeUser(0.0,tmp_h_up.GetMaximum()+0.05)
    nominal.GetYaxis().SetRangeUser(tmp_h_down.GetMinimum() - 0.1,tmp_h_up.GetMaximum()+0.05)

    nominal.Draw("EP")
    tmp_h_up.Draw("same hist ][")
    tmp_h_down.Draw("same hist ][")
    fPads2.Update()
    #c1.SaveAs(outdir+"/graph/"+which_sample+"_"+which_region+"_"+uncertainty_hist_name+".png")
    c1.SaveAs(outdir + "/" + which_sample + "_" + uncertainty_hist_name + ".png")
    c1.Close()
    return h_uncertainty
    f_in.Close()

