#!/bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/scripts/data
configs=$base/configs
translations=$base/translations
logs=$base/logs/beam_search_bleu

mkdir -p $translations
mkdir -p $logs

src=it
trg=de

model_name=transformer_bpe_2000

# loop over beam sizes 1-10
for beam in {1..10}; do
    echo "###############################################################################"
    echo "model_name $model_name with beam_size=$beam"
    
    # Modify beam size in config temporarily
    cp $configs/$model_name.yaml $configs/$model_name.temp.yaml
    sed -i "s/beam_size: [0-9]\+/beam_size: $beam/" $configs/$model_name.temp.yaml

    # Translate
    translations_sub=$translations/$model_name
    mkdir -p $translations_sub

    OMP_NUM_THREADS=4 python -m joeynmt translate $configs/$model_name.temp.yaml < $data/test.it-de.$src > $translations_sub/test.beam${beam}.it-de.$trg

    bleu_output=$(cat $translations_sub/test.beam${beam}.it-de.$trg | sacrebleu $data/test.it-de.$trg)

    echo "#############################" | tee -a $logs/bleu_scores.txt
    echo "Beam size: $beam" | tee -a $logs/bleu_scores.txt
    echo "$bleu_output" | tee -a $logs/bleu_scores.txt
    echo "" | tee -a $logs/bleu_scores.txt


    # Clean up
    rm $configs/$model_name.temp.yaml
done
