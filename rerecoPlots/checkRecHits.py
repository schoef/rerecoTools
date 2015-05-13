import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small=True

#events = Events(['file:crab_test.root'])
events = Events(['root://eoscms.cern.ch//store/group/phys_jetmet/schoef/741_relval_rereco/RelValQCD_FlatPt_15_3000HS_13_CMSSW_7_4_1-MCRUN2_74_V9_gensim71X-v1_PhilFixRecHitFlag/crab_test_10.root'])
edmCollections = {
#  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "Cleaned", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
  'pfRecHits':{'label':("particleFlowRecHitHBHE", "", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
  'pfClusters':{'label':("particleFlowClusterHBHE", "",  "RECO2"), 'edmType':"vector<reco::PFCluster>"},
  'caloRecHits': {'label':("hbhereco", "",  "RECO2"), 'edmType':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >'},
#  'jets':{'label':("ak4PFJetsCHS","","RECO2"), 'edmType':'vector<reco::PFJet>'}
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

## start with pfClusters
  pfClusters = getProd('pfClusters') 
  caloRecHits = getProd('caloRecHits')
  for i_c, c in enumerate(pfClusters):
    hitsAndFractions = c.hitsAndFractions()
    recHitMultiplicity = len(hitsAndFractions)
    print "\nCluster %i energy %5.2f recHitMultiplicity %i" % (i_c,c.energy(),recHitMultiplicity)
    clusterE=0.
    for detid, fraction in hitsAndFractions:
      calo_rh = [crh for crh in  caloRecHits if crh.detid()==detid]
      calo_rh = calo_rh[0] if len(calo_rh)==1 else None
      if calo_rh:
        clusterE+=calo_rh.energy()*fraction
        print "pfRecHit fraction: %5.5f calo RH energy:%5.2f reco method enum: %i"% (fraction, calo_rh.energy(), calo_rh.aux())
      else:
        print "No calo rechit found for PFRecHit detId -> should not happen"%detid
    print "sum of weighted Rechit energies: %10.6f should agree with PFClusterEnergy %10.6f" %(clusterE, c.energy())
   
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
