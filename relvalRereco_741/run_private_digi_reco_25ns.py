# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --conditions auto:run2_mc -s RAW2DIGI,L1
#Reco,RECO,EI,VALIDATION,DQM --datatier GEN-SIM-RECO,DQMIO -n 10 --magField 38T_PostLS1 --eventcontent RECOSIM,DQM --io RECOUP15.io --python RECOUP15.py --no
#_exec --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
#    secondaryFileNames = cms.untracked.vstring(),
#    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),                        
    fileNames = cms.untracked.vstring(
'root://eoscms.cern.ch//store/relval/CMSSW_7_4_1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_74_V9_gensim71X-v1/00000/0287B5B9-5CEC-E411-86E8-003048FF9AA6.root',
    )
)

process.options = cms.untracked.PSet(

)
# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('crab_test.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECO')
    )
)

process.RECOSIMoutput.outputCommands.append( "keep *_particleFlow*_*_RECO2")

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('histo.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('DQMIO')
    )
)

# Additional output definition

# Other statements
#process.mix.playback = True
#process.mix.digitizers = cms.PSet()
#for a in process.aliases: delattr(process, a)
#process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MCRUN2_74_V9::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.prevalidation_step = cms.Path(process.prevalidation)
process.dqmoffline_step = cms.Path(process.DQMOffline)
process.validation_step = cms.EndPath(process.validation)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
#process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.RECOSIMoutput_step)

# customisation of the proces
# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

