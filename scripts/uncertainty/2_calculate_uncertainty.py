#!/usr/bin/env python
import sys
import os
import re
import ROOT
from ROOT import gROOT, TCanvas, TPad, TFile, TH1, TH2D, TF1, TLatex, TMath, TROOT, TTree, TString, TH2, TStyle, TLegend, THStack
from uncer_package.uncertainty_jecr import *
from uncer_package.uncertainty_systematic import *

indir                = sys.argv[1]
outdir               = sys.argv[2]
which_year           = sys.argv[3]
which_type           = sys.argv[4]
which_region         = sys.argv[5]
which_channel        = sys.argv[6]
barrel_or_endcap     = sys.argv[7]
which_btag_workpoint = sys.argv[8]
var_name             = sys.argv[9]

os.system("mkdir -p " + outdir)
py_uncer_dir = outdir + "/" + which_region + "_" + which_channel + "_" + barrel_or_endcap
os.system("mkdir -p " + py_uncer_dir)
graph_dir = outdir + "/" + which_region + "_" + which_channel + "_" + barrel_or_endcap + "/graph"
os.system("mkdir -p " + graph_dir)

lumi =0
if which_year == "2016":
    lumi = 35.92

if which_year == "2017":
    lumi = 41.50

if which_year == "2018":
    lumi = 59.74

uncer_list_data = ['fakephoton'] 
uncer_list_mc = ['pileup', 'L1', 'photon_ID', 'electron_ID', 'electron_Reco', 'electron_HLT', 'muon_ID', 'muon_iso', 'muon_HLT', 'btag', 'pujet', 'pujet_mistag']
if which_type == 'mc':
    uncer_list = uncer_list_mc
else :
    uncer_list = uncer_list_data

def print_uncer(which_sample):
    infilename= indir + "/" + which_year + "_" + which_channel +  "_" + which_type + "_" + which_region + "_"+barrel_or_endcap+"_" +  which_btag_workpoint + "_btag_" + which_sample + "_uncertainty.root"
    f = open(py_uncer_dir + "/" + which_sample + ".py", "w")

    for i in range(len(uncer_list)):
        tmp= get_systematic_1D(which_region, graph_dir, which_sample, uncer_list[i], infilename, var_name, lumi)
        print(uncer_list[i],tmp)
        f.write(which_sample + "_" + uncer_list[i] + " = [")
        for j in range(len(tmp)):
            if j < len(tmp) -1 : f.write(str(1+tmp[j]) + ', ')
            if j == len(tmp) -1 : f.write(str(1+tmp[j]) + '] ' + '\n')
            
    tmp1= get_jecr_1D(which_region, graph_dir, which_sample, 'JEC', infilename, var_name, lumi)
    print('JEC', tmp1)
    f.write(which_sample + "_JEC = [")
    for k in range(len(tmp1)):
        if k < len(tmp1) -1 : f.write(str(1+tmp1[k]) + ', ')
        if k == len(tmp1) -1 : f.write(str(1+tmp1[k]) + '] ' + '\n')

    tmp2= get_jecr_1D(which_region, graph_dir, which_sample, 'JER', infilename, var_name, lumi)
    print('JER', tmp2)
    f.write(which_sample + "_JER = [")
    for k2 in range(len(tmp2)):
        if k2 < len(tmp2) -1 : f.write(str(1+tmp2[k2]) + ', ')
        if k2 == len(tmp2) -1 : f.write(str(1+tmp2[k2]) + '] ' + '\n')

sample_list_mc = ['WGJJ', 'WGJets', 'TTG', 'ZG', 'ST_s', 'ST_t', 'ST_tbar', 'ST_tW', 'ST_tbarW', 'WW', 'WZ', 'ZZ']
sample_list_data = ['fakephoton']

if which_type == 'mc': 
    sample_list = sample_list_mc
else :
    sample_list = sample_list_data
#for i in range(1):
for i in range(len(sample_list)):
    print_uncer(sample_list[i])
