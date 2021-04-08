import ROOT
from ROOT import gROOT, THStack, TH1D, TList, TFile, TH2D, TCanvas

f_in_WGJJ2016 = TFile.Open("/home/pku/pengj/testvbs/workdir/ana2016/step5_unfold/calculate_uncer/step6_uncertainty/testdir/2016_all_mc_signal_barrel_medium_btag_WGJJ_uncertainty.root")
h2016 = f_in_WGJJ2016.Get("hist_count")
h2016.Scale(25.61/h2016.GetSum())

f_in_WGJJ2017 = TFile.Open("/home/pku/pengj/testvbs/workdir/ana2017_v2/step5_unfold/calculate_uncer/step6_uncertainty/testdir/2017_all_mc_signal_barrel_medium_btag_WGJJ_uncertainty.root")
h2017 = f_in_WGJJ2017.Get("hist_count")
h2017.Scale(21.21/h2017.GetSum())

f_in_WGJJ2018 = TFile.Open("2018_all_mc_signal_barrel_medium_btag_WGJJ_uncertainty.root")
h2018 = f_in_WGJJ2018.Get("hist_count")
h2018.Scale(21.21/h2018.GetSum())

h = h2016.Clone()
h.Reset()
tmp_content = 0
bin_with = [20,40,70,110,400]
for i in range(h.GetNbinsX()) : 
    tmp_content = ((h2016.GetBinContent(i+1))**2 + (h2017.GetBinContent(i+1))**2 + (h2018.GetBinContent(i+1))**2)/(h2016.GetBinContent(i+1) + h2017.GetBinContent(i+1) + h2018.GetBinContent(i+1))
    h.SetBinContent(i+1,tmp_content/(bin_with[i+1] - bin_with[i]))
    h.GetXaxis().SetBinLabel(i+1,str(bin_with[i]) + '~' + str(bin_with[i+1]) + ' GeV')
c1 = TCanvas("XS","XS",900,700)
h.Draw("HIST text")
h.SetTitle("")
h.SetStats(0)
h.SetLineColor(2)
h.GetXaxis().SetTitle("ptLep1")
h.GetYaxis().SetTitle("fb / GeV")
h.GetYaxis().SetTitleOffset(1.2)
h.SetMaximum(1.3 * h.GetMaximum())
c1.SaveAs('combine_XS.png')
