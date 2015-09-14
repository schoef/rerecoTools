import ROOT
from array import array
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

ROOT.gStyle.SetOptStat(0)
small=False
verbose=False

edmCollections = {
#  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "Cleaned", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
#  'pfRecHits':{'label':("particleFlowRecHitHBHE", "", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
#  'pfClusters':{'label':("particleFlowClusterHBHE", "",  "RECO2"), 'edmType':"vector<reco::PFCluster>"},
  'caloRecHits': {'label':("hbhereco", "",  "RECO"), 'edmType':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >'},
#  'jets':{'label':("ak4PFJetsCHS","","RECO"), 'edmType':'vector<reco::PFJet>'}
  'vertices':{'label':("offlinePrimaryVertices", "", "RECO"), 'edmType':'vector<reco::Vertex>'},
  'puInfo':{'label':("addPileupInfo", "", "HLT"), 'edmType':'vector<PileupSummaryInfo>'}
   }



handles={v:Handle(edmCollections[v]['edmType']) for v in edmCollections.keys()}

def getProd(name, events):
  events.getByLabel(edmCollections[name]['label'],handles[name])
  return handles[name].product()

nfiles=3
small = False
nMax=10000
m0Threshold=200

from files import QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74_Asympt25nsRecodebug_MCRUN2_74_V9_v1, QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74_Asympt50nsRecodebug_MCRUN2_74_V9A_v2
events = {
  '25ns': Events(QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74_Asympt25nsRecodebug_MCRUN2_74_V9_v1[:nfiles]),
  '50ns': Events(QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74_Asympt50nsRecodebug_MCRUN2_74_V9A_v2[:nfiles])
}

ratio = {
  '25ns':ROOT.TProfile('m2_over_m0_25ns', 'm2_over_m0', 10,0,50,0,2),
  '50ns':ROOT.TProfile('m2_over_m0_50ns', 'm2_over_m0', 10,0,50,0,2),
  }

for key in ['50ns', '25ns' ]:
  nevents = 10 if small else events[key].size()
  count=0
  for i in range(nevents):
    events[key].to(i)
    if i%10==0:print "At event %i/%i"%(i,nevents)
  #  eaux=events.eventAuxiliary()
  #  run=eaux.run()
  #  event=eaux.event()
  #  lumi=eaux.luminosityBlock()

    puInfo = getProd('puInfo', events[key])
    nVertTrue=-1
    for bx in puInfo:
      if bx.getBunchCrossing()==-1:
#        nVertTrue = bx.getTrueNumInteractions()
        nVertTrueBXm1 = bx.getPU_NumInteractions()
      if bx.getBunchCrossing()==0:
#        nVertTrue = bx.getTrueNumInteractions()
        nVertTrue = bx.getPU_NumInteractions()
        break
    nVert = getProd('vertices', events[key]).size()
#    print nVertTrue, nVertTrueBXm1, nVert
    caloRecHits = getProd('caloRecHits', events[key])
    done = False
    for crh in caloRecHits:
      if crh.eraw()>m0Threshold:
  #      print nVert, crh.energy()/crh.eraw()
#        ratio[key].Fill(nVertTrueBXm1, crh.energy()/crh.eraw())
        ratio[key].Fill(nVertTrue, crh.energy()/crh.eraw())
        if count%100==0:print count
        count+=1
        if count>nMax:
          done=True
          break
    if done:
      break

c1 = ROOT.TCanvas()
l = ROOT.TLegend(0.75,0.74,0.99,0.99)
l.SetFillColor(0)
l.SetShadowColor(ROOT.kWhite)
l.SetBorderSize(1)

ratio['50ns'].Draw() 
ratio['50ns'].SetLineColor(ROOT.kRed) 
ratio['50ns'].GetXaxis().SetTitle("gen vertex multiplicity") 
ratio['50ns'].GetYaxis().SetTitle("calo rechit energy ratio M2/M0") 
ratio['50ns'].SetTitle("") 
ratio['50ns'].GetYaxis().SetRangeUser(0.8,1.1) 
l.AddEntry(ratio['50ns'],"50ns")

ratio['25ns'].Draw('same') 
ratio['25ns'].GetXaxis().SetTitle("vertex multiplicity") 
ratio['25ns'].GetYaxis().SetTitle("calo rechit energy ratio M2/M0") 
ratio['25ns'].SetTitle("") 
l.AddEntry(ratio['25ns'],"25ns")

#
#c1.SetLogx() 
c1.RedrawAxis()
ROOT.gStyle.SetOptStat(0)
l.Draw()
c1.Print("/afs/hephy.at/user/r/rschoefbeck/www/pngRecHit/M2_over_M0_nVertTrue.png")
