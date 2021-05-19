#!/usr/bin/python

import sys
import os
import re

import ROOT
from ROOT import gROOT, THStack, TH1D, TList, TFile, TH2D, TCanvas

name = sys.argv[1]
uncer = sys.argv[2]
acc_file = sys.argv[3]
input_2016 = sys.argv[4]
input_2017 = sys.argv[5]
input_2018 = sys.argv[6]

uncer_file = open(uncer, "r")
#print ok
f_in_WGJJ_2016 = TFile.Open(input_2016)
f_in_WGJJ_2017 = TFile.Open(input_2017)
f_in_WGJJ_2018 = TFile.Open(input_2018)
acc = TFile.Open(acc_file)

hh = acc.Get("acc_ptlep")
bin_num = hh.GetNbinsX()

uncer_list_down = []
uncer_list_up = []

lines = uncer_file.readlines()
for i in range(0, len(lines)):
    for j in range(0, len(lines)):
        if "r_Bin" + str(bin_num-i) + " :    +1.000" in lines[j]:
            xx = lines[j].split(' ')
            print (xx[11])
            xxx = xx[11].split('/')
            uncer_list_down.append(xxx[0])
            uncer_list_up.append(xxx[1])
print (uncer_list_down)
print (uncer_list_up)


h_acc = TH1D("h_acc","h_acc", bin_num, 0 ,bin_num)
h_acc.Print()
hh.Scale(24.83/hh.GetSum())
bin_with = []
#bin_with = [20,40,70,110,400]
for i in range(hh.GetNbinsX()+1) :
    if i == hh.GetNbinsX():
        bin_with.append(hh.GetBinLowEdge(i+1))
    else:
        bin_with.append(hh.GetBinLowEdge(i+1))
print(bin_with)

for i in range(hh.GetNbinsX()) :
    h_acc.SetBinContent(i+1,hh.GetBinContent(i+1)/(bin_with[i+1] - bin_with[i]))
    h_acc.GetXaxis().SetBinLabel(i+1,str(bin_with[i]) + '~' + str(bin_with[i+1]) + ' GeV')
    h_acc.SetBinError(i+1,  h_acc.GetBinContent(i+1)*(abs(float(uncer_list_down[i])) + abs(float(uncer_list_up[i])) )/2)

c2 = TCanvas("XS","XS",900,700)
c2.cd()
h_acc.Draw("HIST text e")
h_acc.SetTitle("")
h_acc.SetStats(0)
h_acc.SetLineColor(2)
h_acc.GetXaxis().SetTitle(name)
h_acc.GetYaxis().SetTitle("fb / GeV")
h_acc.SetMaximum(1.3 * h_acc.GetMaximum())
c2.SaveAs('XS'+name+'.png')



h_2016, h_2017, h_2018 = [], [], []

h = f_in_WGJJ_2016.Get("hist_")
#bin_num = h.GetNbinsX()
h.Print()
# read hist
for i in range(bin_num):
   h_2016.append(f_in_WGJJ_2016.Get("hist_in_" + str(i) + "_"))
   h_2016[i].Scale(35.92)
   h_2017.append(f_in_WGJJ_2017.Get("hist_in_" + str(i) + "_"))
   h_2017[i].Scale(41.50)
   h_2018.append(f_in_WGJJ_2018.Get("hist_in_" + str(i) + "_"))
   h_2018[i].Scale(59.74)



#bin_with = [20,40,70,110,400]
h_matrix = TH2D("h_matrix","h_matrix", bin_num, 0 ,bin_num, bin_num, 0 ,bin_num)
for i in range(bin_num) :
    content_gen = 0
    for j in range(bin_num) :
        content_gen = content_gen + h_2016[j].GetBinContent(i+1) + h_2017[j].GetBinContent(i+1) + h_2018[j].GetBinContent(i+1)
    for k in range(bin_num) :
        matrix_content = h_2016[k].GetBinContent(i+1) + h_2017[k].GetBinContent(i+1) + h_2018[k].GetBinContent(i+1)
        h_matrix.SetBinContent(i+1, k+1, matrix_content / content_gen)
    h_matrix.GetXaxis().SetBinLabel(i+1,str(bin_with[i]) + '~' + str(bin_with[i+1]) + ' GeV')
    h_matrix.GetYaxis().SetBinLabel(i+1,str(' '))
    #h.GetYaxis().SetBinLabel(i+1,str(bin_with[i]) + '~' + str(bin_with[i+1]) + ' GeV')

c1 = TCanvas("Acceptance","Acceptance", 900,600)
c1.cd()
h_matrix.Draw("coloz text")
h_matrix.SetTitle("")
h_matrix.SetStats(0)
#h.SetLineColor(2)
h_matrix.GetXaxis().SetTitle("Gen "+ name)
h_matrix.GetYaxis().SetTitle("Reco "+ name)
#h.GetYaxis().SetTitleOffset(0.3)
h_matrix.SetMaximum(1.3 * h.GetMaximum())
c1.SaveAs('matrix_'+name+'.png')
