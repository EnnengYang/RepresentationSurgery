
## ViT-L/14 Result

### Weight Average + Surgery
```
# set method_name = 'weight_averaging' 
# set model_name = 'ViT-L-14' 
python main_WeightAveraging_with_surgery.py
```

```
Eval: step: 500 dataset: SUN397 ACC: 0.7378186755166691
Eval: step: 500 dataset: Cars ACC: 0.839074741947519
Eval: step: 500 dataset: RESISC45 ACC: 0.9207936507936508
Eval: step: 500 dataset: EuroSAT ACC: 0.9840740740740741
Eval: step: 500 dataset: SVHN ACC: 0.8249462200368777
Eval: step: 500 dataset: GTSRB ACC: 0.8638954869358669
Eval: step: 500 dataset: MNIST ACC: 0.9879
Eval: step: 500 dataset: DTD ACC: 0.7191489361702128
Eval: step: 500 Avg ACC:0.8597064731843588
```

### Task Arithmetic + Surgery
```
# set method_name = 'task_arithmetic' 
# set model_name = 'ViT-L-14' 
python main_TaskArithmetic_with_surgery.py
```

```
Eval: step: 500 dataset: SUN397 ACC: 0.7575803288580479
Eval: step: 500 dataset: Cars ACC: 0.8447954234547942
Eval: step: 500 dataset: RESISC45 ACC: 0.9315873015873016
Eval: step: 500 dataset: EuroSAT ACC: 0.9888888888888889
Eval: step: 500 dataset: SVHN ACC: 0.9132221880762139
Eval: step: 500 dataset: GTSRB ACC: 0.9345209817893904
Eval: step: 500 dataset: MNIST ACC: 0.9919
Eval: step: 500 dataset: DTD ACC: 0.7611702127659574
Eval: step: 500 Avg ACC:0.8904581656775744
```

### Ties-Merging + Surgery
```
# set method_name = 'ties_merging' 
# set model_name = 'ViT-L-14' 
python main_TiesMerging_with_surgery.py
```

```
Eval: step: 500 dataset: SUN397 ACC: 0.7658269221099211
Eval: step: 500 dataset: Cars ACC: 0.8585996766571322
Eval: step: 500 dataset: RESISC45 ACC: 0.9376190476190476
Eval: step: 500 dataset: EuroSAT ACC: 0.9929629629629629
Eval: step: 500 dataset: SVHN ACC: 0.8974339274738783
Eval: step: 500 dataset: GTSRB ACC: 0.9200316706254948
Eval: step: 500 dataset: MNIST ACC: 0.9913
Eval: step: 500 dataset: DTD ACC: 0.7819148936170213
Eval: step: 500 Avg ACC:0.8932111376331822
```


### Layer-wise AdaMerging + Surgery
```
# set method_name = 'lw_adamerging' 
# set model_name = 'ViT-L-14' 
python main_AdaMerging_with_surgery.py
```

```
Eval: step: 500 dataset: SUN397 ACC: 0.8038417056368482
Eval: step: 500 dataset: Cars ACC: 0.9089665464494466
Eval: step: 500 dataset: RESISC45 ACC: 0.943968253968254
Eval: step: 500 dataset: EuroSAT ACC: 0.9829629629629629
Eval: step: 500 dataset: SVHN ACC: 0.941341425937308
Eval: step: 500 dataset: GTSRB ACC: 0.98701504354711
Eval: step: 500 dataset: MNIST ACC: 0.9921
Eval: step: 500 dataset: DTD ACC: 0.825
Eval: step: 500 Avg ACC:0.9231494923127412
```
