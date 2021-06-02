#!/usr/bin/env python
import sys
import os
import re
import ROOT
from ROOT import gROOT, TCanvas, TPad, TFile, TH1, TH2D, TF1, TLatex, TMath, TROOT, TTree, TString, TH2, TStyle, TLegend, THStack

indir                = sys.argv[1]
outdir               = sys.argv[2]
which_year           = sys.argv[3]
#which_type           = sys.argv[4]
which_region         = sys.argv[4]
which_channel        = sys.argv[5]
barrel_or_endcap     = sys.argv[6]
#which_btag_workpoint = sys.argv[7]

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


#genbins = 0

def print_uncer(which_sample, which_type,hist_name):
    #print (which_sample + ' ' + which_year + ' ' + which_region + ' ' + which_channel + ' ' + barrel_or_endcap + ' ' + hist_name + ' : ')
    infilename= indir + "/" + which_year + "_" + which_channel +  "_" + which_type + "_" + which_region + "_"+barrel_or_endcap+"_" + which_sample + ".root"

    f_xxx = TFile.Open(infilename)
    h_xxx   = f_xxx.Get("hist_")
    if which_type == 'mc':
        h_xxx.Scale(lumi)
    yields = round(h_xxx.GetSum(), 2)
    return yields

sample_list = ['WGJJ', 'WGJets', 'TTG', 'ZG', 'ST_s', 'ST_t', 'ST_tbar', 'ST_tW', 'ST_tbarW', 'WW', 'WZ', 'ZZ', 'fakephoton', 'doublefake', 'fakelepton']
sample_type = ['mc', 'mc', 'mc', 'mc', 'mc', 'mc', 'mc', 'mc', 'mc', 'mc', 'mc', 'mc', 'data', 'data', 'data']
#sample_list_data = ['fakephoton', 'doublefake']
all_yields = []
#for i in range(1):
for i in range(len(sample_list)):
    all_yields.append(print_uncer(sample_list[i], sample_type[i], 'hist_'))
all_yields[-1] = all_yields[-1] - all_yields[-2]
all_yields[-3] = all_yields[-3] - all_yields[-2]

print str(which_year) + ',',
for i in range(len(sample_list)):
    #print str(sample_list[i]) + ' : ' + str(all_yields[i])
    print str(sample_list[i]) + ',',
print 'total predict'

print str(which_region) + ' '+ str(which_channel) + ' ' + str(barrel_or_endcap) + ',',
for i in range(len(sample_list)):
    #print str(sample_list[i]) + ' : ' + str(all_yields[i])
    print str(all_yields[i]) + ',',
#print 'total predict : ' + 
print str(sum(all_yields))

