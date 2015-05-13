from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "RelValQCD_FlatPt_15_3000HS_13_CMSSW_7_4_1-MCRUN2_74_V9_gensim71X-v1_PhilFixRecHitFlag"
#config.General.requestName = "RelValZMM_13_CMSSW_7_4_1-MCRUN2_74_V9_extended-v2_PhilFix"
config.General.workArea = "privateRelvals"
config.General.transferOutputs = True #whether to transfer
config.General.transferLogs = False #1MB still available
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'run_private_digi_reco_25ns.py'
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
config.Data.publishDBS = 'phys03'
config.Data.inputDataset   = '/RelValQCD_FlatPt_15_3000HS_13/CMSSW_7_4_1-MCRUN2_74_V9_gensim71X-v1/GEN-SIM-DIGI-RAW-HLTDEBUG'
#config.Data.inputDataset   = '/RelValZMM_13/CMSSW_7_4_1-MCRUN2_74_V9_extended-v2/GEN-SIM-DIGI-RAW-HLTDEBUG'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

