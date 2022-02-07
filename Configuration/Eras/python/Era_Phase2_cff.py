import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Modifier_phase2_common_cff import phase2_common
from Configuration.Eras.Modifier_phase2_tracker_cff import phase2_tracker
from Configuration.Eras.Modifier_phase2_ecal_cff import phase2_ecal
from Configuration.Eras.Modifier_trackingPhase2PU140_cff import trackingPhase2PU140
from Configuration.Eras.Modifier_phase2_hcal_cff import phase2_hcal
from Configuration.Eras.Modifier_phase2_hgcal_cff import phase2_hgcal
from Configuration.Eras.Modifier_phase2_muon_cff import phase2_muon
from Configuration.Eras.Modifier_phase2_GEM_cff import phase2_GEM
from Configuration.Eras.Modifier_phase1Pixel_cff import phase1Pixel
from Configuration.Eras.Modifier_trackingPhase1_cff import trackingPhase1
from Configuration.Eras.Modifier_hcalHardcodeConditions_cff import hcalHardcodeConditions
from Configuration.Eras.Modifier_phase2_timing_cff import phase2_timing
from Configuration.Eras.Modifier_phase2_timing_layer_cff import phase2_timing_layer
from Configuration.Eras.Modifier_phase2_trigger_cff import phase2_trigger
from Configuration.Eras.Modifier_run3_GEM_cff import run3_GEM

Phase2 = cms.ModifierChain(Run3.copyAndExclude([phase1Pixel,trackingPhase1,run3_GEM]), phase2_common, phase2_tracker, trackingPhase2PU140, phase2_ecal, phase2_hcal, phase2_hgcal,phase2_muon,phase2_GEM,hcalHardcodeConditions, phase2_timing, phase2_timing_layer, phase2_trigger)

#Phase2 = cms.ModifierChain(Run3.copyAndExclude([phase1Pixel,trackingPhase1,run3_GEM]), phase2_common, phase2_tracker, trackingPhase2PU140, phase2_ecal, phase2_hcal, phase2_hgcal,phase2_GEM,hcalHardcodeConditions, phase2_timing, phase2_timing_layer, phase2_trigger)

#Phase2 = cms.ModifierChain(Run3.copyAndExclude([phase1Pixel,trackingPhase1]), phase2_common, phase2_tracker, trackingPhase2PU140, phase2_ecal, phase2_hcal, phase2_hgcal,hcalHardcodeConditions,phase2_timing, phase2_timing_layer, phase2_trigger)
#removed phase2_hgcal:Not Implemented in FastSim yet
