from WMCore.Configuration import Configuration
config = Configuration()

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option("--cmd", dest="command", default='status', type="string", action="store", help="What to do.")
#(options, args) = parser.parse_args()


config.section_("General")
#config.General.requestName = "QCD_Pt-15to7000_AllChlgoodAsymptFlat0to50bx25_74X_mcRun2_asymptotic_AllChannelsGood_v0-v2_RunIISpring15MiniAODv2-74X"
config.General.requestName = "JetHT_Run2016H-22Feb2017-v1_2"
config.General.workArea = "mAOD"
config.General.transferOutputs = True #whether to transfer
config.General.transferLogs = True #1MB still available
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'miniAOD-prod_PAT.py'
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
#config.Data.inputDBS = 'phys03'
config.Data.allowNonValidInputDataset = True
config.Data.publishDBS = 'phys03'
#/JetHT/Run2016B-22Feb2017_ver1-v2/AOD
#/JetHT/Run2016B-22Feb2017_ver2-v1/AOD
#/JetHT/Run2016C-22Feb2017-v1/AOD
#/JetHT/Run2016D-22Feb2017-v1/AOD
#/JetHT/Run2016E-22Feb2017-v1/AOD
#/JetHT/Run2016F-22Feb2017-v1/AOD
#/JetHT/Run2016H-22Feb2017-v1/AOD

config.Data.inputDataset = '/JetHT/Run2016H-22Feb2017-v1/AOD'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.outputDatasetTag = 'mAOD8025'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
