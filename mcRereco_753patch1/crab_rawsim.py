from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_RunIISummer15GS-MCRUN2_71_V1-v1"
config.General.workArea = "mcRereco"
config.General.transferOutputs = True #whether to transfer
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'rawsim.py'
config.JobType.outputFiles = ['JME-RunIIFall15DR75-00001_step1.root']
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
config.Data.publishDBS = 'phys03'
config.Data.inputDataset   = '/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISummer15GS-MCRUN2_71_V1-v1/GEN-SIM'
config.Data.splitting   = 'EventAwareLumiBased'
config.Data.unitsPerJob = 40
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
config.Data.totalUnits = 1000000
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

