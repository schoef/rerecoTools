from WMCore.Configuration import Configuration
config = Configuration()

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option("--cmd", dest="command", default='status', type="string", action="store", help="What to do.")
#(options, args) = parser.parse_args()


config.section_("General")
config.General.requestName = "RelValZMM_13_CMSSW_7_4_0_pre9-PU50ns_MCRUN2_74_V6-v1_MVA_ON_mAOD"
config.General.workArea = "relValMINIAOD"
config.General.transferOutputs = True #whether to transfer
config.General.transferLogs = False #1MB still available
#config.General.failureLimit =  #0.1 or 10% (which?) fraction of tolerated failures

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'miniAOD-prod_PAT_MCRUN2_74_V6.py'
#config.JobType.allowNonProductionCMSSW = True
#config.JobType.pyCfgParams   = [ 'keep=*_genMetTrue_*_*,*_pfMet_*_*,*_packedPFCandidates_*_*,*_prunedGenParticles_*_*,*_packedGenParticles_*_*', 'GT=POSTLS170_V6::All']
config.section_("Data")
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
config.Data.inputDataset   = '/RelValZMM_13/schoef-crab_RelValZMM_13_CMSSW_7_4_0_pre9-PU50ns_MCRUN2_74_V6-v1_MVA_ON-2c3d09f9ab23f307a4d661ebb9d909a5/USER'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

