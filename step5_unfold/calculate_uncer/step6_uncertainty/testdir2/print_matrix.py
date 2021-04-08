import ROOT
from ROOT import gROOT, THStack, TH1D, TList, TFile, TH2D, TCanvas

f_in_WGJJ = TFile.Open("2018_all_mc_signal_barrel_medium_btag_WGJJ_uncertainty.root")
h = f_in_WGJJ.Get("hist_in_")
h.Scale(0.39/h.GetSum())
bin_with = [20,40,70,110,400]
for i in range(h.GetNbinsX()) : 
    content_gen = 0
    for j in range(h.GetNbinsX()) :
        content_gen = content_gen + h.GetBinContent(i+1,j+1)
    for k in range(h.GetNbinsX()) :
        h.SetBinContent(i+1, k+1, h.GetBinContent(i+1, k+1)/ content_gen)
    h.GetXaxis().SetBinLabel(i+1,str(bin_with[i]) + '~' + str(bin_with[i+1]) + ' GeV')
    h.GetYaxis().SetBinLabel(i+1,str(' '))
    #h.GetYaxis().SetBinLabel(i+1,str(bin_with[i]) + '~' + str(bin_with[i+1]) + ' GeV')

c1 = TCanvas("Acceptance","Acceptance", 900,600)
h.Draw("coloz text")
h.SetTitle("")
h.SetStats(0)
#h.SetLineColor(2)
h.GetXaxis().SetTitle("Gen ptLep1")
h.GetYaxis().SetTitle("Reco ptLep1")
#h.GetYaxis().SetTitleOffset(0.3)
h.SetMaximum(1.3 * h.GetMaximum())
c1.SaveAs('matrix.png')

