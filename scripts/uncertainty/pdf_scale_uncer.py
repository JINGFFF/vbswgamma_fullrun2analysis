#!/usr/bin/env python
import sys
import os
import re
#from uncertainty_unfold import *
import ROOT
from ROOT import gROOT, THStack, TH1D, TList, TFile, TH2D
from math import fabs, sqrt
#qcd
#mr = 1, mf = 1, h1
#for muR1
#mr = 1, mf = 2,   h4
#mr = 1, mf = 0.5, h7
#for muF1
#mr = 2,   mf = 1, h2
#mr = 0.5, mf = 1, h3
#for muRmuF
#mr = 2,   mf = 2,   h5
#mr = 0.5, mf = 0.5, h9
#pdf 10 - 112

#ewk
#mr = 1, mf = 1,   h1
#mr = 1, mf = 2,   h16
#mr = 1, mf = 0.5, h31
#pdf 46 - 148
year      = sys.argv[1]
inputdir  = sys.argv[2]
outputdir = sys.argv[3]
channel   = sys.argv[4]
region    = sys.argv[5]
eORb      = sys.argv[6]
shape     = sys.argv[7]

f_in_WGJJ_m_b   = TFile.Open(inputdir + "/" + year + "_" + channel + "_mc_" + region + "_" + eORb + "_WGJJ.root")

f_in_WGJets_m_b = TFile.Open(inputdir + "/" + year + "_" + channel + "_mc_" + region + "_" + eORb + "_WGJets.root")

#ll = [1, 2, 3, 4]
def scale(f, center_index, index2, index3):
    hist_center = f.Get("hist_pdf_"+str(center_index))
    hist2       = f.Get("hist_pdf_"+str(index2))
    hist3       = f.Get("hist_pdf_"+str(index3))
    
    if(shape == "1") :
        hist_center.Scale(1./hist_center.GetSum())
        hist2.Scale(1./hist2.GetSum())
        hist3.Scale(1./hist3.GetSum())

    scalexx = []# * hist_center.GetNbinsX()
    for i in range(hist_center.GetNbinsX()):
        scalexx.append(fabs(hist2.GetBinContent(i+1) - hist3.GetBinContent(i+1)) / (2 * hist_center.GetBinContent(i+1)))
    return scalexx

def pdf(f, start_index, end_index):
    hist_center = f.Get("hist_pdf_"+str(start_index))
    #hist_center.Print()
    hist_member = []
    for j in range(1, end_index - start_index +1):
        hist_member.append(f.Get("hist_pdf_"+str(start_index + j)))
    scalexx = []# * hist_center.GetNbinsX()
    diff = 0
    su = 0

    if(shape == "1") :
        hist_center.Scale(1./hist_center.GetSum())
        for k in range(len(hist_member)):
            hist_member[k].Scale(1./hist_member[k].GetSum())

    for i in range(hist_center.GetNbinsX()):
        diff = 0
        su = 0
        for k in range(len(hist_member)):
            center = hist_center.GetBinContent(i+1)
            diff = hist_member[k].GetBinContent(i+1)- center
            su = su + diff**2
        #print(len(hist_member),hist_center.GetBinContent(i+1))
        scalexx.append(sqrt(su/len(hist_member))/ (hist_center.GetBinContent(i+1)))
    return scalexx


ll_wgjj_pdf   = pdf(f_in_WGJJ_m_b, 46, 148)
ll_wgjj_scale = scale(f_in_WGJJ_m_b, 1, 16, 31)

ll_wgjets_pdf    = pdf(f_in_WGJets_m_b, 10, 112)
ll_wgjets_muR1   = scale(f_in_WGJets_m_b, 1, 4, 7)
ll_wgjets_muF1   = scale(f_in_WGJets_m_b, 1, 2, 3)
ll_wgjets_muRmuF = scale(f_in_WGJets_m_b, 1, 5, 9)

#print(ll_wgjets_m_b)
#print(ll_wgjets_m_e)
#print(ll_wgjets_e_b)
#print(ll_wgjj_pdf)

os.system("mkdir -p " + outputdir)
outPYfile = open(outputdir + "/uncer_pdf_" + region + "_" + channel + "_" + eORb + ".py", 'w')

outPYfile.write('WGJJ_pdf = [')
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outPYfile.write( str(ll_wgjj_pdf[k1]) + ']'+'\n')
    else :
        outPYfile.write( str(ll_wgjj_pdf[k1]) + ', ')


outPYfile.write('WGJJ_scale = [')
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outPYfile.write( str(ll_wgjj_scale[k1]) + ']'+'\n')
    else :
        outPYfile.write( str(ll_wgjj_scale[k1]) + ', ')

outPYfile.write('WGJets_pdf = [')
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outPYfile.write( str(ll_wgjets_pdf[k1]) + ']'+'\n')
    else :
        outPYfile.write( str(ll_wgjets_pdf[k1]) + ', ')

outPYfile.write('WGJets_muR1 = [')
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outPYfile.write( str(ll_wgjets_muR1[k1]) + ']'+'\n')
    else :
        outPYfile.write( str(ll_wgjets_muR1[k1]) + ', ')

outPYfile.write('WGJets_muF1 = [')
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outPYfile.write( str(ll_wgjets_muF1[k1]) + ']'+'\n')
    else :
        outPYfile.write( str(ll_wgjets_muF1[k1]) + ', ')

outPYfile.write('WGJets_muRmuF = [')
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outPYfile.write( str(ll_wgjets_muRmuF[k1]) + ']'+'\n')
    else :
        outPYfile.write( str(ll_wgjets_muRmuF[k1]) + ', ')
outPYfile.close()

## for csv
outCSVfile = open(outputdir + "/uncer_pdf_" + region + "_" + channel + "_" + eORb + ".csv", 'w')

outCSVfile.write(region + ' ' + channel + ' '+ eORb + ', ' )
for k1 in range(len(ll_wgjj_pdf)):
    outCSVfile.write( "bin" + str(k1+1) +', ')
outCSVfile.write('\n')

outCSVfile.write('WGJJ_pdf, ' )
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outCSVfile.write( str(ll_wgjj_pdf[k1]) +'\n')
    else :
        outCSVfile.write( str(ll_wgjj_pdf[k1]) + ', ')


outCSVfile.write('WGJJ_scale, ')
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outCSVfile.write( str(ll_wgjj_scale[k1]) +'\n')
    else :
        outCSVfile.write( str(ll_wgjj_scale[k1]) + ', ')

outCSVfile.write('WGJets_pdf, ' )
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outCSVfile.write( str(ll_wgjets_pdf[k1]) +'\n')
    else :
        outCSVfile.write( str(ll_wgjets_pdf[k1]) + ', ')

outCSVfile.write('WGJets_muR1, ' )
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outCSVfile.write( str(ll_wgjets_muR1[k1]) +'\n')
    else :
        outCSVfile.write( str(ll_wgjets_muR1[k1]) + ', ')

outCSVfile.write('WGJets_muF1, ' )
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outCSVfile.write( str(ll_wgjets_muF1[k1]) +'\n')
    else :
        outCSVfile.write( str(ll_wgjets_muF1[k1]) + ', ')

outCSVfile.write('WGJets_muRmuF, ' )
for k1 in range(len(ll_wgjj_pdf)):
    if k1 == (len(ll_wgjj_pdf) - 1):
        outCSVfile.write( str(ll_wgjets_muRmuF[k1]) +'\n')
    else :
        outCSVfile.write( str(ll_wgjets_muRmuF[k1]) + ', ')
outCSVfile.close()

