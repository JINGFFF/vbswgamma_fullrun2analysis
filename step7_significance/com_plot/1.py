import os
import re
import ROOT
from ROOT import gROOT, TGraph, TCanvas, TPad, TFile, TH1D, TH2D, TF1, TLatex, TMath, TROOT, TTree, TString, TH2, TStyle, TLegend, THStack
from array import array

x1 = array('d',(1, 1))
y1 = array('d',(0, 10))
g = TGraph(2, x1, y1)
g.Draw("AC")
