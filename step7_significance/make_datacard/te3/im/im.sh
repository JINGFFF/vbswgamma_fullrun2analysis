text2workspace.py datacard.txt -m 125
combineTool.py -M Impacts -d datacard.root -m 125 --doInitialFit
combineTool.py -M Impacts -d datacard.root -m 125 --doFits --parallel 4
combineTool.py -M Impacts -d datacard.root -m 125 -o impacts.json
plotImpacts.py -i impacts.json -o impacts
