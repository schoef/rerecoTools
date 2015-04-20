import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

#events = Events(['root://eoscms.cern.ch//store/group/phys_jetmet/schoef/pickEvents/muTails_Phys14/720_step3_RECO.root'])
events = Events(['root://eoscms.cern.ch//store/group/phys_jetmet/schoef/pickEvents/muTails_Phys14/720_phys14_qcd_mAOD.root'])


#edmCollections = [ {'name':'pfMet', 'label':("pfMet"), 'edmType':"vector<reco::PFMET>"} ]
edmCollections = [ {'name':'pfMet', 'label':("slimmedMETs"), 'edmType':"vector<pat::MET>"} ]
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

  print run,lumi,event, products['pfMet'][0].shiftedPt(12,0), products['pfMet'][0].pt()#, 'old', products_old['pfMet'][0].pt()
