#!/usr/bin/env python
import sys
import os
import re
#from uncertainty_unfold import *
import ROOT
from ROOT import gROOT, THStack, TH1D, TList, TFile, TH2D

indir = sys.argv[1]
outdir = sys.argv[2]
region = sys.argv[3]
bORe = sys.argv[4]
year = sys.argv[5]
channel = sys.argv[6]
channel_name = ''
if not os.path.exists(outdir):
    os.makedirs(outdir)
if region == 'signal':
    if channel == 'muon':
        if bORe == 'barrel':
            from uncer_signal_muon_barrel import *
        if bORe == 'endcap':
            from uncer_signal_muon_endcap import *
        channel_name = 'SingleMuon'
    if channel == 'electron':
        if bORe == 'barrel':
            from uncer_signal_electron_barrel import *
        if bORe == 'endcap':
            from uncer_signal_electron_endcap import *
        channel_name = 'SingleElectron'

if region  == 'control':
    if channel == 'muon':
        if bORe == 'barrel':
            from uncer_control_muon_barrel import *
        if bORe == 'endcap':
            from uncer_control_muon_endcap import *
        channel_name = 'SingleMuon'
    if channel == 'electron':
        if bORe == 'barrel':
            from uncer_control_electron_barrel import *
        if bORe == 'endcap':
            from uncer_control_electron_endcap import *
        channel_name = 'SingleElectron'

if region  == 'aqgc':
    if channel == 'muon':
        if bORe == 'barrel':
            from uncer_aqgc_muon_barrel import *
        if bORe == 'endcap':
            from uncer_aqgc_muon_endcap import *
        if bORe == 'all':
            from uncer_aqgc_muon_all import *
        channel_name = 'SingleMuon'
    if channel == 'electron':
        if bORe == 'barrel':
            from uncer_aqgc_electron_barrel import *
        if bORe == 'endcap':
            from uncer_aqgc_electron_endcap import *
        if bORe == 'all':
            from uncer_aqgc_electron_all import *
        channel_name = 'SingleElectron'

#print(ST_s_photon_ID[(i-1)*3 + j - 1])
print ('-----begin to transfer TH2D to txt for Higgs-combine tool----- \n')
histname = 'ptlep'
f_in_WGJJ = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" + bORe + "_medium_btag_WGJJ_uncertainty.root")
VBS = f_in_WGJJ.Get("hist_")

f_in_ST_s = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_ST_s_uncertainty.root")
#ST_s     =ROOT.TH2D()
#f_in_ST_s.GetObject("hist_2D_Mjj_detajj",ST_s)
ST_s = f_in_ST_s.Get("hist_")

f_in_ST_t = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_ST_t_uncertainty.root")
ST_t = f_in_ST_t.Get("hist_")

f_in_ST_tbar = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_ST_tbar_uncertainty.root")
ST_tbar = f_in_ST_tbar.Get("hist_")

f_in_ST_tW = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_ST_tW_uncertainty.root")
ST_tW = f_in_ST_tW.Get("hist_")

f_in_ST_tbarW = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_ST_tbarW_uncertainty.root")
ST_tbarW = f_in_ST_tbarW.Get("hist_")

f_in_TTG = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_TTG_uncertainty.root")
TTG = f_in_TTG.Get("hist_")

f_in_WGJets = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_WGJets_uncertainty.root")
WGJets = f_in_WGJets.Get("hist_")

f_in_WW = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_WW_uncertainty.root")
WW = f_in_WW.Get("hist_")

f_in_WZ = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_WZ_uncertainty.root")
WZ = f_in_WZ.Get("hist_")

f_in_ZZ = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_" +bORe + "_medium_btag_ZZ_uncertainty.root")
ZZ = f_in_ZZ.Get("hist_")

f_in_ZG = TFile.Open(indir + "/scaled_"+year+"_"+channel+"_mc_" + region + "_"+ bORe+ "_medium_btag_ZG_uncertainty.root")
ZG = f_in_ZG.Get("hist_")

#f_in_data = TFile.Open(indir + "/"+year+"_"+channel+"_data_"+ region + "_" + +bORe + "_medium_btag_"+channel_name+"_uncertainty.root")
#f_in_data = TFile.Open(indir + "/2016_muon_data_signal_barrel_medium_btag_SingleMuon_uncertainty.root")
f_in_data = TFile.Open(indir + "/"+year+"_"+channel+"_data_" + region + "_" + bORe + "_medium_btag_"+channel_name+"_uncertainty.root")
data = f_in_data.Get("hist_")

f_in_doublefake = TFile.Open(indir + "/"+year+"_"+channel+"_doublefake_" + region + "_" + bORe + "_medium_btag_"+channel_name+"_uncertainty.root")
doublefake = f_in_doublefake.Get("hist_")

f_in_fakephoton = TFile.Open(indir + "/"+year+"_"+channel+"_fakephoton_" + region + "_" + bORe + "_medium_btag_"+channel_name+"_uncertainty.root")
fakephoton = f_in_fakephoton.Get("hist_")

f_in_fakelepton = TFile.Open(indir + "/"+year+"_"+channel+"_fakelepton_" + region + "_" + bORe + "_medium_btag_"+channel_name+"_uncertainty.root")
fakelepton = f_in_fakelepton.Get("hist_")

binNum = VBS.GetNbinsX();
print(binNum)
print ('>>>>begin to read bin content to the txt file>>>>')

for i in range(1,VBS.GetNbinsX()+1):
    f = open('%s/%s_%s_%s_%s_bin_%d.txt'%(outdir,'16',channel, region ,bORe, i-1),'w')
    f.write('imax 1   number of channels\n')
    f.write('jmax '+str(14)+'   number of processes-1\n')
    f.write('kmax 1  number of nuisance parameters (sources of systematical uncertainties)\n')
    f.write('------------\n')
    f.write('# we have just one channel, in which we observe 0 events\n')
    f.write('bin mubarrel\n')
    bin_content = ST_s.GetBinContent(i) + ST_t.GetBinContent(i) + ST_tbar.GetBinContent(i) + ST_tW.GetBinContent(i) + ST_tbarW.GetBinContent(i) + TTG.GetBinContent(i) + WW.GetBinContent(i) + WZ.GetBinContent(i) + ZZ.GetBinContent(i) + WGJets.GetBinContent(i) + ZG.GetBinContent(i)  + VBS.GetBinContent(i) + fakephoton.GetBinContent(i) + fakelepton.GetBinContent(i) - doublefake.GetBinContent(i)
    # bincontent of each precess
    ST_s_bincontent = ST_s.GetBinContent(i) if ST_s.GetBinContent(i)>0 else 0
    ST_t_bincontent = ST_t.GetBinContent(i) if ST_t.GetBinContent(i)>0 else 0
    ST_tbar_bincontent = ST_tbar.GetBinContent(i) if ST_tbar.GetBinContent(i)>0 else 0
    ST_tW_bincontent = ST_tW.GetBinContent(i) if ST_tW.GetBinContent(i)>0 else 0
    ST_tbarW_bincontent = ST_tbarW.GetBinContent(i) if ST_tbarW.GetBinContent(i)>0 else 0

    TTG_bincontent = TTG.GetBinContent(i) if TTG.GetBinContent(i)>0 else 0
    WW_bincontent = WW.GetBinContent(i) if WW.GetBinContent(i)>0 else 0
    WZ_bincontent = WZ.GetBinContent(i) if WZ.GetBinContent(i)>0 else 0
    ZZ_bincontent = ZZ.GetBinContent(i) if ZZ.GetBinContent(i)>0 else 0
    ZG_bincontent = ZG.GetBinContent(i) if ZG.GetBinContent(i)>0 else 0
    WGJets_bincontent = WGJets.GetBinContent(i) if WGJets.GetBinContent(i)>0 else 0
    #VBS_bincontent=[0 for ii in range(VBS.GetNbinsX())]
    #VBS_bincontent.append(1)
    VBS_bincontent = VBS.GetBinContent(i) if VBS.GetBinContent(i)>0 else 0

    doublefake_bincontent = doublefake.GetBinContent(i) if doublefake.GetBinContent(i)>0 else 0
    fakephoton_bincontent = fakephoton.GetBinContent(i) - doublefake_bincontent if fakephoton.GetBinContent(i)>0 else 0
    fakelepton_bincontent = fakelepton.GetBinContent(i) - doublefake_bincontent if fakelepton.GetBinContent(i)>0 else 0
    #doublefake_bincontent = doublefake.GetBinContent(i) if doublefake.GetBinContent(i)>0 else 0

    # bin error
    ST_s_binerror = ST_s.GetBinError(i)/ST_s_bincontent if ST_s_bincontent>0 else 0
    ST_s_binerror = ST_s_binerror if ST_s_binerror<1 else 1
    ST_s_binerror = ST_s_binerror+1

    ST_t_binerror = ST_t.GetBinError(i)/ST_t_bincontent if ST_t_bincontent>0 else 0
    ST_t_binerror = ST_t_binerror if ST_t_binerror<1 else 1
    ST_t_binerror = ST_t_binerror+1

    ST_tbar_binerror = ST_tbar.GetBinError(i)/ST_tbar_bincontent if ST_tbar_bincontent>0 else 0
    ST_tbar_binerror = ST_tbar_binerror if ST_tbar_binerror<1 else 1
    ST_tbar_binerror = ST_tbar_binerror+1

    ST_tW_binerror = ST_tW.GetBinError(i)/ST_tW_bincontent if ST_tW_bincontent>0 else 0
    ST_tW_binerror = ST_tW_binerror if ST_tW_binerror<1 else 1
    ST_tW_binerror = ST_tW_binerror+1

    ST_tbarW_binerror = ST_tbarW.GetBinError(i)/ST_tbarW_bincontent if ST_tbarW_bincontent>0 else 0
    ST_tbarW_binerror = ST_tbarW_binerror if ST_tbarW_binerror<1 else 1
    ST_tbarW_binerror = ST_tbarW_binerror+1

    TTG_binerror = TTG.GetBinError(i)/TTG_bincontent if TTG_bincontent>0 else 0
    TTG_binerror = TTG_binerror if TTG_binerror<1 else 1
    TTG_binerror = TTG_binerror+1

    WGJets_binerror = WGJets.GetBinError(i)/WGJets_bincontent if WGJets_bincontent>0 else 0
    WGJets_binerror = WGJets_binerror if WGJets_binerror<1 else 1
    WGJets_binerror = WGJets_binerror+1

    WW_binerror = WW.GetBinError(i)/WW_bincontent if WW_bincontent>0 else 0
    WW_binerror = WW_binerror if WW_binerror<1 else 1
    WW_binerror = WW_binerror+1

    WZ_binerror = WZ.GetBinError(i)/WZ_bincontent if WZ_bincontent>0 else 0
    WZ_binerror = WZ_binerror if WZ_binerror<1 else 1
    WZ_binerror = WZ_binerror+1

    ZZ_binerror = ZZ.GetBinError(i)/ZZ_bincontent if ZZ_bincontent>0 else 0
    ZZ_binerror = ZZ_binerror if ZZ_binerror<1 else 1
    ZZ_binerror = ZZ_binerror+1

    ZG_binerror = ZG.GetBinError(i)/ZG_bincontent if ZG_bincontent>0 else 0
    ZG_binerror = ZG_binerror if ZG_binerror<1 else 1
    ZG_binerror = ZG_binerror+1
    #print("VBS_binerror: ", VBS_binerror)
    VBS_binerror = VBS.GetBinError(i)/VBS_bincontent if VBS_bincontent>0 else 0
    VBS_binerror = VBS_binerror if VBS_binerror<1 else 1
    VBS_binerror = VBS_binerror+1

    f.write('observation %.2f\n'%0)
    f.write('------------\n')
    f.write('# now we list the expected events for signal and all backgrounds in that bin\n')
    f.write('# the second process line must have a positive number for backgrounds, and 0 for signal\n')
    f.write('# then we list the independent sources of uncertainties, and give their effect (syst. error)\n')
    f.write('# on each process and bin\n')
    f.write('bin')
    f.write('\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\tmubarrel\n')

    f.write('process')
    f.write('\tVBS\tWGJets\tST_s\tST_t\tST_tbar\tST_tW\tST_tbarW\tTTG\tWW\tWZ\tZZ\tZG\tfakephoton\tfakelepton\tdoublefake\n')

    f.write('process')
    f.write('\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\n')

    f.write('rate')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\n'%(VBS_bincontent, WGJets_bincontent, ST_s_bincontent, ST_t_bincontent, ST_tbar_bincontent, ST_tW_bincontent, ST_tbarW_bincontent, TTG_bincontent, WW_bincontent, WZ_bincontent, ZZ_bincontent, ZG_bincontent, fakephoton_bincontent, fakelepton_bincontent, doublefake_bincontent))


    f.write('------------\n')

    f.write('lumi\tlnN')
    f.write('\t1.025\t1.025\t1.025\t1.025\t1.025\t1.025\t1.025\t1.025\t1.025\t1.025\t1.025\t1.025\t-\t-\t-\t#lumi\n')

    #f.write('stat\tlnN')
    #for k in range(1,VBS.GetNbinsX()+1):
       #if k == i:
       #f.write('\t'+str(VBS_binerror[k-1]))
       #elif k != i :
        #   f.write('\t-')
    #f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(VBS_out_binerror, WGJets_binerror, ST_s_binerror, ST_t_binerror, ST_tbar_binerror, ST_tW_binerror, ST_tbarW_binerror, TTG_binerror, WW_binerror, WZ_binerror, ZZ_binerror, ZG_binerror))
'''
    f.write('WGJJ_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t'+str(VBS_binerror)+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('WGJets_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t'+str(WGJets_binerror)+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('ST_s_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t'+str(ST_s_binerror)+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('ST_t_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t'+str(ST_t_binerror)+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('ST_tbar_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t'+str(ST_tbar_binerror)+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('ST_tW_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t-\t'+str(ST_tW_binerror)+'\t-\t-\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('ST_tbarW_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t-\t-\t'+str(ST_tbarW_binerror)+'\t-\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('TTG_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t-\t-\t-\t'+str(TTG_binerror)+'\t-\t-\t-\t-\t-\t-\t-\n')

    f.write('WW_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t-\t-\t-\t-\t'+str(WW_binerror)+'\t-\t-\t-\t-\t-\t-\n')

    f.write('WZ_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t-\t-\t-\t-\t-\t'+str(WZ_binerror)+'\t-\t-\t-\t-\t-\n')

    f.write('ZZ_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t'+str(ZZ_binerror)+'\t-\t-\t-\t-\n')

    f.write('ZG_'+channel+'_'+bORe+'_stat_bin_'+ str(i) + "_"+year+'\tlnN')
    f.write('\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t'+str(ZG_binerror)+'\t-\t-\t-\n')

    f.write('photon_ID_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_photon_ID[i - 1], WGJets_photon_ID[i - 1], ST_s_photon_ID[i - 1], ST_t_photon_ID[i - 1], ST_tbar_photon_ID[i - 1], ST_tW_photon_ID[i - 1], ST_tbarW_photon_ID[i - 1], TTG_photon_ID[i - 1], WW_photon_ID[i - 1], WZ_photon_ID[i - 1], ZZ_photon_ID[i - 1], ZG_photon_ID[i - 1]))

    f.write('electron_ID_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_electron_ID[i - 1], WGJets_electron_ID[i - 1], ST_s_electron_ID[i - 1], ST_t_electron_ID[i - 1], ST_tbar_electron_ID[i - 1], ST_tW_electron_ID[i - 1], ST_tbarW_electron_ID[i - 1], TTG_electron_ID[i - 1], WW_electron_ID[i - 1], WZ_electron_ID[i - 1], ZZ_electron_ID[i - 1], ZG_electron_ID[i - 1]))

    f.write('electron_Reco_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_electron_Reco[i - 1], WGJets_electron_Reco[i - 1], ST_s_electron_Reco[i - 1], ST_t_electron_Reco[i - 1], ST_tbar_electron_Reco[i - 1], ST_tW_electron_Reco[i - 1], ST_tbarW_electron_Reco[i - 1], TTG_electron_Reco[i - 1], WW_electron_Reco[i - 1], WZ_electron_Reco[i - 1], ZZ_electron_Reco[i - 1], ZG_electron_Reco[i - 1]))

    f.write('electron_HLT_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_electron_HLT[i - 1], WGJets_electron_HLT[i - 1], ST_s_electron_HLT[i - 1], ST_t_electron_HLT[i - 1], ST_tbar_electron_HLT[i - 1], ST_tW_electron_HLT[i - 1], ST_tbarW_electron_HLT[i - 1], TTG_electron_HLT[i - 1], WW_electron_HLT[i - 1], WZ_electron_HLT[i - 1], ZZ_electron_HLT[i - 1], ZG_electron_HLT[i - 1]))

    f.write('muon_ID_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_muon_ID[i - 1], WGJets_muon_ID[i - 1], ST_s_muon_ID[i - 1], ST_t_muon_ID[i - 1], ST_tbar_muon_ID[i - 1], ST_tW_muon_ID[i - 1], ST_tbarW_muon_ID[i - 1], TTG_muon_ID[i - 1], WW_muon_ID[i - 1], WZ_muon_ID[i - 1], ZZ_muon_ID[i - 1], ZG_muon_ID[i - 1]))

    f.write('muon_iso_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_muon_iso[i - 1], WGJets_muon_iso[i - 1], ST_s_muon_iso[i - 1], ST_t_muon_iso[i - 1], ST_tbar_muon_iso[i - 1], ST_tW_muon_iso[i - 1], ST_tbarW_muon_iso[i - 1], TTG_muon_iso[i - 1], WW_muon_iso[i - 1], WZ_muon_iso[i - 1], ZZ_muon_iso[i - 1], ZG_muon_iso[i - 1]))

    f.write('muon_HLT_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_muon_HLT[i - 1], WGJets_muon_HLT[i - 1], ST_s_muon_HLT[i - 1], ST_t_muon_HLT[i - 1], ST_tbar_muon_HLT[i - 1], ST_tW_muon_HLT[i - 1], ST_tbarW_muon_HLT[i - 1], TTG_muon_HLT[i - 1], WW_muon_HLT[i - 1], WZ_muon_HLT[i - 1], ZZ_muon_HLT[i - 1], ZG_muon_HLT[i - 1]))

    f.write('btag_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_btag[i - 1], WGJets_btag[i - 1], ST_s_btag[i - 1], ST_t_btag[i - 1], ST_tbar_btag[i - 1], ST_tW_btag[i - 1], ST_tbarW_btag[i - 1], TTG_btag[i - 1], WW_btag[i - 1], WZ_btag[i - 1], ZZ_btag[i - 1], ZG_btag[i - 1]))

    f.write('JEC_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_JEC[i - 1], WGJets_JEC[i - 1], ST_s_JEC[i - 1], ST_t_JEC[i - 1], ST_tbar_JEC[i - 1], ST_tW_JEC[i - 1], ST_tbarW_JEC[i - 1], TTG_JEC[i - 1], WW_JEC[i - 1], WZ_JEC[i - 1], ZZ_JEC[i - 1], ZG_JEC[i - 1]))

    f.write('JER_'+year+'\tlnN')
    f.write('\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t-\t-\t-\n'%(WGJJ_JER[i - 1], WGJets_JER[i - 1], ST_s_JER[i - 1], ST_t_JER[i - 1], ST_tbar_JER[i - 1], ST_tW_JER[i - 1], ST_tbarW_JER[i - 1], TTG_JER[i - 1], WW_JER[i - 1], WZ_JER[i - 1], ZZ_JER[i - 1], ZG_JER[i - 1]))
'''
   #prin[i - 1], i,' ',ZA_sig_binerror,' ',ZA_sig_binerror,' ',ZA_binerror,' ',non_prompt_binerror,' ',TTA_binerror,' ',VV_binerror,' ',ST_binerror,' ',WA_binerror
