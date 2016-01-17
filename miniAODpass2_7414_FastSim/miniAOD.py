# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/RunIISpring15FSPremix-GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/AODSIM --fileout file:JME-RunIISpring15MiniAODv2-00008.root --mc --eventcontent MINIAODSIM --runUnscheduled --fast --customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 74X_mcRun2_asymptotic_v2 --step PAT --python_filename miniAOD.py --no_exec -n 1920
import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('FastSimulation.Configuration.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1920)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/00099680-BD95-E511-877D-02163E01686C.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/002D3CE7-AA95-E511-B04F-02163E010CC6.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/0071FE55-CC95-E511-B394-02163E01606A.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/008E200A-8E95-E511-AE2F-02163E016950.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/00E42C99-0A96-E511-A653-02163E00B178.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/00F09DD9-8E95-E511-8BA2-02163E0130AE.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/02019F86-7D95-E511-9FE1-02163E010BDF.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/026C201F-9995-E511-B50E-02163E01413F.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/02CDFA30-7E95-E511-BFF4-0CC47A04D082.root', 
        '/store/mc/RunIISpring15FSPremix/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/AODSIM/GenFromFullSim_FastAsympt25ns_MCRUN2_74_V9-v1/00000/04AE8B93-C095-E511-8F49-02163E015D8D.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1920'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:JME-RunIISpring15MiniAODv2-00008.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '74X_mcRun2_asymptotic_v2', '')

# Path and EndPath definitions
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from FastSimulation.Configuration.MixingModule_Full2Fast
from FastSimulation.Configuration.MixingModule_Full2Fast import prepareDigiRecoMixing 

#call to customisation function prepareDigiRecoMixing imported from FastSimulation.Configuration.MixingModule_Full2Fast
process = prepareDigiRecoMixing(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff import miniAOD_customizeMETFiltersFastSim 

#call to customisation function miniAOD_customizeMETFiltersFastSim imported from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
process = miniAOD_customizeMETFiltersFastSim(process)

# End of customisation functions
