2_calculate_uncertainty.py $1 $2 $4 $3 signal muon barrel medium mjj unfolding off
2_calculate_uncertainty.py $1 $2 $4 $3 signal electron barrel medium mjj unfolding off
2_calculate_uncertainty.py $1 $2 $4 $3 signal muon endcap medium mjj unfolding off
2_calculate_uncertainty.py $1 $2 $4 $3 signal electron endcap medium mjj unfolding off
2_calculate_uncertainty.py $1 $2 $4 $3 control muon barrel medium mjj unfolding off
2_calculate_uncertainty.py $1 $2 $4 $3 control electron barrel medium mjj unfolding off
2_calculate_uncertainty.py $1 $2 $4 $3 control muon endcap medium mjj unfolding off
2_calculate_uncertainty.py $1 $2 $4 $3 control electron endcap medium mjj unfolding off

cat $2/signal_muon_barrel/*py     > $2/uncer_signal_muon_barrel.py
cat $2/signal_muon_endcap/*py     > $2/uncer_signal_muon_endcap.py
cat $2/signal_electron_barrel/*py     > $2/uncer_signal_electron_barrel.py
cat $2/signal_electron_endcap/*py     > $2/uncer_signal_electron_endcap.py
cat $2/control_muon_barrel/*py     > $2/uncer_control_muon_barrel.py
cat $2/control_muon_endcap/*py     > $2/uncer_control_muon_endcap.py
cat $2/control_electron_barrel/*py     > $2/uncer_control_electron_barrel.py
cat $2/control_electron_endcap/*py     > $2/uncer_control_electron_endcap.py

pdf_scale_uncer.py $4 $1 $2 muon signal barrel 1
pdf_scale_uncer.py $4 $1 $2 muon signal endcap 1
pdf_scale_uncer.py $4 $1 $2 electron signal barrel 1
pdf_scale_uncer.py $4 $1 $2 electron signal endcap 1
pdf_scale_uncer.py $4 $1 $2 muon control barrel 1
pdf_scale_uncer.py $4 $1 $2 muon control endcap 1
pdf_scale_uncer.py $4 $1 $2 electron control barrel 1
pdf_scale_uncer.py $4 $1 $2 electron control endcap 1
