from WMCore.Configuration import Configuration
config = Configuration()

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option("--cmd", dest="command", default='status', type="string", action="store", help="What to do.")
#(options, args) = parser.parse_args()


config.section_("General")
#config.General.requestName = "JetHT_CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_jht2012D-v1_ecalCalibNewPFHadCalib_mAOD"
#config.General.requestName = "JetHT25ns_CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_jht25ns2012D-v2_ecalCalibNewPFHadCalib_mAOD"
config.General.requestName = "DoubleMuParked_CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_dm2012D-v2_mAOD"
config.General.workArea = "mAOD"
config.General.transferOutputs = True #whether to transfer
config.General.transferLogs = False #1MB still available
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'miniAOD-prod_PAT.py'
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
#config.Data.inputDataset = '/JetHT/schoef-crab_JetHT_CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_jht2012D-v1_ecalCalibNewPFHadCalib_AOD-1a2e9f62947707e2ae5b0f7441f32b8f/USER'
#config.Data.inputDataset = '/JetHT25ns/schoef-crab_JetHT25ns_CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_jht25ns2012D-v2_ecalCalibNewPFHadCalib_AOD-1a2e9f62947707e2ae5b0f7441f32b8f/USER'
config.Data.inputDataset = '/DoubleMuParked/schoef-crab_DoubleMuParked_CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_dm2012D-v2_AOD-1a2e9f62947707e2ae5b0f7441f32b8f/USER'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

