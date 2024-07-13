Uses perturbation theory to generate the coefficients of the polynomial that will compute the sum of the first n terms of k-powers. 

For example, perturb(2) will produce the polynomial coefficients that compute the sum of the first n terms of all powers of 2. perturb(2).compute(5) will produce the sum of the first 5 terms (55).

This code uses a custom polynomial class. Accuracy is maintained until perturb(6), after which the values are inaccurate due to the use of floating point integers. Future version will include a Fraction class to maintain accuracy.

RESULTS for k=0,1,2,...,19,20

POWER: 0
POLYNOMIAL: 1 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 10
SUM of term 20: 20
SUM of term 30: 30
SUM of term 40: 40
SUM of term 50: 50
SUM of term 60: 60
SUM of term 70: 70
SUM of term 80: 80
SUM of term 90: 90
SUM of term 100: 100
-------------------------------------------------------

POWER: 1
POLYNOMIAL: ( 1 / 2 ) * x^2 + ( 1 / 2 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 55
SUM of term 20: 210
SUM of term 30: 465
SUM of term 40: 820
SUM of term 50: 1275
SUM of term 60: 1830
SUM of term 70: 2485
SUM of term 80: 3240
SUM of term 90: 4095
SUM of term 100: 5050
-------------------------------------------------------

POWER: 2
POLYNOMIAL: ( 1 / 3 ) * x^3 + ( 1 / 2 ) * x^2 + ( 1 / 6 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 385
SUM of term 20: 2870
SUM of term 30: 9455
SUM of term 40: 22140
SUM of term 50: 42925
SUM of term 60: 73810
SUM of term 70: 116795
SUM of term 80: 173880
SUM of term 90: 247065
SUM of term 100: 338350
-------------------------------------------------------

POWER: 3
POLYNOMIAL: ( 1 / 4 ) * x^4 + ( 1 / 2 ) * x^3 + ( 1 / 4 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 3025
SUM of term 20: 44100
SUM of term 30: 216225
SUM of term 40: 672400
SUM of term 50: 1625625
SUM of term 60: 3348900
SUM of term 70: 6175225
SUM of term 80: 10497600
SUM of term 90: 16769025
SUM of term 100: 25502500
-------------------------------------------------------

POWER: 4
POLYNOMIAL: ( 1 / 5 ) * x^5 + ( 1 / 2 ) * x^4 + ( 1 / 3 ) * x^3 + 0 * x^2 + ( -1 / 30 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 25333
SUM of term 20: 722666
SUM of term 30: 5273999
SUM of term 40: 21781332
SUM of term 50: 65666665
SUM of term 60: 162071998
SUM of term 70: 348259331
SUM of term 80: 676010664
SUM of term 90: 1214027997
SUM of term 100: 2050333330
-------------------------------------------------------

POWER: 5
POLYNOMIAL: ( 1 / 6 ) * x^6 + ( 1 / 2 ) * x^5 + ( 5 / 12 ) * x^4 + 0 * x^3 + ( -1 / 12 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 220825
SUM of term 20: 12333300
SUM of term 30: 133987425
SUM of term 40: 734933200
SUM of term 50: 2763020625
SUM of term 60: 8170199700
SUM of term 70: 20458520425
SUM of term 80: 45346132800
SUM of term 90: 91553286825
SUM of term 100: 171708332500
-------------------------------------------------------

POWER: 6
POLYNOMIAL: ( 1 / 7 ) * x^7 + ( 1 / 2 ) * x^6 + ( 1 / 2 ) * x^5 + 0 * x^4 + ( -1 / 6 ) * x^3 + 0 * x^2 + ( 1 / 42 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 1978405
SUM of term 20: 216455810
SUM of term 30: 3500931215
SUM of term 40: 25504903620
SUM of term 50: 119575872025
SUM of term 60: 423625335430
SUM of term 70: 1236154792835
SUM of term 80: 3128641743240
SUM of term 90: 7101485685645
SUM of term 100: 14790714119050
-------------------------------------------------------

POWER: 7
POLYNOMIAL: ( 1 / 8 ) * x^8 + ( 1 / 2 ) * x^7 + ( 7 / 12 ) * x^6 + 0 * x^5 + ( -7 / 24 ) * x^4 + 0 * x^3 + ( 1 / 12 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 18080425
SUM of term 20: 3877286700
SUM of term 30: 93372513825
SUM of term 40: 903508586800
SUM of term 50: 5282550260625
SUM of term 60: 22422092220300
SUM of term 70: 76246349080825
SUM of term 80: 220353865387200
SUM of term 90: 562308845614425
SUM of term 100: 1300583304167500
-------------------------------------------------------

POWER: 8
POLYNOMIAL: ( 1 / 9 ) * x^9 + ( 1 / 2 ) * x^8 + ( 2 / 3 ) * x^7 + 0 * x^6 + ( -7 / 15 ) * x^5 + 0 * x^4 + ( 2 / 9 ) * x^3 + 0 * x^2 + ( -1 / 30 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 167731333
SUM of term 20: 70540730666
SUM of term 30: 2529618665999
SUM of term 40: 32513090005332
SUM of term 50: 237065826416665
SUM of term 60: 1205590677167998
SUM of term 70: 4777463663527331
SUM of term 80: 15765921173162664
SUM of term 90: 45230940754541997
SUM of term 100: 116177773111333330
-------------------------------------------------------

POWER: 9
POLYNOMIAL: ( 1 / 10 ) * x^10 + ( 1 / 2 ) * x^9 + ( 3 / 4 ) * x^8 + 0 * x^7 + ( -7 / 10 ) * x^6 + 0 * x^5 + ( 1 / 2 ) * x^4 + 0 * x^3 + ( -3 / 20 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 1574304985
SUM of term 20: 1299155279940
SUM of term 30: 69382065104865
SUM of term 40: 1184560334079760
SUM of term 50: 10771473440624625
SUM of term 60: 65630962547279460
SUM of term 70: 303084330232704265
SUM of term 80: 1142108795719679040
SUM of term 90: 3683722777599103785
SUM of term 100: 10507499300049998500
-------------------------------------------------------

POWER: 10
POLYNOMIAL: ( 1 / 11 ) * x^11 + ( 1 / 2 ) * x^10 + ( 5 / 6 ) * x^9 + 0 * x^8 + -1 * x^7 + 0 * x^6 + 1 * x^5 + 0 * x^4 + ( -1 / 2 ) * x^3 + 0 * x^2 + ( 5 / 66 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 14914341925
SUM of term 20: 24163571680850
SUM of term 30: 1922052927013775
SUM of term 40: 43591205959337700
SUM of term 50: 494346993683649625
SUM of term 60: 3608881215962946550
SUM of term 70: 19421693680720225475
SUM of term 80: 83570850731150483400
SUM of term 90: 303039084670532717325
SUM of term 100: 959924142434241924250
-------------------------------------------------------

POWER: 11
POLYNOMIAL: ( 1 / 12 ) * x^12 + ( 1 / 2 ) * x^11 + ( 11 / 12 ) * x^10 + 0 * x^9 + ( -11 / 8 ) * x^8 + 0 * x^7 + ( 11 / 6 ) * x^6 + 0 * x^5 + ( -11 / 8 ) * x^4 + 0 * x^3 + ( 5 / 12 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 142364319625
SUM of term 20: 453084917113500
SUM of term 30: 53684481697886625
SUM of term 40: 1617419476305814000
SUM of term 50: 22875922880199740625
SUM of term 60: 200092423218318181500
SUM of term 70: 1254895501238019321625
SUM of term 80: 6165960117933341016000
SUM of term 90: 25136803959592580789625
SUM of term 100: 88424986251833195837500
-------------------------------------------------------

POWER: 12
POLYNOMIAL: ( 1 / 13 ) * x^13 + ( 1 / 2 ) * x^12 + 1 * x^11 + 0 * x^10 + ( -11 / 6 ) * x^9 + 0 * x^8 + ( 22 / 7 ) * x^7 + 0 * x^6 + ( -33 / 10 ) * x^5 + 0 * x^4 + ( 5 / 3 ) * x^3 + 0 * x^2 + ( -691 / 2730 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 1367428536133
SUM of term 20: 8553403807182266
SUM of term 30: 1509801490846448399
SUM of term 40: 60429761394177644532
SUM of term 50: 1065951950571313280665
SUM of term 60: 11171340111234807466798
SUM of term 70: 81648310324449016312931
SUM of term 80: 458107573433418858329064
SUM of term 90: 2099633570487728974825197
SUM of term 100: 8202305859288611690311330
-------------------------------------------------------

POWER: 13
POLYNOMIAL: ( 1 / 14 ) * x^14 + ( 1 / 2 ) * x^13 + ( 13 / 12 ) * x^12 + 0 * x^11 + ( -143 / 60 ) * x^10 + 0 * x^9 + ( 143 / 28 ) * x^8 + 0 * x^7 + ( -143 / 20 ) * x^6 + 0 * x^5 + ( 65 / 12 ) * x^4 + 0 * x^3 + ( -691 / 420 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 13202860761145
SUM of term 20: 162401629714694580
SUM of term 30: 42710003046802750305
SUM of term 40: 2271090793998613178320
SUM of term 50: 49964308932645011528625
SUM of term 60: 627404239948085222651220
SUM of term 70: 5343883570802640664696105
SUM of term 80: 34237817523414160635113280
SUM of term 90: 176420871785697206848652745
SUM of term 100: 765368809336778564827364500
-------------------------------------------------------

POWER: 14
POLYNOMIAL: ( 1 / 15 ) * x^15 + ( 1 / 2 ) * x^14 + ( 7 / 6 ) * x^13 + 0 * x^12 + ( -91 / 30 ) * x^11 + 0 * x^10 + ( 143 / 18 ) * x^9 + 0 * x^8 + ( -143 / 10 ) * x^7 + 0 * x^6 + ( 91 / 6 ) * x^5 + 0 * x^4 + ( -691 / 90 ) * x^3 + 0 * x^2 + ( 7 / 6 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 128037802953445
SUM of term 20: 3098689489300027490
SUM of term 30: 1214289106468127342735
SUM of term 40: 85786227621367085019780
SUM of term 50: 2353907730349075919179225
SUM of term 60: 35416138638301356943941670
SUM of term 70: 351545026624755537783427715
SUM of term 80: 2571938344758519200513757960
SUM of term 90: 14899560681210896946485053005
SUM of term 100: 71783303007943014596103433450
-------------------------------------------------------

POWER: 15
POLYNOMIAL: ( 1 / 16 ) * x^16 + ( 1 / 2 ) * x^15 + ( 5 / 4 ) * x^14 + 0 * x^13 + ( -91 / 24 ) * x^12 + 0 * x^11 + ( 143 / 12 ) * x^10 + 0 * x^9 + ( -429 / 16 ) * x^8 + 0 * x^7 + ( 455 / 12 ) * x^6 + 0 * x^5 + ( -691 / 24 ) * x^4 + 0 * x^3 + ( 35 / 4 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 1246324856379625
SUM of term 20: 59376590676022063500
SUM of term 30: 34674517221983436686625
SUM of term 40: 3254716415169076832974000
SUM of term 50: 111388235619070416486740625
SUM of term 60: 2008073458528026938266891500
SUM of term 70: 23229087797177127634985421625
SUM of term 80: 194063541869023969388047416000
SUM of term 90: 1263941712673329168455401049625
SUM of term 100: 6762496209524731912913787587500
-------------------------------------------------------

POWER: 16
POLYNOMIAL: ( 1 / 17 ) * x^17 + ( 1 / 2 ) * x^16 + ( 4 / 3 ) * x^15 + 0 * x^14 + ( -14 / 3 ) * x^13 + 0 * x^12 + ( 52 / 3 ) * x^11 + 0 * x^10 + ( -143 / 3 ) * x^9 + 0 * x^8 + ( 260 / 3 ) * x^7 + 0 * x^6 + ( -1382 / 15 ) * x^5 + 0 * x^4 + ( 140 / 3 ) * x^3 + 0 * x^2 + ( -3617 / 510 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 12170706132009733
SUM of term 20: 1142003663611187899466
SUM of term 30: 993939403025528985949199
SUM of term 40: 123961421779521671133238932
SUM of term 50: 5291451811717630485920048665
SUM of term 60: 114300438948397316881214258398
SUM of term 70: 1540905004959594729319355748131
SUM of term 80: 14700142996255279017152050797864
SUM of term 90: 107640572709256841678163266487597
SUM of term 100: 639568160957599400822608125097330
-------------------------------------------------------

POWER: 17
POLYNOMIAL: ( 1 / 18 ) * x^18 + ( 1 / 2 ) * x^17 + ( 17 / 12 ) * x^16 + 0 * x^15 + ( -17 / 3 ) * x^14 + 0 * x^13 + ( 221 / 9 ) * x^12 + 0 * x^11 + ( -2431 / 30 ) * x^10 + 0 * x^9 + ( 1105 / 6 ) * x^8 + 0 * x^7 + ( -11747 / 45 ) * x^6 + 0 * x^5 + ( 595 / 3 ) * x^4 + 0 * x^3 + ( -3617 / 60 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 119179318935377305
SUM of term 20: 22036397710027769309220
SUM of term 30: 28587499850500268609195745
SUM of term 40: 4737435834482524911714036880
SUM of term 50: 252232807636408014585614432625
SUM of term 60: 6528474157881238346799280582980
SUM of term 70: 102569363668476175807716338287945
SUM of term 80: 1117374979507992438815701332947520
SUM of term 90: 9198688097575345728201118041561705
SUM of term 100: 60697165580103009619183419832730500
-------------------------------------------------------

POWER: 18
POLYNOMIAL: ( 1 / 19 ) * x^19 + ( 1 / 2 ) * x^18 + ( 3 / 2 ) * x^17 + 0 * x^16 + ( -34 / 5 ) * x^15 + 0 * x^14 + 34 * x^13 + 0 * x^12 + ( -663 / 5 ) * x^11 + 0 * x^10 + ( 1105 / 3 ) * x^9 + 0 * x^8 + ( -23494 / 35 ) * x^7 + 0 * x^6 + 714 * x^5 + 0 * x^4 + ( -3617 / 10 ) * x^3 + 0 * x^2 + ( 43867 / 798 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 1169842891165484965
SUM of term 20: 426453788542828686799730
SUM of term 30: 824700797689433390367774095
SUM of term 40: 181602022664795798585548237860
SUM of term 50: 12060259460444952018292472020825
SUM of term 60: 374031437065955427645001574952790
SUM of term 70: 6848487644168540665630033332863555
SUM of term 80: 85194829147159262964944599309582920
SUM of term 90: 788522083956512918422865075044940685
SUM of term 100: 5778151098135516473529372653422766650
-------------------------------------------------------

POWER: 19
POLYNOMIAL: ( 1 / 20 ) * x^20 + ( 1 / 2 ) * x^19 + ( 19 / 12 ) * x^18 + 0 * x^17 + ( -323 / 40 ) * x^16 + 0 * x^15 + ( 323 / 7 ) * x^14 + 0 * x^13 + ( -4199 / 20 ) * x^12 + 0 * x^11 + ( 4199 / 6 ) * x^10 + 0 * x^9 + ( -223193 / 140 ) * x^8 + 0 * x^7 + 2261 * x^6 + 0 * x^5 + ( -68723 / 40 ) * x^4 + 0 * x^3 + ( 43867 / 84 ) * x^2 + 0 * x^1 + 0

SUM of term 0: 0
SUM of term 10: 11506994510201252425
SUM of term 20: 8274164048960901518840700
SUM of term 30: 23855191050350940875254257825
SUM of term 40: 6980407928279022508351576658800
SUM of term 50: 578232233820997526581169322860625
SUM of term 60: 21488166721605375271461211317342300
SUM of term 70: 458531448512418136138005100812244825
SUM of term 80: 6513683552228581040401031656247371200
SUM of term 90: 67780086196990388199328860333130186425
SUM of term 100: 551582526294552024729297998923435817500
-------------------------------------------------------

POWER: 20
POLYNOMIAL: ( 1 / 21 ) * x^21 + ( 1 / 2 ) * x^20 + ( 5 / 3 ) * x^19 + 0 * x^18 + ( -19 / 2 ) * x^17 + 0 * x^16 + ( 1292 / 21 ) * x^15 + 0 * x^14 + -323 * x^13 + 0 * x^12 + ( 41990 / 33 ) * x^11 + 0 * x^10 + ( -223193 / 63 ) * x^9 + 0 * x^8 + 6460 * x^7 + 0 * x^6 + ( -68723 / 10 ) * x^5 + 0 * x^4 + ( 219335 / 63 ) * x^3 + 0 * x^2 + ( -174611 / 330 ) * x^1 + 0

SUM of term 0: 0
SUM of term 10: 113394131858832552133
SUM of term 20: 160908785696531607621474266
SUM of term 30: 691700496303093161541855536399
SUM of term 40: 268971411049648078275152088308532
SUM of term 50: 27792071444979815655627001470560665
SUM of term 60: 1237564563389799704344023035282662798
SUM of term 70: 30776796293294568246976963626466984931
SUM of term 80: 499254050215865400586705364941160297064
SUM of term 90: 5840809691465323098310800385808226169197
SUM of term 100: 52785619347205807958795562237196787371330
-------------------------------------------------------
