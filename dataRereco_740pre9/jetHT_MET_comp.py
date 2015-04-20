import ROOT
cOld = ROOT.TChain("Events")
cOld.Add("/data/schoef/local/METtree_JetHT_oldPFHCalib.root")
cNew = ROOT.TChain("Events")
cNew.Add("/data/schoef/local/METtree_JetHT_newPFHCalib.root")

cOld.Draw("met_rawPt>>hOld(100,0,10000)","","goff")
cOld.Draw("met_rawPt>>hOldF(100,0,10000)","Flag_METFilters","goff")
cNew.Draw("met_rawPt>>hNewF(100,0,10000)","Flag_METFilters","goff")

hOld = ROOT.gDirectory.Get("hOld")
hOld.SetLineColor(ROOT.kGray)
hOld.SetTitle("")
hOldF = ROOT.gDirectory.Get("hOldF")
hNewF = ROOT.gDirectory.Get("hNewF")
hNewF.SetLineColor(ROOT.kRed)

c1 = ROOT.TCanvas()
hOld.Draw()
c1.SetLogy()
hOldF.Draw("same")
hNewF.Draw("same")

l = ROOT.TLegend(0.6,0.7,0.99,0.95)
l.AddEntry(hOld,"before filters")
l.AddEntry(hOldF,"old calibration")
l.AddEntry(hNewF,"new calibration")
l.Draw()
c1.Print("/afs/hephy.at/user/s/schoefbeck/www/etc/jetht_rawmet_wide.png")
