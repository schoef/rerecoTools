from WMCore.Configuration import Configuration
config = Configuration()

#from optparse import OptionParser
#parser = OptionParser()
#parser.add_option("--cmd", dest="command", default='status', type="string", action="store", help="What to do.")
#(options, args) = parser.parse_args()


config.section_("General")
#config.General.requestName = "QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8"
config.General.requestName = "QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_M2_5_500"
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
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
#config.Data.inputDataset = '/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/schoef-crab_QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_RunIISummer15GS-MCRUN2_71_V1-v1-8d945e02baaaaef6f16f2f3bf8ea5c13/USER'
config.Data.inputDataset = '/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/schoef-crab_QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8_RunIISummer15GS-MCRUN2_71_V1-v1_M2_5_500-83131275e9c2749afbfc1eb67dd321f9/USER'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 20
config.Data.publication = True
#config.Data.publishDataName = 'mAOD730p1'
#config.Data.totalUnits = 
config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

