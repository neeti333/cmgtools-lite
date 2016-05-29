from CMGTools.XZZ2l2nu.analyzers.AutoFillTreeProducer  import * 
import math


LLType = NTupleObjectType("LLType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("mt",   lambda x : x.mt(), float),       
    NTupleVariable("deltaPhi",   lambda x : x.deltaPhi(), float),       
    NTupleVariable("deltaR",   lambda x : x.deltaR(), float),       
])



VVType = NTupleObjectType("VVType", baseObjectTypes=[], variables = [
  NTupleSubObject("LV",  lambda x : x['pair'],fourVectorType),
  NTupleVariable("deltaPhi",   lambda x : x['pair'].deltaPhi(), float),       
  NTupleVariable("deltaR",   lambda x : x['pair'].deltaR(), float),       
  NTupleVariable("mt",   lambda x : x['pair'].mt(), float),       
  NTupleVariable("mta",   lambda x : x['pair'].mta(), float),       
  NTupleVariable("mtb",   lambda x : x['pair'].mtb(), float),       
  NTupleVariable("mtc",   lambda x : x['pair'].mtc(), float),   
])


LLNuNuType = NTupleObjectType("LLNuNuType", baseObjectTypes=[VVType], variables = [
    NTupleSubObject("l1",  lambda x : x['pair'].leg1,LLType),
    NTupleSubObject("l1_l1",  lambda x : x['pair'].leg1.leg1,leptonTypeExtra),
    NTupleSubObject("l1_l2",  lambda x : x['pair'].leg1.leg2,leptonTypeExtra),
    NTupleSubObject("l2",  lambda x : x['pair'].leg2,metType),
    NTupleVariable("CosdphiZMet",   lambda x : math.cos(x['pair'].deltaPhi()), float), 
    NTupleVariable("CosZdeltaPhi",   lambda x : math.cos(x['pair'].leg1.deltaPhi()), float), 
    NTupleVariable("dPTPara",   lambda x : math.fabs(x['pair'].leg1.pt() + x['pair'].leg2.pt() * math.cos(x['pair'].deltaPhi())), float), 
    NTupleVariable("dPTParaRel",   lambda x : math.fabs(x['pair'].leg1.pt() + x['pair'].leg2.pt() * math.cos(x['pair'].deltaPhi()))/(x['pair'].leg1.pt()), float), 
    NTupleVariable("dPTPerp",   lambda x : math.fabs(x['pair'].leg2.pt() * math.sin(x['pair'].deltaPhi())), float), 
    NTupleVariable("dPTPerpRel",   lambda x : math.fabs(x['pair'].leg2.pt() * math.sin(x['pair'].deltaPhi()))/(x['pair'].leg1.pt()), float), 
    NTupleVariable("metOvSqSET",   lambda x : (x['pair'].leg2.pt())/math.sqrt(x['pair'].leg2.sumEt()), float), 
      
])

llpairType = NTupleObjectType("llpairType", baseObjectTypes=[], variables = [
    NTupleSubObject("Z",  lambda x : x,LLType),
    NTupleSubObject("l1",  lambda x : x.leg1,leptonType),
    NTupleSubObject("l2",  lambda x : x.leg2,leptonType),
])


JetType = NTupleObjectType("JetType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("area",   lambda x : x.jetArea(), float),
    NTupleVariable("rawFactor",   lambda x : x.rawFactor(), float),
#    NTupleVariable("btag",   lambda x : x.bTag(), float),
#    NTupleVariable("nConstituents",   lambda x : len(x.constituents), int),
    # NTupleVariable("looseID",   lambda x : x.looseID, int),
    # NTupleVariable("tightID",   lambda x : x.tightID, int),
    # NTupleVariable("chargedHadronEnergyFraction",   lambda x : x.chargedHadronEnergyFraction(), float),
    # NTupleVariable("neutralHadronEnergyFraction",   lambda x : x.neutralHadronEnergyFraction(), float),
    # NTupleVariable("photonEnergyFraction",   lambda x : x.photonEnergyFraction(), float),
    # NTupleVariable("HFHadronEnergyFraction",   lambda x : x.HFHadronEnergyFraction(), float),
    # NTupleVariable("HFEMEnergyFraction",   lambda x : x.HFEMEnergyFraction(), float),
    # NTupleVariable("muonEnergyFraction",   lambda x : x.muonEnergyFraction(), float),
    # NTupleVariable("electronEnergyFraction",   lambda x : x.electronEnergyFraction(), float),
    # NTupleVariable("leptonEnergyFraction",   lambda x : x.leptonEnergyFraction(), float),

])

corrJetType = NTupleObjectType("corrJetType", baseObjectTypes=[JetType], variables = [
    NTupleVariable("jec_corr",   lambda x : x.corr, float), # JEC correction factor 
    NTupleVariable("jec_corrUp",   lambda x : x.corrJECUp if hasattr(x,"corrJECUp") else  1.0 ,float), 
    NTupleVariable("jec_corrDown",   lambda x : x.corrJECDown if hasattr(x,"corrJECDown") else  1.0 ,float), 
    NTupleVariable("jer_corr",   lambda x : x.corrJER if hasattr(x,"corrJER") else  1.0 ,float), # JER correction factor
])
