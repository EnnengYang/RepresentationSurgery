
## ViT-B/32 Result

### Weight Average + Surgery
```
# set method_name = 'weight_averaging'
# set model_name = 'ViT-B-32'
python main_WeightAveraging_with_surgery.py
```

```
Eval: step: 100 dataset: SUN397 ACC: 0.6733041685523206
Eval: step: 100 dataset: Cars ACC: 0.6333789329685362
Eval: step: 100 dataset: RESISC45 ACC: 0.8192063492063492
Eval: step: 100 dataset: EuroSAT ACC: 0.9492592592592592
Eval: step: 100 dataset: SVHN ACC: 0.6746696373693916
Eval: step: 100 dataset: GTSRB ACC: 0.7765637371338084
Eval: step: 100 dataset: MNIST ACC: 0.9606
Eval: step: 100 dataset: DTD ACC: 0.601063829787234
Eval: step: 100 Avg ACC:0.7610057392846125

Eval: step: 200 dataset: SUN397 ACC: 0.6754663850756776
Eval: step: 200 dataset: Cars ACC: 0.638477801268499
Eval: step: 200 dataset: RESISC45 ACC: 0.8369841269841269
Eval: step: 200 dataset: EuroSAT ACC: 0.9574074074074074
Eval: step: 200 dataset: SVHN ACC: 0.7235325752919484
Eval: step: 200 dataset: GTSRB ACC: 0.8049881235154395
Eval: step: 200 dataset: MNIST ACC: 0.9669
Eval: step: 200 dataset: DTD ACC: 0.6367021276595745
Eval: step: 200 Avg ACC:0.7800573184003341

Eval: step: 300 dataset: SUN397 ACC: 0.6742595665510133
Eval: step: 300 dataset: Cars ACC: 0.6496704390001243
Eval: step: 300 dataset: RESISC45 ACC: 0.8503174603174604
Eval: step: 300 dataset: EuroSAT ACC: 0.9629629629629629
Eval: step: 300 dataset: SVHN ACC: 0.7482329440688383
Eval: step: 300 dataset: GTSRB ACC: 0.8057007125890736
Eval: step: 300 dataset: MNIST ACC: 0.9715
Eval: step: 300 dataset: DTD ACC: 0.65
Eval: step: 300 Avg ACC:0.7890805106861841

Eval: step: 400 dataset: SUN397 ACC: 0.6752149645497059
Eval: step: 400 dataset: Cars ACC: 0.6344981967416988
Eval: step: 400 dataset: RESISC45 ACC: 0.8568253968253968
Eval: step: 400 dataset: EuroSAT ACC: 0.9677777777777777
Eval: step: 400 dataset: SVHN ACC: 0.7546097111247695
Eval: step: 400 dataset: GTSRB ACC: 0.8190023752969121
Eval: step: 400 dataset: MNIST ACC: 0.975
Eval: step: 400 dataset: DTD ACC: 0.6718085106382978
Eval: step: 400 Avg ACC:0.7943421166193199

Eval: step: 500 dataset: SUN397 ACC: 0.6763212148639814
Eval: step: 500 dataset: Cars ACC: 0.6464370103220992
Eval: step: 500 dataset: RESISC45 ACC: 0.8584126984126984
Eval: step: 500 dataset: EuroSAT ACC: 0.9681481481481482
Eval: step: 500 dataset: SVHN ACC: 0.7693223724646588
Eval: step: 500 dataset: GTSRB ACC: 0.8297703879651623
Eval: step: 500 dataset: MNIST ACC: 0.9783
Eval: step: 500 dataset: DTD ACC: 0.673936170212766
Eval: step: 500 Avg ACC:0.8000810002986893

```

### Task Arithmetic + Surgery
```
# set method_name = 'task_arithmetic'
# set model_name = 'ViT-B-32'
python main_TaskArithmetic_with_surgery.py
```

```
Eval: step: 100 dataset: SUN397 ACC: 0.6346356916578669
Eval: step: 100 dataset: Cars ACC: 0.5728143265762965
Eval: step: 100 dataset: RESISC45 ACC: 0.79
Eval: step: 100 dataset: EuroSAT ACC: 0.947037037037037
Eval: step: 100 dataset: SVHN ACC: 0.8448063921327597
Eval: step: 100 dataset: GTSRB ACC: 0.8258115597783057
Eval: step: 100 dataset: MNIST ACC: 0.9827
Eval: step: 100 dataset: DTD ACC: 0.65
Eval: step: 100 Avg ACC:0.7809756258977834

Eval: step: 200 dataset: SUN397 ACC: 0.6401669432292453
Eval: step: 200 dataset: Cars ACC: 0.5843800522323094
Eval: step: 200 dataset: RESISC45 ACC: 0.8195238095238095
Eval: step: 200 dataset: EuroSAT ACC: 0.967037037037037
Eval: step: 200 dataset: SVHN ACC: 0.8589428395820529
Eval: step: 200 dataset: GTSRB ACC: 0.8507521773555028
Eval: step: 200 dataset: MNIST ACC: 0.9851
Eval: step: 200 dataset: DTD ACC: 0.6851063829787234
Eval: step: 200 Avg ACC:0.798876155242335

Eval: step: 300 dataset: SUN397 ACC: 0.63941268165133
Eval: step: 300 dataset: Cars ACC: 0.5985573933590349
Eval: step: 300 dataset: RESISC45 ACC: 0.8312698412698413
Eval: step: 300 dataset: EuroSAT ACC: 0.97
Eval: step: 300 dataset: SVHN ACC: 0.8598647818070068
Eval: step: 300 dataset: GTSRB ACC: 0.8622327790973872
Eval: step: 300 dataset: MNIST ACC: 0.9869
Eval: step: 300 dataset: DTD ACC: 0.6872340425531915
Eval: step: 300 Avg ACC:0.8044339399672239

Eval: step: 400 dataset: SUN397 ACC: 0.6392618293357469
Eval: step: 400 dataset: Cars ACC: 0.588484019400572
Eval: step: 400 dataset: RESISC45 ACC: 0.8322222222222222
Eval: step: 400 dataset: EuroSAT ACC: 0.9744444444444444
Eval: step: 400 dataset: SVHN ACC: 0.8694683466502766
Eval: step: 400 dataset: GTSRB ACC: 0.8687252573238321
Eval: step: 400 dataset: MNIST ACC: 0.9879
Eval: step: 400 dataset: DTD ACC: 0.6872340425531915
Eval: step: 400 Avg ACC:0.8059675202412857

Eval: step: 500 dataset: SUN397 ACC: 0.6383064313370543
Eval: step: 500 dataset: Cars ACC: 0.59980101977366
Eval: step: 500 dataset: RESISC45 ACC: 0.8331746031746031
Eval: step: 500 dataset: EuroSAT ACC: 0.9792592592592593
Eval: step: 500 dataset: SVHN ACC: 0.8702366318377381
Eval: step: 500 dataset: GTSRB ACC: 0.8708630245447347
Eval: step: 500 dataset: MNIST ACC: 0.9867
Eval: step: 500 dataset: DTD ACC: 0.6946808510638298
Eval: step: 500 Avg ACC:0.80912772762386
```

### Ties-Merging + Surgery
```
# set method_name = 'ties_merging'
# set model_name = 'ViT-B-32'
python main_TiesMerging_with_surgery.py
```

```
Eval: step: 100 dataset: SUN397 ACC: 0.6933172424196712
Eval: step: 100 dataset: Cars ACC: 0.6497948016415869
Eval: step: 100 dataset: RESISC45 ACC: 0.85
Eval: step: 100 dataset: EuroSAT ACC: 0.955925925925926
Eval: step: 100 dataset: SVHN ACC: 0.854179471419791
Eval: step: 100 dataset: GTSRB ACC: 0.8494061757719715
Eval: step: 100 dataset: MNIST ACC: 0.979
Eval: step: 100 dataset: DTD ACC: 0.6797872340425531
Eval: step: 100 Avg ACC:0.8139263564026874

Eval: step: 200 dataset: SUN397 ACC: 0.6954291748378337
Eval: step: 200 dataset: Cars ACC: 0.6526551423952245
Eval: step: 200 dataset: RESISC45 ACC: 0.8650793650793651
Eval: step: 200 dataset: EuroSAT ACC: 0.9677777777777777
Eval: step: 200 dataset: SVHN ACC: 0.8582513829133375
Eval: step: 200 dataset: GTSRB ACC: 0.8546318289786223
Eval: step: 200 dataset: MNIST ACC: 0.9816
Eval: step: 200 dataset: DTD ACC: 0.7015957446808511
Eval: step: 200 Avg ACC:0.8221275520828765

Eval: step: 300 dataset: SUN397 ACC: 0.6949766178910847
Eval: step: 300 dataset: Cars ACC: 0.6499191642830494
Eval: step: 300 dataset: RESISC45 ACC: 0.8690476190476191
Eval: step: 300 dataset: EuroSAT ACC: 0.9744444444444444
Eval: step: 300 dataset: SVHN ACC: 0.863821450522434
Eval: step: 300 dataset: GTSRB ACC: 0.8600158353127474
Eval: step: 300 dataset: MNIST ACC: 0.9835
Eval: step: 300 dataset: DTD ACC: 0.7175531914893617
Eval: step: 300 Avg ACC:0.8266597903738426

Eval: step: 400 dataset: SUN397 ACC: 0.698345652939106
Eval: step: 400 dataset: Cars ACC: 0.6612361646561373
Eval: step: 400 dataset: RESISC45 ACC: 0.871904761904762
Eval: step: 400 dataset: EuroSAT ACC: 0.9740740740740741
Eval: step: 400 dataset: SVHN ACC: 0.857521511985249
Eval: step: 400 dataset: GTSRB ACC: 0.8750593824228029
Eval: step: 400 dataset: MNIST ACC: 0.9851
Eval: step: 400 dataset: DTD ACC: 0.7212765957446808
Eval: step: 400 Avg ACC:0.8305647679658515

Eval: step: 500 dataset: SUN397 ACC: 0.6981948006235229
Eval: step: 500 dataset: Cars ACC: 0.6617336152219874
Eval: step: 500 dataset: RESISC45 ACC: 0.8738095238095238
Eval: step: 500 dataset: EuroSAT ACC: 0.9751851851851852
Eval: step: 500 dataset: SVHN ACC: 0.867701290719115
Eval: step: 500 dataset: GTSRB ACC: 0.876326207442597
Eval: step: 500 dataset: MNIST ACC: 0.9851
Eval: step: 500 dataset: DTD ACC: 0.7164893617021276
Eval: step: 500 Avg ACC:0.8318174980880074
```




### Layer-wise AdaMerging + Surgery
```
# set method_name = 'lw_adamerging'
# set model_name = 'ViT-B-32'
python main_AdaMerging_with_surgery.py
```


```
Eval: step: 100 dataset: SUN397 ACC: 0.6940715039975863
Eval: step: 100 dataset: Cars ACC: 0.6943166272851635
Eval: step: 100 dataset: RESISC45 ACC: 0.8677777777777778
Eval: step: 100 dataset: EuroSAT ACC: 0.9718518518518519
Eval: step: 100 dataset: SVHN ACC: 0.9025430239704979
Eval: step: 100 dataset: GTSRB ACC: 0.9586698337292161
Eval: step: 100 dataset: MNIST ACC: 0.9831
Eval: step: 100 dataset: DTD ACC: 0.7090425531914893
Eval: step: 100 Avg ACC:0.8476716464754478

Eval: step: 200 dataset: SUN397 ACC: 0.6977925277819681
Eval: step: 200 dataset: Cars ACC: 0.6965551548314887
Eval: step: 200 dataset: RESISC45 ACC: 0.8806349206349207
Eval: step: 200 dataset: EuroSAT ACC: 0.9744444444444444
Eval: step: 200 dataset: SVHN ACC: 0.9080746773202213
Eval: step: 200 dataset: GTSRB ACC: 0.9629453681710214
Eval: step: 200 dataset: MNIST ACC: 0.9844
Eval: step: 200 dataset: DTD ACC: 0.7223404255319149
Eval: step: 200 Avg ACC:0.8533984398394974

Eval: step: 300 dataset: SUN397 ACC: 0.6978930959923568
Eval: step: 300 dataset: Cars ACC: 0.6761596816316379
Eval: step: 300 dataset: RESISC45 ACC: 0.8807936507936508
Eval: step: 300 dataset: EuroSAT ACC: 0.9781481481481481
Eval: step: 300 dataset: SVHN ACC: 0.9129532882606023
Eval: step: 300 dataset: GTSRB ACC: 0.9619952494061758
Eval: step: 300 dataset: MNIST ACC: 0.9865
Eval: step: 300 dataset: DTD ACC: 0.7281914893617021
Eval: step: 300 Avg ACC:0.8528293254492842

Eval: step: 400 dataset: SUN397 ACC: 0.6997033237793533
Eval: step: 400 dataset: Cars ACC: 0.6985449570948887
Eval: step: 400 dataset: RESISC45 ACC: 0.8877777777777778
Eval: step: 400 dataset: EuroSAT ACC: 0.9785185185185186
Eval: step: 400 dataset: SVHN ACC: 0.916641057160418
Eval: step: 400 dataset: GTSRB ACC: 0.964528899445764
Eval: step: 400 dataset: MNIST ACC: 0.9869
Eval: step: 400 dataset: DTD ACC: 0.7441489361702127
Eval: step: 400 Avg ACC:0.8595954337433667

Eval: step: 500 dataset: SUN397 ACC: 0.6985467893598833
Eval: step: 500 dataset: Cars ACC: 0.7103594080338267
Eval: step: 500 dataset: RESISC45 ACC: 0.8893650793650794
Eval: step: 500 dataset: EuroSAT ACC: 0.9818518518518519
Eval: step: 500 dataset: SVHN ACC: 0.9175629993853719
Eval: step: 500 dataset: GTSRB ACC: 0.9652414885193983
Eval: step: 500 dataset: MNIST ACC: 0.9884
Eval: step: 500 dataset: DTD ACC: 0.7367021276595744
Eval: step: 500 Avg ACC:0.8610037180218733
```
