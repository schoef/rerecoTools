from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "JetHT_Run2015D_lumiBased_reduced_M2_5_100"
config.General.workArea = "dataRereco"
config.General.transferOutputs = True #whether to transfer
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'RECO_RAW2DIGI_L1Reco_RECO_ALCA_EI_PAT_DQM_M2_5_100.py'
#config.JobType.psetName   = 'RECO_RAW2DIGI_L1Reco_RECO_ALCA_EI_PAT_DQM_M2_5_500.py'
config.JobType.outputFiles = ['RECO_RAW2DIGI_L1Reco_RECO_ALCA_EI_PAT_DQM.root']
config.JobType.maxMemoryMB = 2500
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
config.Data.publishDBS = 'phys03'
config.Data.lumiMask = 'json_260431.txt'
#config.Data.inputDBS = 'phys03'
config.Data.inputDataset   = '/JetHT/Run2015D-v1/RAW'
config.Data.splitting   = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 1000000
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
