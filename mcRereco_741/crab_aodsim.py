from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_AODSIM"
config.General.workArea = "mcRereco"
config.General.transferOutputs = True #whether to transfer
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'raw2digi_reco.py'
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
config.Data.publishDBS = 'phys03'
config.Data.inputDBS = 'phys03'
config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/schoef-crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_GEN-SIM-a545037419a6c9acf651cdcc5cc6843f/USER'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 6 
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 1000000
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

