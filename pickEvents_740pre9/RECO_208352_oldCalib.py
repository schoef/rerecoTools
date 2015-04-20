# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:run1_data_Fake --scenario pp --process reRECO --data --eventcontent AOD -s RAW2DIGI,RECO --datatier RECO --python RECO.py --conditions GR_R_74_V8 -n 10 --no_exec
import FWCore.ParameterSet.Config as cms
#from FWCore.ParameterSet.VarParsing import VarParsing
#
#options = VarParsing ('analysis')
#
## add a list of strings for events to process
#options.register ('eventsToProcess',
#          '',
#          VarParsing.multiplicity.list,
#          VarParsing.varType.string,
#          "Events to process")
#options.parseArguments()
#

process = cms.Process('reRECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:step3_DIGI2RAW.root'),
    fileNames = cms.untracked.vstring('root://eoscms.cern.ch//store/group/phys_jetmet/schoef/740pre9_outlier_rereco/Run2012D_JetHT_RAW_208352.root'),
    secondaryFileNames = cms.untracked.vstring()
)
process.source.eventsToProcess = \
       cms.untracked.VEventRange (
"208352:9:11740159",
"208352:11:14235949",
"208352:3:2804412",
"208352:19:20981421",
"208352:15:20368765",
"208352:13:16969238",
"208352:15:20680976",
"208352:9:12159249",
"208352:3:3034705",
"208352:13:17582465",
"208352:12:15767735",
"208352:3:3265403",
"208352:5:6032679",
"208352:9:11740159",
"208352:11:14235949",
"208352:19:20981421",
"208352:5:6032679",
"208352:3:2804412",
"208352:13:17722247",
"208352:11:14050347",
"208352:2:2205211",
"208352:5:6452080",
"208352:13:17110246",
"208352:1:1340235",
"208352:12:16474308",
"208352:3:3265403",
"208352:3:3298932",
)
process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('~/eos/cms/store/group/phys_jetmet/schoef/Run2012D_JetHT_RAW2DIGI_AOD_208352.root'),
    outputCommands = process.AODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_74_V8', '')
#process.GlobalTag.toGet.append(
#  cms.PSet(record = cms.string("PFCalibrationRcd"),
#           tag = cms.string("PFCalibration"),
#           connect = cms.untracked.string("sqlite_file:PFCalibration.db")
#           )
#)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODoutput_step = cms.EndPath(process.AODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.AODoutput_step)


