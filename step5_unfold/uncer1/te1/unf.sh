#
text2workspace.py -m 125 -o datacard.root datacard.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO map='.*genbin1.*:r_Bin1[1,-2,4]' --PO map='.*genbin2.*:r_Bin2[1,-2,4]' --PO map='.*genbin3.*:r_Bin3[1,-2,4]' --PO map='.*genbin4.*:r_Bin4[1,-2,4]' --PO map='.*genbin5.*:r_Bin5[1,-2,4]' --PO map='.*genbin6.*:r_Bin6[1,-2,4]' --PO map='.*genbin7.*:r_Bin7[1,-2,4]' --PO map='.*genbin8.*:r_Bin8[1,-2,4]' --PO map='.*genbin9.*:r_Bin9[1,-2,4]' --PO map='.*genbin10.*:r_Bin10[1,-2,4]' --PO map='.*genbin11.*:r_Bin11[1,-2,4]' --PO map='.*genbin12.*:r_Bin12[1,-2,4]'
#
combine datacard.root -M MultiDimFit --algo singles -t -1 --setParameters r_Bin1=1,r_Bin2=1,r_Bin3=1,r_Bin4=1,r_Bin5=1,r_Bin6=1,r_Bin7=1,r_Bin8=1,r_Bin9=1,r_Bin10=1,r_Bin11=1,r_Bin12=1 -m 125 --saveFitResult  > tmp.txt 