from WMCore.Configuration import Configuration
config = Configuration()

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option("--cmd", dest="command", default='status', type="string", action="store", help="What to do.")
#(options, args) = parser.parse_args()


config.section_("General")
#config.General.requestName = "QCD_Pt-15to7000_AllChlgoodAsymptFlat0to50bx25_74X_mcRun2_asymptotic_AllChannelsGood_v0-v2_RunIISpring15MiniAODv2-74X"
#config.General.requestName = "QCD_Pt-15to7000_AllChlgoodAsymptNoPUbx25_74X_mcRun2_asymptotic_AllChannelsGood_v0-v2_RunIISpring15MiniAODv2-74X"
#config.General.requestName = "QCD_Pt-15to7000_AsymptFlat0to50bx25Reco_MCRUN2_74_V9-v3_RunIISpring15MiniAODv2-74X"
config.General.requestName = "QCD_Pt-15to7000_AsymptNoPUbx25Reco_MCRUN2_74_V9-v3_RunIISpring15MiniAODv2-74X"
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
#config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
#config.Data.inputDataset = '/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-AllChlgoodAsymptFlat0to50bx25_74X_mcRun2_asymptotic_AllChannelsGood_v0-v2/AODSIM'
#config.Data.inputDataset = '/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-AllChlgoodAsymptNoPUbx25_74X_mcRun2_asymptotic_AllChannelsGood_v0-v2/AODSIM'
#config.Data.inputDataset = '/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-AsymptFlat0to50bx25Reco_MCRUN2_74_V9-v3/GEN-SIM-RECO'
config.Data.inputDataset = '/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-AsymptNoPUbx25Reco_MCRUN2_74_V9-v3/GEN-SIM-RECO'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

