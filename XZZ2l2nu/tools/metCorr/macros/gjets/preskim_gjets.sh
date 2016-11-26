#!/bin/sh



# compile
g++ preskim_gjets.cc -o preskim_gjets.exe `root-config --cflags` `root-config --libs`

#samples="SinglePhoton_Run2016H_PromptReco_new"
#samples="SinglePhoton_Run2016B2H_ReReco_36p1fbinv"
#samples="DYJets*"
#samples="ZJetsToNuNu_HT*_BIG"
#samples="W*"
#samples="GJet_Pt*"
samples="GJets_HT*"
#samples="QCD_*_BIG"
#samples="QCD_*_EMEnriched"
#samples="T*"
indir=/data2/XZZ2/80X_20161029_GJets
outdir=/home/heli/XZZ/80X_20161029_GJets_light

mkdir -p $outdir

#for dd in ${indir}/*/vvTreeProducer;
#for dd in ${indir}/SinglePhoton_Run2016BCD_PromptReco/vvTreeProducer;
#for dd in ${indir}/SinglePhoton_Run2016B2G_PromptReco/vvTreeProducer;
#for dd in ${indir}/SinglePhoton_Run2016B2H29fbinv_PromptReco/vvTreeProducer;
for dd in ${indir}/${samples}/vvTreeProducer;
do 
  infile="${dd}/tree.root";
  oo="${dd/$indir/$outdir}";
  outfile="${oo}/tree_light.root";
  echo mkdir -p $oo;
  mkdir -p $oo ;
  echo "./preskim_gjets.exe $infile $outfile &> ${outfile}.log & "
  ./preskim_gjets.exe $infile $outfile &> ${outfile}.log &
done



# wait and replace old one

wait

#for dd in  ${indir}/* ;
#for dd in  ${indir}/SinglePhoton_Run2016BCD_PromptReco ;
for dd in  ${indir}/${samples} ;
do
  echo $dd;
  ddo=${dd/$indir/$outdir}
  echo "mkdir -p ${ddo} " 
  mkdir -p ${ddo}

  for dd2 in ${dd}/* ;
  do
    if [[ ${dd2} != *"vvTree"* ]]; then
      #echo $dd2;
      #ddo2="${dd2/$indir/$outdir} "
      #echo "cp -rp $dd2 $ddo2 " 
      #cp -rp $dd2 $ddo2
      echo "cp -rp $dd2 $ddo/ " 
      cp -rp $dd2 $ddo/
    fi
  done;

  ttin="${ddo/_light/}/vvTreeProducer"

#  echo "cp -rp $ttin $ddo/"
#  cp -rp $ttin $ddo/
  mkdir -p $ddo/vvTreeProducer
  echo "mv $ddo/vvTreeProducer/tree_light.root $ddo/vvTreeProducer/tree.root"
  rm $ddo/vvTreeProducer/tree.root
  mv $ddo/vvTreeProducer/tree_light.root $ddo/vvTreeProducer/tree.root
done
