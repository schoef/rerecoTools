# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:run1_data_Fake --scenario pp --process reRECO --data --eventcontent AOD -s RAW2DIGI,RECO --datatier RECO --python RECO.py --conditions GR_R_74_V8 -n 10 --no_exec
import FWCore.ParameterSet.Config as cms

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
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:step3_DIGI2RAW.root'),
    fileNames = cms.untracked.vstring(
'file:pickevents_RAW_10.root',
'file:pickevents_RAW_1.root',
'file:pickevents_RAW_2.root',
'file:pickevents_RAW_11.root',
'file:pickevents_RAW_20.root',
'file:pickevents_RAW_3.root',
'file:pickevents_RAW_12.root',
'file:pickevents_RAW_21.root',
'file:pickevents_RAW_4.root',
'file:pickevents_RAW_13.root',
'file:pickevents_RAW_22.root',
'file:pickevents_RAW_5.root',
'file:pickevents_RAW_14.root',
'file:pickevents_RAW_23.root',
'file:pickevents_RAW_6.root',
'file:pickevents_RAW_15.root',
'file:pickevents_RAW_24.root',
'file:pickevents_RAW_7.root',
'file:pickevents_RAW_16.root',
'file:pickevents_RAW_25.root',
'file:pickevents_RAW_8.root',
'file:pickevents_RAW_17.root',
'file:pickevents_RAW_26.root',
'file:pickevents_RAW_9.root',
'file:pickevents_RAW_18.root',
'file:pickevents_RAW_27.root',
'file:pickevents_RAW_19.root',
'file:pickevents_RAW_28.root',
),
    secondaryFileNames = cms.untracked.vstring()
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
    fileName = cms.untracked.string('step3_RAW2DIGI_RECO.root'),
    outputCommands = process.AODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_74_V8', '')
process.GlobalTag.toGet.append(
  cms.PSet(record = cms.string("PFCalibrationRcd"),
           tag = cms.string("PFCalibration"),
           connect = cms.untracked.string("sqlite_file:PFCalibration.db")
           )
)
# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODoutput_step = cms.EndPath(process.AODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.AODoutput_step)


