import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small=True

events = Events(['file:crab_test.root'])
edmCollections = [ 
#  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "Cleaned", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
#  {'name':'pfClusters', 'label':("particleFlowClusterHBHE", "",  "RECO2"), 'edmType':"vector<reco::PFCluster>"}
  {'name':'hbheRechits','edmType':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >', 'label':("hbhereco", "",  "RECO2")}
   ]
handles={v['name']:Handle(v['edmType']) for v in edmCollections}

nevents = 1 if small else events.size()
for i in range(nevents):
  events.to(i)
  eaux=events.eventAuxiliary()
  run=eaux.run()
  event=eaux.event()
  lumi=eaux.luminosityBlock()

  #read all products
  products = {}
  for v in edmCollections:
    events.getByLabel(v['label'],handles[v['name']])
    products[v['name']] =handles[v['name']].product()

  print run,lumi,event,"PFRecHitsHBHE:",products["pfRecHitsHBHE"].size(), "CaloRecHits",products["hbheRechits"].size()
  
  #find PFRecHits
  for i_pf, pf_rh in enumerate(products["pfRecHitsHBHE"]):
    calo_rh = [crh for crh in  products["hbheRechits"] if crh.detid().rawId()==pf_rh.detId()]
    calo_rh = calo_rh[0] if len(calo_rh)==1 else None
    if calo_rh:
      print "For PF RecHitHBHE %3i with energy %7.3f found Calo HBHERecHit with energy %7.3f and aux %i"%(i_pf, pf_rh.energy(), calo_rh.energy(), calo_rh.aux())
    else:
      print "For PF RecHitHBHE %3i with energy %7.3f found no Calo HBHERecHit"%(i_pf, pf_rh.energy())
  
#  cl=[]
#  print run,lumi,event,products['pfClusters'].size()
#  for j in range(products['pfClusters'].size()):
#    cl.append(products['pfClusters'][j])

#  rh=[]
#  for j in range(products['pfRecHitsHBHE'].size()):
#    print type(products['pfRecHitsHBHE'][j].originalRecHit()), products['pfRecHitsHBHE'][j].originalRecHit()
#    rh.append(products['pfRecHitsHBHE'][j].originalRecHit())
