import ROOT
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

events_new = Events(['~/eos/cms/store/group/phys_jetmet/schoef/pickEvents/jack_metTailPhys14_susyHadronic/merged_bad_GEN-SIM_rereco_740_newPFHadCalib.root'])
#events_old = Events(['~/eos/cms/store/group/phys_jetmet/schoef/pickEvents/jack_metTailPhys14_susyHadronic/merged_bad_GEN-SIM.root'])

edmCollections = [ {'name':'pfMet', 'label':("pfMet"), 'edmType':"vector<reco::PFMET>"} ]
handles={v['name']:Handle(v['edmType']) for v in edmCollections}
for i in range(events_new.size()):
  events_new.to(i)
  products_new = {}
  for v in edmCollections:
    events_new.getByLabel(v['label'],handles[v['name']])
    products_new[v['name']] =handles[v['name']].product()
#  events_old.to(i)
#  products_old = {}
#  for v in edmCollections:
#    events_old.getByLabel(v['label'],handles[v['name']])
#    products_old[v['name']] =handles[v['name']].product()

  print "new",products_new['pfMet'][0].pt()#, 'old', products_old['pfMet'][0].pt()
