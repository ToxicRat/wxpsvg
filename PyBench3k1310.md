
```
-------------------------------------------------------------------------------
PYBENCH 2.0
-------------------------------------------------------------------------------
* using CPython 3.0a1+ (py3k:59136, Nov 23 2007, 12:08:13) [MSC v.1310 32 bit (Intel)]
* disabled garbage collection
* system check interval set to maximum: 2147483647
* using timer: time.clock

Calibrating tests. Please wait... done.

Running 10 round(s) of the suite at warp factor 10:

* Round 1 done in 6.276 seconds.
* Round 2 done in 6.266 seconds.
* Round 3 done in 6.281 seconds.
* Round 4 done in 6.259 seconds.
* Round 5 done in 6.292 seconds.
* Round 6 done in 6.281 seconds.
* Round 7 done in 6.271 seconds.
* Round 8 done in 6.290 seconds.
* Round 9 done in 6.300 seconds.
* Round 10 done in 6.262 seconds.

-------------------------------------------------------------------------------
Benchmark: 2007-11-23 12:13:07
-------------------------------------------------------------------------------

    Rounds: 10
    Warp:   10
    Timer:  time.clock

    Machine Details:
       Platform ID:    Windows-XP-5.1.2600
       Processor:      
    
    Python:
       Implementation: CPython
       Executable:     C:\pbuild3k\py3k\PCbuild\python.exe
       Version:        3.0.0
       Compiler:       MSC v.1310 32 bit (Intel)
       Bits:           32bit
       Build:          Nov 23 2007 12:08:13 (#py3k:59136)
       Unicode:        None


Test                             minimum  average  operation  overhead
-------------------------------------------------------------------------------
          BuiltinFunctionCalls:     84ms     85ms    0.17us    0.260ms
           BuiltinMethodLookup:     82ms     83ms    0.08us    0.300ms
                 CompareFloats:     83ms     83ms    0.07us    0.350ms
         CompareFloatsIntegers:    232ms    232ms    0.26us    0.257ms
               CompareIntegers:    119ms    119ms    0.07us    0.518ms
        CompareInternedStrings:    127ms    128ms    0.09us    1.327ms
                  CompareLongs:     79ms     79ms    0.08us    0.300ms
                CompareStrings:     84ms     95ms    0.09us    0.912ms
                 ConcatStrings:    178ms    182ms    0.36us    0.615ms
               CreateInstances:    150ms    151ms    1.35us    0.417ms
            CreateNewInstances:    112ms    113ms    1.35us    0.341ms
       CreateStringsWithConcat:    267ms    284ms    0.28us    0.857ms
                  DictCreation:     75ms     76ms    0.19us    0.344ms
             DictWithFloatKeys:    176ms    178ms    0.20us    0.648ms
           DictWithIntegerKeys:     72ms     73ms    0.06us    0.912ms
            DictWithStringKeys:     76ms     78ms    0.07us    0.865ms
                      ForLoops:     77ms     77ms    3.08us    0.040ms
                    IfThenElse:    105ms    105ms    0.08us    0.648ms
                   ListSlicing:    100ms    104ms    7.40us    0.071ms
                NestedForLoops:     98ms     98ms    0.07us    0.001ms
          NormalClassAttribute:    245ms    252ms    0.21us    0.463ms
       NormalInstanceAttribute:    170ms    172ms    0.14us    0.463ms
           PythonFunctionCalls:     94ms     95ms    0.29us    0.258ms
             PythonMethodCalls:    156ms    161ms    0.71us    0.166ms
                     Recursion:    164ms    170ms    3.41us    0.431ms
                  SecondImport:    151ms    152ms    1.52us    0.170ms
           SecondPackageImport:    162ms    164ms    1.64us    0.170ms
         SecondSubmoduleImport:    217ms    219ms    2.19us    0.169ms
       SimpleComplexArithmetic:     83ms     83ms    0.09us    0.344ms
        SimpleDictManipulation:    134ms    135ms    0.11us    0.433ms
         SimpleFloatArithmetic:     76ms     77ms    0.06us    0.520ms
      SimpleIntFloatArithmetic:    157ms    158ms    0.12us    0.519ms
       SimpleIntegerArithmetic:    156ms    158ms    0.12us    0.511ms
        SimpleListManipulation:     72ms     73ms    0.06us    0.585ms
          SimpleLongArithmetic:     99ms    100ms    0.15us    0.257ms
                    SmallLists:    151ms    152ms    0.22us    0.344ms
                   SmallTuples:    143ms    144ms    0.27us    0.388ms
         SpecialClassAttribute:    265ms    267ms    0.22us    0.469ms
      SpecialInstanceAttribute:    170ms    173ms    0.14us    0.469ms
                StringMappings:    253ms    255ms    1.01us    0.461ms
              StringPredicates:    119ms    120ms    0.17us    2.327ms
                 StringSlicing:    212ms    215ms    0.38us    0.789ms
                     TryExcept:     67ms     67ms    0.03us    0.649ms
                TryRaiseExcept:    153ms    154ms    2.41us    0.342ms
                  TupleSlicing:    136ms    137ms    0.52us    0.048ms
-------------------------------------------------------------------------------
Totals:                           6179ms   6278ms

```