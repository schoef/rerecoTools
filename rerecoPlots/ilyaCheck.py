import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small=True

events = Events(['file:SMP-RunIIFall15DR76-00032.root'])
edmCollections = [ 
  # {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE"), 'edmType':"vector<reco::PFRecHit>"},
    {'name':'pfMet', 'label':('pfMet'), 'edmType':'vector<reco::PFMET>'},
   #{'name':'caloRecHits', 'label':("reducedHcalRecHits"), 'edmType':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >'},
    {'name':'pf', 'label':('particleFlow'), 'edmType':'vector<reco::PFCandidate>'}
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

  print run,lumi,event#,"caloRecHits:",products["caloRecHits"].size()
  
  #find PFRecHits
#  for i, rh in enumerate(products["caloRecHits"]):
#    print "n %i E %3.2f"%(i, rh.energy())
