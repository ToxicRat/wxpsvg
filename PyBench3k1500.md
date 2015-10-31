
```
-------------------------------------------------------------------------------
PYBENCH 2.0
-------------------------------------------------------------------------------
* using CPython 3.0a1+ (py3k:59136, Nov 23 2007, 12:11:02) [MSC v.1500 32 bit (Intel)]
* disabled garbage collection
* system check interval set to maximum: 2147483647
* using timer: time.clock

Calibrating tests. Please wait... done.

Running 10 round(s) of the suite at warp factor 10:

* Round 1 done in 6.389 seconds.
* Round 2 done in 6.249 seconds.
* Round 3 done in 6.274 seconds.
* Round 4 done in 6.367 seconds.
* Round 5 done in 6.318 seconds.
* Round 6 done in 6.426 seconds.
* Round 7 done in 6.453 seconds.
* Round 8 done in 6.414 seconds.
* Round 9 done in 6.316 seconds.
* Round 10 done in 6.378 seconds.

-------------------------------------------------------------------------------
Benchmark: 2007-11-23 12:16:00
-------------------------------------------------------------------------------

    Rounds: 10
    Warp:   10
    Timer:  time.clock

    Machine Details:
       Platform ID:    Windows-XP-5.1.2600
       Processor:      
    
    Python:
       Implementation: CPython
       Executable:     C:\pbuild3k\py3k\PCbuild9\python.exe
       Version:        3.0.0
       Compiler:       MSC v.1500 32 bit (Intel)
       Bits:           32bit
       Build:          Nov 23 2007 12:11:02 (#py3k:59136)
       Unicode:        None


Test                             minimum  average  operation  overhead
-------------------------------------------------------------------------------
          BuiltinFunctionCalls:     92ms     93ms    0.18us    0.274ms
           BuiltinMethodLookup:     78ms     79ms    0.08us    0.311ms
                 CompareFloats:     76ms     76ms    0.06us    0.370ms
         CompareFloatsIntegers:    234ms    234ms    0.26us    0.273ms
               CompareIntegers:    116ms    117ms    0.07us    0.543ms
        CompareInternedStrings:    125ms    127ms    0.08us    1.411ms
                  CompareLongs:     77ms     77ms    0.07us    0.314ms
                CompareStrings:     84ms     85ms    0.08us    0.980ms
                 ConcatStrings:    173ms    231ms    0.46us    0.622ms
               CreateInstances:    157ms    159ms    1.42us    0.441ms
            CreateNewInstances:    118ms    119ms    1.42us    0.358ms
       CreateStringsWithConcat:    243ms    274ms    0.27us    0.915ms
                  DictCreation:     76ms     76ms    0.19us    0.361ms
             DictWithFloatKeys:    179ms    183ms    0.20us    0.688ms
           DictWithIntegerKeys:     70ms     71ms    0.06us    0.988ms
            DictWithStringKeys:     67ms     69ms    0.06us    1.021ms
                      ForLoops:     72ms     78ms    3.12us    0.041ms
                    IfThenElse:     95ms     98ms    0.07us    0.688ms
                   ListSlicing:    101ms    103ms    7.39us    0.065ms
                NestedForLoops:     96ms     96ms    0.06us    0.001ms
          NormalClassAttribute:    249ms    252ms    0.21us    0.493ms
       NormalInstanceAttribute:    167ms    172ms    0.14us    0.492ms
           PythonFunctionCalls:     96ms     99ms    0.30us    0.269ms
             PythonMethodCalls:    153ms    160ms    0.71us    0.168ms
                     Recursion:    178ms    179ms    3.58us    0.451ms
                  SecondImport:    134ms    139ms    1.39us    0.178ms
           SecondPackageImport:    144ms    149ms    1.49us    0.180ms
         SecondSubmoduleImport:    191ms    200ms    2.00us    0.179ms
       SimpleComplexArithmetic:     94ms     95ms    0.11us    0.364ms
        SimpleDictManipulation:    138ms    142ms    0.12us    0.465ms
         SimpleFloatArithmetic:     78ms     80ms    0.06us    0.541ms
      SimpleIntFloatArithmetic:    137ms    139ms    0.11us    0.539ms
       SimpleIntegerArithmetic:    136ms    139ms    0.11us    0.547ms
        SimpleListManipulation:     72ms     74ms    0.06us    0.616ms
          SimpleLongArithmetic:    101ms    101ms    0.15us    0.269ms
                    SmallLists:    145ms    149ms    0.22us    0.358ms
                   SmallTuples:    125ms    127ms    0.23us    0.403ms
         SpecialClassAttribute:    269ms    273ms    0.23us    0.494ms
      SpecialInstanceAttribute:    169ms    171ms    0.14us    0.493ms
                StringMappings:    304ms    306ms    1.21us    0.476ms
              StringPredicates:    148ms    150ms    0.21us    2.337ms
                 StringSlicing:    199ms    204ms    0.36us    0.809ms
                     TryExcept:     97ms     98ms    0.04us    0.688ms
                TryRaiseExcept:    151ms    156ms    2.43us    0.368ms
                  TupleSlicing:    152ms    160ms    0.61us    0.044ms
-------------------------------------------------------------------------------
Totals:                           6153ms   6358ms

```