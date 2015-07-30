from WMCore.Configuration import Configuration
config = Configuration()

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option("--cmd", dest="command", default='status', type="string", action="store", help="What to do.")
#(options, args) = parser.parse_args()


config.section_("General")
config.General.requestName = "JetHT_Run2015B-v1_74X_dataRun2_Prompt_v1_M0"
config.General.workArea = "reReco"
config.General.transferOutputs = True #whether to transfer
config.General.transferLogs = True #1MB still available
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'RECO.py'
#config.JobType.inputFiles = ['PFCalibration.db']
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
config.Data.lumiMask = 'Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt'
config.Data.publishDBS = 'phys03'
config.Data.inputDataset   = '/JetHT/Run2015B-v1/RAW'
config.Data.splitting   = 'LumiBased'
config.Data.unitsPerJob = 2
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

