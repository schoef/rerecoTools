from WMCore.Configuration import Configuration
config = Configuration()

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option("--cmd", dest="command", default='status', type="string", action="store", help="What to do.")
#(options, args) = parser.parse_args()


config.section_("General")
#config.General.requestName = "QCD_Pt-15to7000_AllChlgoodAsymptFlat0to50bx25_74X_mcRun2_asymptotic_AllChannelsGood_v0-v2_RunIISpring15MiniAODv2-74X"
config.General.requestName = "QCD_Pt-15to7000_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1"
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
config.Data.inputDataset = '/QCD_Pt-15to7000_TuneCUETP8M1_FlatP6_13TeV_pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.publication = True
config.Data.outputDatasetTag = 'mAOD8021'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
