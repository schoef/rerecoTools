#!/bin/sh
#python $CMSSW_RELEASE_BASE/src/Configuration/DataProcessing/test/RunPromptReco.py --scenario ppRun2 --reco --aod --miniaod --dqmio --global-tag 74X_dataRun2_Prompt_v1 --lfn=/store/data/Run2015B/SingleMuon/RAW/v1/000/252/116/00000/A403ACE8-8F2E-E511-B3D6-02163E0138B3.root --alcareco TkAlMinBias
python $CMSSW_RELEASE_BASE/src/Configuration/DataProcessing/test/RunPromptReco.py --scenario ppRun2 --reco --aod --global-tag 74X_dataRun2_Prompt_v2 --lfn=root://xrootd.unl.edu//store/data/Run2015D/JetHT/RAW/v1/000/257/599/00000/08832569-C264-E511-AC49-02163E014154.root --alcareco TkAlMinBias
