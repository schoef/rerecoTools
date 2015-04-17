import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

events_new = Events(['step3_newCalib.root'])
events_old = Events(['step3_RAW2DIGI_RECO.root'])

edmCollections = [ {'name':'pfMet', 'label':("pfMet"), 'edmType':"vector<reco::PFMET>"} ]
handles={v['name']:Handle(v['edmType']) for v in edmCollections}
for i in range(10):
  events_new.to(i)
  products_new = {}
  for v in edmCollections:
    events_new.getByLabel(v['label'],handles[v['name']])
    products_new[v['name']] =handles[v['name']].product()
  events_old.to(i)
  products_old = {}
  for v in edmCollections:
    events_old.getByLabel(v['label'],handles[v['name']])
    products_old[v['name']] =handles[v['name']].product()

  print "new",products_new['pfMet'][0].pt(), 'old', products_old['pfMet'][0].pt()
