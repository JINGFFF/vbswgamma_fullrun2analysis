#!/usr/bin/env python
import sys
import os
import re
import ROOT
from ROOT import gROOT, TCanvas, TPad, TFile, TH1D, TH2D, TF1, TLatex, TMath, TROOT, TTree, TString, TH2, TStyle, TLegend, THStack
from array import array

indir                = sys.argv[1]
outdir               = sys.argv[2]
which_year           = sys.argv[3]
#which_type           = sys.argv[4]
which_region         = sys.argv[4]
#which_channel        = sys.argv[5]
#barrel_or_endcap     = sys.argv[6]
#fit_para_dir         = sys.argv[7]
#which_btag_workpoint = sys.argv[8]
#var_name             = sys.argv[9]

os.system("mkdir -p " + outdir)

lumi =0
if which_year == "2016":
    lumi = 35.92

if which_year == "2017":
    lumi = 41.50

if which_year == "2018":
    lumi = 59.74


def read_hist(indir, which_year, which_channel, which_type, which_region, barrel_or_endcap, which_sample) :
    infilename= indir + "/" + which_year + "_" + which_channel +  "_" + which_type + "_" + which_region + "_"+barrel_or_endcap+"_medium_btag_" + which_sample + "_uncertainty.root"
    f_in = TFile.Open(infilename)
    hist       = f_in.Get("hist_")
    #hist.Print()
    if which_type == 'mc':
        hist.Scale(lumi)
    return hist.GetSum()

data_name = ''
#if which_channel == 'muon':
#    data_name = 'SingleMuon'
#if which_channel == 'electron':
#    data_name = 'SingleElectron'

setting_for_muon_h = [
['WGJJ',     'mc',         2, 'EWK WG'],
['WGJets',   'mc',         7, 'QCD WG'],
['ZG',       'mc',         8, 'QCD ZG'],
['WW',       'mc',        42, 'WW'],
['WZ',       'mc',        42, 'WZ'],
['ZZ',       'mc',        42, 'ZZ'],
['ST_s',     'mc',         9, 'ST_s'],
['ST_t',     'mc',         9, 'ST_t'],
['ST_tbar',  'mc',         9, 'ST_tbar'],
['ST_tW',    'mc',         9, 'ST_tW'],
['ST_tbarW', 'mc',         9, 'ST_tbarW'],
['TTG',      'mc',         6, 'TTG'],
#[data_name,  'data',       1],
['SingleMuon',  'fakelepton', 5, 'fake photon'],
['SingleMuon',  'fakephoton',15, 'fake lepton'],
['SingleMuon',  'doublefake',30, 'double fake'],
]

setting_for_electron_h = [
['WGJJ',     'mc',         2, 'EWK WG'],
['WGJets',   'mc',         7, 'QCD WG'],
['ZG',       'mc',         8, 'QCD ZG'],
['WW',       'mc',        42, 'WW'],
['WZ',       'mc',        42, 'WZ'],
['ZZ',       'mc',        42, 'ZZ'],
['ST_s',     'mc',         9, 'ST_s'],
['ST_t',     'mc',         9, 'ST_t'],
['ST_tbar',  'mc',         9, 'ST_tbar'],
['ST_tW',    'mc',         9, 'ST_tW'],
['ST_tbarW', 'mc',         9, 'ST_tbarW'],
['TTG',      'mc',         6, 'TTG'],
#[data_name,  'data',       1],
['SingleElectron',  'fakelepton', 5, 'fake photon'],
['SingleElectron',  'fakephoton',15, 'fake lepton'],
['SingleElectron',  'doublefake',30, 'double fake'],
]

content_m_b, content_m_e, content_e_b, content_e_e, = [], [], [], []
for i in range(15):
    content_m_b.append(read_hist(indir, which_year, 'muon', setting_for_muon_h[i][1], which_region, 'barrel', setting_for_muon_h[i][0]))
    content_m_e.append(read_hist(indir, which_year, 'muon', setting_for_muon_h[i][1], which_region, 'endcap', setting_for_muon_h[i][0]))
    content_e_b.append(read_hist(indir, which_year, 'electron', setting_for_electron_h[i][1], which_region, 'barrel', setting_for_electron_h[i][0]))
    content_e_e.append(read_hist(indir, which_year, 'electron', setting_for_electron_h[i][1], which_region, 'endcap', setting_for_electron_h[i][0]))

#str(format(float(uncer_endcap[i])*100, '.2f'))
for i in range(15):
    print str(setting_for_electron_h[i][3]) + ' & $ ' + str(format(float(content_e_b[i]), '.2f')) + ' $  & $ ' + str(format(float(content_e_e[i]), '.2f')) + ' $ & $ ' + str(format(float(content_m_b[i]), '.2f')) + ' $  & $ ' + str(format(float(content_m_e[i]), '.2f')) + ' $  \\\\'

#print float(sum(content_e_b),'.2f')
#print float(1.23456,'.2f')

#print str(format(float(sum(content_e_b), '.2f')))
print 'Total predicted' + ' & $ ' + str(format(sum(content_e_b), '.2f')) + ' $  & $ ' + str(format(sum(content_e_e), '.2f')) + ' $ & $ ' + str(format(sum(content_m_b), '.2f')) + ' $  & $ ' + str(format(sum(content_m_e), '.2f')) + ' $  \\\\'

