
## ViT-B/16 Result

### Weight Average + Surgery
```
# set method_name = 'weight_averaging' 
# set model_name = 'ViT-B-16' 
python main_WeightAveraging_with_surgery.py
```

```
Eval: step 0:  dataset: SUN397 ACC: 0.6779805903353949
Eval: step 0:  dataset: Cars ACC: 0.7002860340753637
Eval: step 0:  dataset: RESISC45 ACC: 0.753968253968254
Eval: step 0:  dataset: EuroSAT ACC: 0.7959259259259259
Eval: step 0:  dataset: SVHN ACC: 0.7490780577750461
Eval: step 0:  dataset: GTSRB ACC: 0.6010292953285827
Eval: step 0:  dataset: MNIST ACC: 0.9442
Eval: step 0:  dataset: DTD ACC: 0.43829787234042555
Eval: step 0: Avg ACC:0.707595753718624

Eval: step: 100 dataset: SUN397 ACC: 0.7025192336702368
Eval: step: 100 dataset: Cars ACC: 0.7001616714339013
Eval: step: 100 dataset: RESISC45 ACC: 0.8493650793650793
Eval: step: 100 dataset: EuroSAT ACC: 0.9574074074074074
Eval: step: 100 dataset: SVHN ACC: 0.7849569760295021
Eval: step: 100 dataset: GTSRB ACC: 0.7835312747426761
Eval: step: 100 dataset: MNIST ACC: 0.9687
Eval: step: 100 dataset: DTD ACC: 0.625531914893617
Eval: step: 100 Avg ACC:0.7965216946928024

Eval: step: 200 dataset: SUN397 ACC: 0.703122642932569
Eval: step: 200 dataset: Cars ACC: 0.6997885835095138
Eval: step: 200 dataset: RESISC45 ACC: 0.8644444444444445
Eval: step: 200 dataset: EuroSAT ACC: 0.9685185185185186
Eval: step: 200 dataset: SVHN ACC: 0.81399815611555
Eval: step: 200 dataset: GTSRB ACC: 0.808313539192399
Eval: step: 200 dataset: MNIST ACC: 0.9771
Eval: step: 200 dataset: DTD ACC: 0.6659574468085107
Eval: step: 200 Avg ACC:0.8126554164401882

Eval: step: 300 dataset: SUN397 ACC: 0.7057877005078694
Eval: step: 300 dataset: Cars ACC: 0.7285163536873523
Eval: step: 300 dataset: RESISC45 ACC: 0.8852380952380953
Eval: step: 300 dataset: EuroSAT ACC: 0.9707407407407408
Eval: step: 300 dataset: SVHN ACC: 0.8143822987092809
Eval: step: 300 dataset: GTSRB ACC: 0.8167062549485352
Eval: step: 300 dataset: MNIST ACC: 0.979
Eval: step: 300 dataset: DTD ACC: 0.6813829787234043
Eval: step: 300 Avg ACC:0.8227193028194097

Eval: step: 400 dataset: SUN397 ACC: 0.7057374164026751
Eval: step: 400 dataset: Cars ACC: 0.7222982216142271
Eval: step: 400 dataset: RESISC45 ACC: 0.8785714285714286
Eval: step: 400 dataset: EuroSAT ACC: 0.9718518518518519
Eval: step: 400 dataset: SVHN ACC: 0.8122311001843885
Eval: step: 400 dataset: GTSRB ACC: 0.8311163895486936
Eval: step: 400 dataset: MNIST ACC: 0.9801
Eval: step: 400 dataset: DTD ACC: 0.6813829787234043
Eval: step: 400 Avg ACC:0.8229111733620835

Eval: step: 500 dataset: SUN397 ACC: 0.7030723588273746
Eval: step: 500 dataset: Cars ACC: 0.7242880238776271
Eval: step: 500 dataset: RESISC45 ACC: 0.8884126984126984
Eval: step: 500 dataset: EuroSAT ACC: 0.9762962962962963
Eval: step: 500 dataset: SVHN ACC: 0.8206438229870928
Eval: step: 500 dataset: GTSRB ACC: 0.8319873317498021
Eval: step: 500 dataset: MNIST ACC: 0.9818
Eval: step: 500 dataset: DTD ACC: 0.6856382978723404
Eval: step: 500 Avg ACC:0.8265173537529039

```

### Task Arithmetic + Surgery
```
# set method_name = 'task_arithmetic' 
# set model_name = 'ViT-B-16' 
python main_TaskArithmetic_with_surgery.py
```

```
Eval: step: 100 dataset: SUN397 ACC: 0.678131442650978
Eval: step: 100 dataset: Cars ACC: 0.6878497699291133
Eval: step: 100 dataset: RESISC45 ACC: 0.8546031746031746
Eval: step: 100 dataset: EuroSAT ACC: 0.9562962962962963
Eval: step: 100 dataset: SVHN ACC: 0.8943223724646588
Eval: step: 100 dataset: GTSRB ACC: 0.8304038004750594
Eval: step: 100 dataset: MNIST ACC: 0.9869
Eval: step: 100 dataset: DTD ACC: 0.6797872340425531
Eval: step: 100 Avg ACC:0.8210367613077293

Eval: step: 200 dataset: SUN397 ACC: 0.6807965002262785
Eval: step: 200 dataset: Cars ACC: 0.7158313642581768
Eval: step: 200 dataset: RESISC45 ACC: 0.8711111111111111
Eval: step: 200 dataset: EuroSAT ACC: 0.9622222222222222
Eval: step: 200 dataset: SVHN ACC: 0.9038106945298094
Eval: step: 200 dataset: GTSRB ACC: 0.8608867775138559
Eval: step: 200 dataset: MNIST ACC: 0.9888
Eval: step: 200 dataset: DTD ACC: 0.7047872340425532
Eval: step: 200 Avg ACC:0.8360307379880009

Eval: step: 300 dataset: SUN397 ACC: 0.6810479207522502
Eval: step: 300 dataset: Cars ACC: 0.7249098370849397
Eval: step: 300 dataset: RESISC45 ACC: 0.8822222222222222
Eval: step: 300 dataset: EuroSAT ACC: 0.9703703703703703
Eval: step: 300 dataset: SVHN ACC: 0.9079978488014752
Eval: step: 300 dataset: GTSRB ACC: 0.8785431512272367
Eval: step: 300 dataset: MNIST ACC: 0.9896
Eval: step: 300 dataset: DTD ACC: 0.7175531914893617
Eval: step: 300 Avg ACC:0.844030567743482

Eval: step: 400 dataset: SUN397 ACC: 0.6833609895911902
Eval: step: 400 dataset: Cars ACC: 0.7125979355801517
Eval: step: 400 dataset: RESISC45 ACC: 0.8782539682539683
Eval: step: 400 dataset: EuroSAT ACC: 0.9762962962962963
Eval: step: 400 dataset: SVHN ACC: 0.9094960049170252
Eval: step: 400 dataset: GTSRB ACC: 0.894061757719715
Eval: step: 400 dataset: MNIST ACC: 0.9897
Eval: step: 400 dataset: DTD ACC: 0.726063829787234
Eval: step: 400 Avg ACC:0.8462288477681976

Eval: step: 500 dataset: SUN397 ACC: 0.6833107054859959
Eval: step: 500 dataset: Cars ACC: 0.7237905733117771
Eval: step: 500 dataset: RESISC45 ACC: 0.8876190476190476
Eval: step: 500 dataset: EuroSAT ACC: 0.9774074074074074
Eval: step: 500 dataset: SVHN ACC: 0.9102258758451137
Eval: step: 500 dataset: GTSRB ACC: 0.8956452889944576
Eval: step: 500 dataset: MNIST ACC: 0.9897
Eval: step: 500 dataset: DTD ACC: 0.7297872340425532
Eval: step: 500 Avg ACC:0.8496857665882941
```

### Ties-Merging + Surgery
```
# set method_name = 'ties_merging' 
# set model_name = 'ViT-B-16' 
python main_TiesMerging_with_surgery.py
```

```
Eval: step: 100 dataset: SUN397 ACC: 0.7266556041635239
Eval: step: 100 dataset: Cars ACC: 0.7370973759482652
Eval: step: 100 dataset: RESISC45 ACC: 0.8971428571428571
Eval: step: 100 dataset: EuroSAT ACC: 0.9662962962962963
Eval: step: 100 dataset: SVHN ACC: 0.8743469575906576
Eval: step: 100 dataset: GTSRB ACC: 0.8211401425178148
Eval: step: 100 dataset: MNIST ACC: 0.9852
Eval: step: 100 dataset: DTD ACC: 0.7324468085106383
Eval: step: 100 Avg ACC:0.8425407552712567

Eval: step: 200 dataset: SUN397 ACC: 0.7303766279479057
Eval: step: 200 dataset: Cars ACC: 0.7490361895286656
Eval: step: 200 dataset: RESISC45 ACC: 0.8995238095238095
Eval: step: 200 dataset: EuroSAT ACC: 0.9751851851851852
Eval: step: 200 dataset: SVHN ACC: 0.8824907805777504
Eval: step: 200 dataset: GTSRB ACC: 0.8405384006334126
Eval: step: 200 dataset: MNIST ACC: 0.9863
Eval: step: 200 dataset: DTD ACC: 0.7420212765957447
Eval: step: 200 Avg ACC:0.8506840337490592

Eval: step: 300 dataset: SUN397 ACC: 0.7307286166842661
Eval: step: 300 dataset: Cars ACC: 0.7542594204700908
Eval: step: 300 dataset: RESISC45 ACC: 0.9044444444444445
Eval: step: 300 dataset: EuroSAT ACC: 0.9762962962962963
Eval: step: 300 dataset: SVHN ACC: 0.891018746158574
Eval: step: 300 dataset: GTSRB ACC: 0.8615993665874901
Eval: step: 300 dataset: MNIST ACC: 0.9868
Eval: step: 300 dataset: DTD ACC: 0.7489361702127659
Eval: step: 300 Avg ACC:0.856760382606741

Eval: step: 400 dataset: SUN397 ACC: 0.7307789007894605
Eval: step: 400 dataset: Cars ACC: 0.761223728391991
Eval: step: 400 dataset: RESISC45 ACC: 0.9082539682539682
Eval: step: 400 dataset: EuroSAT ACC: 0.9822222222222222
Eval: step: 400 dataset: SVHN ACC: 0.8929010448678549
Eval: step: 400 dataset: GTSRB ACC: 0.8623119556611243
Eval: step: 400 dataset: MNIST ACC: 0.9876
Eval: step: 400 dataset: DTD ACC: 0.7441489361702127
Eval: step: 400 Avg ACC:0.8586800945446043

Eval: step: 500 dataset: SUN397 ACC: 0.7304269120531001
Eval: step: 500 dataset: Cars ACC: 0.7622186295236911
Eval: step: 500 dataset: RESISC45 ACC: 0.9077777777777778
Eval: step: 500 dataset: EuroSAT ACC: 0.9814814814814815
Eval: step: 500 dataset: SVHN ACC: 0.8970113706207744
Eval: step: 500 dataset: GTSRB ACC: 0.8676167854315123
Eval: step: 500 dataset: MNIST ACC: 0.9878
Eval: step: 500 dataset: DTD ACC: 0.752127659574468
Eval: step: 500 Avg ACC:0.8608075770578506

```



### Layer-wise AdaMerging + Surgery
```
# set method_name = 'lw_adamerging' 
# set model_name = 'ViT-B-16' 
python main_AdaMerging_with_surgery.py
```

```
Eval: step: 100 dataset: SUN397 ACC: 0.7333936742595666
Eval: step: 100 dataset: Cars ACC: 0.8117149608257679
Eval: step: 100 dataset: RESISC45 ACC: 0.8901587301587301
Eval: step: 100 dataset: EuroSAT ACC: 0.975925925925926
Eval: step: 100 dataset: SVHN ACC: 0.9231330669944684
Eval: step: 100 dataset: GTSRB ACC: 0.9720506730007917
Eval: step: 100 dataset: MNIST ACC: 0.9882
Eval: step: 100 dataset: DTD ACC: 0.7627659574468085
Eval: step: 100 Avg ACC:0.8821678735765074

Eval: step: 200 dataset: SUN397 ACC: 0.7353547543621461
Eval: step: 200 dataset: Cars ACC: 0.8133316751647806
Eval: step: 200 dataset: RESISC45 ACC: 0.8946031746031746
Eval: step: 200 dataset: EuroSAT ACC: 0.9822222222222222
Eval: step: 200 dataset: SVHN ACC: 0.9252458512599877
Eval: step: 200 dataset: GTSRB ACC: 0.9729216152019002
Eval: step: 200 dataset: MNIST ACC: 0.9886
Eval: step: 200 dataset: DTD ACC: 0.7627659574468085
Eval: step: 200 Avg ACC:0.8843806562826275

Eval: step: 300 dataset: SUN397 ACC: 0.7379695278322522
Eval: step: 300 dataset: Cars ACC: 0.814699664220868
Eval: step: 300 dataset: RESISC45 ACC: 0.9017460317460317
Eval: step: 300 dataset: EuroSAT ACC: 0.9837037037037037
Eval: step: 300 dataset: SVHN ACC: 0.9283574062692072
Eval: step: 300 dataset: GTSRB ACC: 0.973396674584323
Eval: step: 300 dataset: MNIST ACC: 0.9888
Eval: step: 300 dataset: DTD ACC: 0.7718085106382979
Eval: step: 300 Avg ACC:0.8875601898743355

Eval: step: 400 dataset: SUN397 ACC: 0.7353044702569518
Eval: step: 400 dataset: Cars ACC: 0.8156945653525681
Eval: step: 400 dataset: RESISC45 ACC: 0.9049206349206349
Eval: step: 400 dataset: EuroSAT ACC: 0.9833333333333333
Eval: step: 400 dataset: SVHN ACC: 0.9314689612784266
Eval: step: 400 dataset: GTSRB ACC: 0.9748218527315915
Eval: step: 400 dataset: MNIST ACC: 0.9888
Eval: step: 400 dataset: DTD ACC: 0.775
Eval: step: 400 Avg ACC:0.8886679772341883

Eval: step: 500 dataset: SUN397 ACC: 0.7365112887816161
Eval: step: 500 dataset: Cars ACC: 0.8159432906354931
Eval: step: 500 dataset: RESISC45 ACC: 0.9042857142857142
Eval: step: 500 dataset: EuroSAT ACC: 0.9855555555555555
Eval: step: 500 dataset: SVHN ACC: 0.9326982175783651
Eval: step: 500 dataset: GTSRB ACC: 0.9749010292953286
Eval: step: 500 dataset: MNIST ACC: 0.989
Eval: step: 500 dataset: DTD ACC: 0.7702127659574468
Eval: step: 500 Avg ACC:0.88863848276119
```



