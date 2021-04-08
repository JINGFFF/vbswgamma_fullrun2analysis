void test(){

hist_JER_up->SetLineColor(kBlue)
hist_JEC_up->SetLineColor(kBlue)
hist_JER_down->SetLineColor(kRed)
hist_JEC_down->SetLineColor(kRed)
hist_new->SetLineColor(kBlack)
hist_JER_down->SetLineStyle(2)
hist_JER_up->SetLineStyle(2)
hist_JEC_up->Draw("hist")
hist_JER_up->Draw("hist same")
hist_new->Draw("hist same")
hist_JER_down->Draw("hist same")
hist_JEC_down->Draw("hist same")

}
