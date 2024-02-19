
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


## Layer-wise AdaMerging + Surgery (Online Setting)
```
SUN397 Eval step:
[198, 1988, 3977, 5966, 7954, 9943, 11932, 13920, 15909, 17898, 19887]
Eval: ratio: 0.009956252828480916 step:198 dataset: SUN397 ACC: 0.6776788857042289
Eval: ratio: 0.09996480112636395 step:1988 dataset: SUN397 ACC: 0.6925629808417559
Eval: ratio: 0.19997988635792227 step:3977 dataset: SUN397 ACC: 0.6958314476793885
Eval: ratio: 0.2999949715894806 step:5966 dataset: SUN397 ACC: 0.6986473575702721
Eval: ratio: 0.39995977271584454 step:7954 dataset: SUN397 ACC: 0.6967868456780811
Eval: ratio: 0.4999748579474028 step:9943 dataset: SUN397 ACC: 0.6959320158897773
Eval: ratio: 0.5999899431789611 step:11932 dataset: SUN397 ACC: 0.6960325841001659
Eval: ratio: 0.6999547443053251 step:13920 dataset: SUN397 ACC: 0.6956805953638056
Eval: ratio: 0.7999698295368833 step:15909 dataset: SUN397 ACC: 0.6970382662040528
Eval: ratio: 0.8999849147684417 step:17898 dataset: SUN397 ACC: 0.6958314476793885
Eval: ratio: 1.0 step:19887 dataset: SUN397 ACC: 0.6947251973651128
Cars Eval step:
[80, 804, 1608, 2412, 3216, 4020, 4824, 5628, 6432, 7236, 8041]
Eval: ratio: 0.009949011317000373 step:80 dataset: Cars ACC: 0.680388011441363
Eval: ratio: 0.09998756373585375 step:804 dataset: Cars ACC: 0.6878497699291133
Eval: ratio: 0.1999751274717075 step:1608 dataset: Cars ACC: 0.691705011814451
Eval: ratio: 0.29996269120756125 step:2412 dataset: Cars ACC: 0.692699912946151
Eval: ratio: 0.399950254943415 step:3216 dataset: Cars ACC: 0.6872279567218008
Eval: ratio: 0.49993781867926873 step:4020 dataset: Cars ACC: 0.6990424076607387
Eval: ratio: 0.5999253824151225 step:4824 dataset: Cars ACC: 0.6869792314388757
Eval: ratio: 0.6999129461509762 step:5628 dataset: Cars ACC: 0.6956846163412511
Eval: ratio: 0.79990050988683 step:6432 dataset: Cars ACC: 0.6964307921900261
Eval: ratio: 0.8998880736226837 step:7236 dataset: Cars ACC: 0.6977987812461137
Eval: ratio: 1.0 step:8041 dataset: Cars ACC: 0.6907101106827509
RESISC45 Eval step:
[63, 630, 1260, 1890, 2520, 3150, 3780, 4410, 5040, 5670, 6300]
Eval: ratio: 0.01 step:63 dataset: RESISC45 ACC: 0.8184126984126984
Eval: ratio: 0.1 step:630 dataset: RESISC45 ACC: 0.8522222222222222
Eval: ratio: 0.2 step:1260 dataset: RESISC45 ACC: 0.8676190476190476
Eval: ratio: 0.3 step:1890 dataset: RESISC45 ACC: 0.8706349206349207
Eval: ratio: 0.4 step:2520 dataset: RESISC45 ACC: 0.8757142857142857
Eval: ratio: 0.5 step:3150 dataset: RESISC45 ACC: 0.8790476190476191
Eval: ratio: 0.6 step:3780 dataset: RESISC45 ACC: 0.8795238095238095
Eval: ratio: 0.7 step:4410 dataset: RESISC45 ACC: 0.8795238095238095
Eval: ratio: 0.8 step:5040 dataset: RESISC45 ACC: 0.8841269841269841
Eval: ratio: 0.9 step:5670 dataset: RESISC45 ACC: 0.8817460317460317
Eval: ratio: 1.0 step:6300 dataset: RESISC45 ACC: 0.8825396825396825
EuroSAT Eval step:
[27, 270, 540, 810, 1080, 1350, 1620, 1889, 2160, 2430, 2700]
Eval: ratio: 0.01 step:27 dataset: EuroSAT ACC: 0.912962962962963
Eval: ratio: 0.1 step:270 dataset: EuroSAT ACC: 0.9533333333333334
Eval: ratio: 0.2 step:540 dataset: EuroSAT ACC: 0.9592592592592593
Eval: ratio: 0.3 step:810 dataset: EuroSAT ACC: 0.9637037037037037
Eval: ratio: 0.4 step:1080 dataset: EuroSAT ACC: 0.9711111111111111
Eval: ratio: 0.5 step:1350 dataset: EuroSAT ACC: 0.9703703703703703
Eval: ratio: 0.6 step:1620 dataset: EuroSAT ACC: 0.9740740740740741
Eval: ratio: 0.6996296296296296 step:1889 dataset: EuroSAT ACC: 0.9718518518518519
Eval: ratio: 0.8 step:2160 dataset: EuroSAT ACC: 0.9744444444444444
Eval: ratio: 0.9 step:2430 dataset: EuroSAT ACC: 0.9762962962962963
Eval: ratio: 1.0 step:2700 dataset: EuroSAT ACC: 0.9762962962962963
SVHN Eval step:
[260, 2603, 5206, 7809, 10412, 13016, 15619, 18222, 20825, 23428, 26032]
Eval: ratio: 0.009987707437000615 step:260 dataset: SVHN ACC: 0.8845267363245236
Eval: ratio: 0.09999231714812538 step:2603 dataset: SVHN ACC: 0.9005838967424709
Eval: ratio: 0.19998463429625077 step:5206 dataset: SVHN ACC: 0.9111094038106945
Eval: ratio: 0.29997695144437614 step:7809 dataset: SVHN ACC: 0.9110325752919484
Eval: ratio: 0.39996926859250154 step:10412 dataset: SVHN ACC: 0.9141441303011678
Eval: ratio: 0.5 step:13016 dataset: SVHN ACC: 0.9138752304855562
Eval: ratio: 0.5999923171481254 step:15619 dataset: SVHN ACC: 0.9163337430854334
Eval: ratio: 0.6999846342962508 step:18222 dataset: SVHN ACC: 0.9168715427166564
Eval: ratio: 0.7999769514443762 step:20825 dataset: SVHN ACC: 0.9140673017824217
Eval: ratio: 0.8999692685925015 step:23428 dataset: SVHN ACC: 0.9200983405039951
Eval: ratio: 1.0 step:26032 dataset: SVHN ACC: 0.9206361401352182
GTSRB Eval step:
[126, 1263, 2526, 3789, 5052, 6315, 7578, 8841, 10104, 11367, 12630]
Eval: ratio: 0.009976247030878859 step:126 dataset: GTSRB ACC: 0.9458432304038005
Eval: ratio: 0.1 step:1263 dataset: GTSRB ACC: 0.9582739509105305
Eval: ratio: 0.2 step:2526 dataset: GTSRB ACC: 0.9577988915281077
Eval: ratio: 0.3 step:3789 dataset: GTSRB ACC: 0.957957244655582
Eval: ratio: 0.4 step:5052 dataset: GTSRB ACC: 0.9615993665874901
Eval: ratio: 0.5 step:6315 dataset: GTSRB ACC: 0.9619160728424386
Eval: ratio: 0.6 step:7578 dataset: GTSRB ACC: 0.9614410134600159
Eval: ratio: 0.7 step:8841 dataset: GTSRB ACC: 0.9627870150435471
Eval: ratio: 0.8 step:10104 dataset: GTSRB ACC: 0.965083135391924
Eval: ratio: 0.9 step:11367 dataset: GTSRB ACC: 0.9642913697545527
Eval: ratio: 1.0 step:12630 dataset: GTSRB ACC: 0.9631828978622328
MNIST Eval step:
[100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
Eval: ratio: 0.01 step:100 dataset: MNIST ACC: 0.9774
Eval: ratio: 0.1 step:1000 dataset: MNIST ACC: 0.982
Eval: ratio: 0.2 step:2000 dataset: MNIST ACC: 0.9827
Eval: ratio: 0.3 step:3000 dataset: MNIST ACC: 0.9842
Eval: ratio: 0.4 step:4000 dataset: MNIST ACC: 0.9852
Eval: ratio: 0.5 step:5000 dataset: MNIST ACC: 0.985
Eval: ratio: 0.6 step:6000 dataset: MNIST ACC: 0.9858
Eval: ratio: 0.7 step:7000 dataset: MNIST ACC: 0.9862
Eval: ratio: 0.8 step:8000 dataset: MNIST ACC: 0.9852
Eval: ratio: 0.9 step:9000 dataset: MNIST ACC: 0.9858
Eval: ratio: 1.0 step:10000 dataset: MNIST ACC: 0.9871
DTD Eval step:
[18, 188, 376, 564, 752, 940, 1128, 1316, 1504, 1692, 1880]
Eval: ratio: 0.009574468085106383 step:18 dataset: DTD ACC: 0.6053191489361702
Eval: ratio: 0.1 step:188 dataset: DTD ACC: 0.6420212765957447
Eval: ratio: 0.2 step:376 dataset: DTD ACC: 0.675531914893617
Eval: ratio: 0.3 step:564 dataset: DTD ACC: 0.675531914893617
Eval: ratio: 0.4 step:752 dataset: DTD ACC: 0.6792553191489362
Eval: ratio: 0.5 step:940 dataset: DTD ACC: 0.6872340425531915
Eval: ratio: 0.6 step:1128 dataset: DTD ACC: 0.6968085106382979
Eval: ratio: 0.7 step:1316 dataset: DTD ACC: 0.7101063829787234
Eval: ratio: 0.8 step:1504 dataset: DTD ACC: 0.7101063829787234
Eval: ratio: 0.9 step:1692 dataset: DTD ACC: 0.7069148936170213
Eval: ratio: 1.0 step:1880 dataset: DTD ACC: 0.7074468085106383

```
