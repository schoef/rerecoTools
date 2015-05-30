import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *
from math import sqrt
small=True

#events = Events(['file:crab_test.root'])
#events = Events(['root://eoscms.cern.ch//store/group/phys_jetmet/schoef/741_relval_rereco/RelValQCD_FlatPt_15_3000HS_13_CMSSW_7_4_1-MCRUN2_74_V9_gensim71X-v1_PhilFixRecHitFlag/crab_test_10.root'])

events = Events(['file:/afs/cern.ch/user/k/kfiekas/public/TTBAROldM2.root'])
#events = Events(['file:/afs/cern.ch/user/k/kfiekas/public/TTBARNewM2.root'])

#events = Events('file:/afs/cern.ch/user/k/kfiekas/public/TTBARNewM2.root')

#/afs/cern.ch/user/k/kfiekas/public/TTBAROldM2.root
#/afs/cern.ch/user/k/kfiekas/public/TTBARNewM2.root

edmCollections = {
#  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "Cleaned", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
#  'pfRecHits':{'label':("particleFlowRecHitHBHE", "", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
#  'pfClusters':{'label':("particleFlowClusterHCAL", "",  "RECO2"), 'edmType':"vector<reco::PFCluster>"},
  'pfClusters':{'label':("particleFlowClusterECAL", "",  "RECO2"), 'edmType':"vector<reco::PFCluster>"},

#  'caloRecHits': {'label':("hbhereco", "",  "RECO2"), 'edmType':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >'},
#   'ecalRecHits': {'edmType':'vector<reco::PFRecHit>', 'label': ( "particleFlowRecHitECAL",    "Cleaned",         "RECO2") }

#  'jets':{'label':("ak4PFJetsCHS","","RECO2"), 'edmType':'vector<reco::PFJet>'}
#  'pfCandidates':{'label':("particleFlow","","RECO2"), 'edmType':'vector<reco::PFCandidate>'}
   }
handles={v:Handle(edmCollections[v]['edmType']) for v in edmCollections.keys()}

def getProd(name):
  events.getByLabel(edmCollections[name]['label'],handles[name])
  return handles[name].product()

nevents = 1 if small else events.size()
for i in range(nevents):
  events.to(i)
  eaux=events.eventAuxiliary()
  run=eaux.run()
  event=eaux.event()
  lumi=eaux.luminosityBlock()
  print ":".join(str(x) for x in [run, lumi, event])
### start with pfCandidates
#  pfCandidates = getProd('pfCandidates') 
#  for i_c, c in enumerate(pfCandidates):
##    if c.particleId()==2: print "Candidate %i type  %i energy %5.2f  eta %5.2f phi %5.2f" % (i_c,c.particleId(),c.energy(),c.eta(),c.phi())
##    if c.particleId()==4 and c.energy()>20: print "Candidate %i type  %i energy %5.2f eta %5.2f phi %5.2f" % (i_c,c.particleId(),c.energy(),c.eta(),c.phi())
#    if sqrt((c.eta()-1.08)**2+(c.phi()-3.01)**2)<0.12: print "Candidate %i type  %i energy %5.2f pt %5.2f eta %5.2f phi %5.2f" % (i_c,c.particleId(),c.energy(),c.pt(),c.eta(),c.phi())

## start with pfClusters
#  caloRecHits = getProd('caloRecHits')
  pfClusters = getProd('pfClusters') 
  for i_c, c in enumerate(pfClusters):
    hitsAndFractions = c.hitsAndFractions()
    recHitMultiplicity = len(hitsAndFractions)
    print "Cluster %i energy %5.2f corrected energy %5.2f recHitMultiplicity %i" % (i_c,c.energy(),c.correctedEnergy(),recHitMultiplicity)
#    clusterE=0.
#    for detid, fraction in hitsAndFractions:
#      calo_rh = [crh for crh in  caloRecHits if crh.detid()==detid]
#      calo_rh = calo_rh[0] if len(calo_rh)==1 else None
#      if calo_rh:
#        clusterE+=calo_rh.energy()*fraction
#        print "pfRecHit fraction: %5.5f calo RH energy:%5.2f"% (fraction, calo_rh.energy())
#      else:
#        print "No calo rechit found for PFRecHit detId -> should not happen"%detid
#    print "sum of weighted Rechit energies: %10.6f should agree with PFClusterEnergy %10.6f" %(clusterE, c.energy())
   
## start with pfRecHits 
#  pfRecHits = getProd('pfRecHits')
#  caloRecHits = getProd('caloRecHits')
#  print run,lumi,event,"PFRecHitsHBHE:",pfRecHits.size(), "CaloRecHits", caloRecHits.size()
#  #find PFRecHits
#  for i_pf, pf_rh in enumerate(pfRecHits):
#    calo_rh = [crh for crh in  caloRecHits if crh.detid().rawId()==pf_rh.detId()]
#    calo_rh = calo_rh[0] if len(calo_rh)==1 else None
#    if calo_rh:
#      print "For PF RecHitHBHE %3i with energy %7.3f found Calo HBHERecHit with energy %7.3f and aux %i"%(i_pf, pf_rh.energy(), calo_rh.energy(), calo_rh.aux())
#    else:
#      print "For PF RecHitHBHE %3i with energy %7.3f found no Calo HBHERecHit"%(i_pf, pf_rh.energy())

###start with jets
#  jets = getProd("jets")
#  for j in jets[:1]:
#    print "jet pt",j.pt()
#    cons=j.getPFConstituents()
#    print "constituents:",cons.size()
#    for i_c, c in enumerate(cons):
#      eib=c.elementsInBlocks()
#      print "Elements in Block for constituent",i_c," of type ",c.particleId(),":", eib.size()
