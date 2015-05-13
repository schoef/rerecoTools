import ROOT
from array import array
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small=False
verbose=False

#events = Events(['file:crab_test.root'])
events = Events(['root://eoscms.cern.ch//store/group/phys_jetmet/schoef/741_relval_rereco/RelValQCD_FlatPt_15_3000HS_13_CMSSW_7_4_1-MCRUN2_74_V9_gensim71X-v1_PhilFixRecHitFlag/crab_test_10.root'])
edmCollections = {
#  {'name':'pfRecHitsHBHE', 'label':("particleFlowRecHitHBHE", "Cleaned", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
  'pfRecHits':{'label':("particleFlowRecHitHBHE", "", "RECO2"), 'edmType':"vector<reco::PFRecHit>"},
#  'pfClusters':{'label':("particleFlowClusterHBHE", "",  "RECO2"), 'edmType':"vector<reco::PFCluster>"},
  'caloRecHits': {'label':("hbhereco", "",  "RECO2"), 'edmType':'edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit> >'},
  'jets':{'label':("ak4PFJetsCHS","","RECO2"), 'edmType':'vector<reco::PFJet>'}
   }
handles={v:Handle(edmCollections[v]['edmType']) for v in edmCollections.keys()}

def getProd(name):
  events.getByLabel(edmCollections[name]['label'],handles[name])
  return handles[name].product()

nevents = 10 if small else events.size()
binning=range(20)+[x*10 for x in range(2,20)]+[x*100 for x in range(2,20)]
m0_energy  = ROOT.TH1F("m0_energy","m0_energy",len(binning)-1,array('d',binning))
m21_energy = ROOT.TH1F("m21_energy","m21_energy",len(binning)-1,array('d',binning))
m23_energy = ROOT.TH1F("m23_energy","m23_energy",len(binning)-1,array('d',binning))
#m0_multiplicity  = ROOT.TH1F("m0_multiplicity","m0_multiplicity",len(binning)-1,array('d',binning))
#m21_multiplicity = ROOT.TH1F("m21_multiplicity","m21_multiplicity",len(binning)-1,array('d',binning))
#m23_multiplicity = ROOT.TH1F("m23_multiplicity","m23_multiplicity",len(binning)-1,array('d',binning))
for i in range(nevents):
  events.to(i)
  if i%10==0:print "At event %i/%i"%(i,nevents)
#  eaux=events.eventAuxiliary()
#  run=eaux.run()
#  event=eaux.event()
#  lumi=eaux.luminosityBlock()

  caloRecHits = getProd('caloRecHits')
  for i_crh, crh in enumerate(caloRecHits):
    if crh.aux()==0:   m0_energy.Fill(crh.energy())
    if crh.aux()==1:   m21_energy.Fill(crh.energy())
    if crh.aux()==2:   m23_energy.Fill(crh.energy())

for h in [m0_energy, m21_energy, m23_energy]:
  for i in range(0,h.GetNbinsX()+1):
    h.SetBinError(i,0)
 
c1 = ROOT.TCanvas()

l = ROOT.TLegend(0.3,0.8,0.6,1.0)
l.SetFillColor(0)
l.SetShadowColor(ROOT.kWhite)
l.SetBorderSize(1)

m0_21_energy=m0_energy.Clone()
m0_21_energy.Add(m21_energy)
tot_energy=m0_21_energy.Clone()
tot_energy.Add(m23_energy)

m0_energy_frac=m0_energy.Clone()
m0_energy_frac.Divide(tot_energy)
m0_21_energy_frac=m0_21_energy.Clone()
m0_21_energy_frac.Divide(tot_energy)
tot_energy_frac=tot_energy.Clone()
tot_energy_frac.Divide(tot_energy)

m0_energy_frac.Draw('h') 
m0_energy_frac.GetXaxis().SetTitle("calo RecHit energy") 
m0_energy_frac.GetYaxis().SetTitle("energy fraction per HCAL method") 
m0_energy_frac.SetTitle("") 
m0_energy_frac.GetYaxis().SetRangeUser(0,1) 
l.AddEntry(m0_energy_frac,"M0")
m0_21_energy_frac.SetLineColor(ROOT.kRed) 
m0_21_energy_frac.Draw("hsame")
l.AddEntry(m0_21_energy_frac,"M2 (1pulse)")
l.Draw()
c1.SetLogx() 
#tot_energy_frac.SetLineColor(ROOT.kGreen) 
#tot_energy_frac.Draw("hsame") 
c1.RedrawAxis()
#c1.Print("/afs/hephy.at/user/s/schoefbeck/www/pngCluster/recHit_energy_fraction.png")
c1.Print("recHit_energy_fraction.png")
