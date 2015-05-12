import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

#events = Events(['root://eoscms.cern.ch//store/group/phys_jetmet/schoef/pickEvents/muTails_Phys14/720_step3_RECO.root'])
events = Events(['file:crab_test.root'])


#edmCollections = [ {'name':'pfMet', 'label':("pfMet"), 'edmType':"vector<reco::PFMET>"} ]
edmCollections = [ 
#  {'name':'pfMet', 'label':("slimmedMETs"), 'edmType':"vector<pat::MET>"},
#  {'name':'triggerResults', 'label':("TriggerResults","","PAT"), 'edmType':"edm::TriggerResults"},
#  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "Cleaned", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
  {'name':'pfClusters', 'label':("particleFlowClusterHBHE", "",  "RECO2"), 'edmType':"vector<reco::PFCluster>"}
   ]
handles={v['name']:Handle(v['edmType']) for v in edmCollections}
for i in range(events.size()):
  events.to(i)
  eaux=events.eventAuxiliary()
  run=eaux.run()
  event=eaux.event()
  lumi=eaux.luminosityBlock()

  products = {}
  for v in edmCollections:
    events.getByLabel(v['label'],handles[v['name']])
    products[v['name']] =handles[v['name']].product()
#  events_old.to(i)
#  products_old = {}
#  for v in edmCollections:
#    events_old.getByLabel(v['label'],handles[v['name']])
#    products_old[v['name']] =handles[v['name']].product()

  cl=[]
  print run,lumi,event,products['pfClusters'].size()
  for j in range(products['pfClusters'].size()):
    cl.append(products['pfClusters'][j])
#  print run,lumi,event,products['pfRecHitsHBHE'].size()
#  rh=[]
#  for j in range(products['pfRecHitsHBHE'].size()):
#    print type(products['pfRecHitsHBHE'][j].originalRecHit()), products['pfRecHitsHBHE'][j].originalRecHit()
#    rh.append(products['pfRecHitsHBHE'][j].originalRecHit())
