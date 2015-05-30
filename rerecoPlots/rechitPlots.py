import ROOT
from array import array
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

ROOT.gStyle.SetOptStat(0)
small=False
verbose=False

#events = Events(['root://eoscms.cern.ch//store/group/phys_jetmet/schoef/741_relval_rereco/RelValQCD_FlatPt_15_3000HS_13_CMSSW_7_4_1-MCRUN2_74_V9_gensim71X-v1_PhilFixRecHitFlag/crab_test_10.root'])

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

binning=range(20)+[x*10 for x in range(2,20)]+[x*100 for x in range(2,20)]
m0_energy  = ROOT.TH1F("m0_energy","m0_energy",len(binning)-1,array('d',binning))
m21_energy = ROOT.TH1F("m21_energy","m21_energy",len(binning)-1,array('d',binning))
m23_energy = ROOT.TH1F("m23_energy","m23_energy",len(binning)-1,array('d',binning))
#m0_multiplicity  = ROOT.TH1F("m0_multiplicity","m0_multiplicity",len(binning)-1,array('d',binning))
#m21_multiplicity = ROOT.TH1F("m21_multiplicity","m21_multiplicity",len(binning)-1,array('d',binning))
#m23_multiplicity = ROOT.TH1F("m23_multiplicity","m23_multiplicity",len(binning)-1,array('d',binning))

from files import *
events = Events(RelValZMM_13_CMSSW_7_4_1_MCRUN2_74_V9_gensim_740pre7_v1_PhilFixRecHitFlag)
prefix="RelValZMM_13_CMSSW_7_4_1-MCRUN2_74_V9_gensim_740pre7-v1_PhilFixRecHitFlag"

#events = Events(RelValZMM_13_CMSSW_7_4_1_PU25ns_MCRUN2_74_V9_gensim_740pre7_v1_PhilFixRecHitFlag)
#prefix="RelValZMM_13_CMSSW_7_4_1_PU25ns_MCRUN2_74_V9_gensim_740pre7_v1_PhilFixRecHitFlag"

#events = Events(RelValZMM_13_CMSSW_7_4_1_PU50ns_MCRUN2_74_V8_gensim_740pre7_v1_PhilFixRecHitFlag)
#prefix="RelValZMM_13_CMSSW_7_4_1_PU50ns_MCRUN2_74_V8_gensim_740pre7_v1_PhilFixRecHitFlag"

nevents = 10 if small else events.size()
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
l = ROOT.TLegend(0.75,0.74,0.99,0.99)
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

m0_energy_frac.SetLineColor(ROOT.kBlue) 
m0_energy_frac.SetFillColor(ROOT.kBlue) 
m0_21_energy_frac.SetLineColor(ROOT.kRed) 
m0_21_energy_frac.SetFillColor(ROOT.kRed) 
tot_energy_frac.SetLineColor(ROOT.kGreen) 
tot_energy_frac.SetFillColor(ROOT.kGreen) 

tot_energy_frac.Draw() 
tot_energy_frac.GetXaxis().SetTitle("calo RecHit energy") 
tot_energy_frac.GetYaxis().SetTitle("energy fraction per HCAL method") 
tot_energy_frac.SetTitle("") 
tot_energy_frac.GetYaxis().SetRangeUser(0,1) 
l.AddEntry(tot_energy_frac,"M2 (3-pulse)")
m0_21_energy_frac.Draw("same")
l.AddEntry(m0_21_energy_frac,"M2 (1pulse)")
m0_energy_frac.Draw('same') 
l.AddEntry(m0_energy_frac,"M0")

c1.SetLogx() 
c1.RedrawAxis()
ROOT.gStyle.SetOptStat(0)
#c1.Print("/afs/hephy.at/user/s/schoefbeck/www/pngCluster/recHit_energy_fraction.png")
l.Draw()
c1.Print("recHit_energy_fraction_"+prefix+".png")
