for file in `das_client.py --limit=0 --query="file dataset=/DYJetsToLL_M-50_PtZ-100_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"`; do echo "'$file',"; done