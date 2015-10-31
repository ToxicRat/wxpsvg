
```
-------------------------------------------------------------------------------
PYBENCH 2.0
-------------------------------------------------------------------------------
* using CPython 2.6a0 (trunk:59136, Nov 23 2007, 11:55:33) [MSC v.1500 32 bit (Intel)]
* disabled garbage collection
* system check interval set to maximum: 2147483647
* using timer: time.clock

Calibrating tests. Please wait... done.

Running 10 round(s) of the suite at warp factor 10:

* Round 1 done in 5.707 seconds.
* Round 2 done in 5.500 seconds.
* Round 3 done in 5.588 seconds.
* Round 4 done in 5.516 seconds.
* Round 5 done in 5.605 seconds.
* Round 6 done in 5.511 seconds.
* Round 7 done in 5.557 seconds.
* Round 8 done in 5.519 seconds.
* Round 9 done in 5.600 seconds.
* Round 10 done in 5.639 seconds.

-------------------------------------------------------------------------------
Benchmark: 2007-11-23 11:59:57
-------------------------------------------------------------------------------

    Rounds: 10
    Warp:   10
    Timer:  time.clock

    Machine Details:
       Platform ID:    Windows-XP-5.1.2600
       Processor:      
    
    Python:
       Implementation: CPython
       Executable:     C:\pbuild2.6\trunk\PCbuild9\python.exe
       Version:        2.6.0
       Compiler:       MSC v.1500 32 bit (Intel)
       Bits:           32bit
       Build:          Nov 23 2007 11:55:33 (#trunk:59136)
       Unicode:        UCS2


Test                             minimum  average  operation  overhead
-------------------------------------------------------------------------------
          BuiltinFunctionCalls:    123ms    124ms    0.24us    0.171ms
           BuiltinMethodLookup:     93ms     94ms    0.09us    0.198ms
                 CompareFloats:     82ms     82ms    0.07us    0.225ms
         CompareFloatsIntegers:     81ms     82ms    0.09us    0.169ms
               CompareIntegers:     81ms     81ms    0.05us    0.341ms
        CompareInternedStrings:     85ms     87ms    0.06us    0.862ms
                  CompareLongs:     72ms     72ms    0.07us    0.199ms
                CompareStrings:     67ms     67ms    0.07us    0.582ms
                CompareUnicode:     78ms     79ms    0.10us    0.445ms
                 ConcatStrings:    183ms    214ms    0.43us    0.385ms
                 ConcatUnicode:    179ms    197ms    0.66us    0.275ms
               CreateInstances:    131ms    133ms    1.19us    0.232ms
            CreateNewInstances:    114ms    117ms    1.39us    0.234ms
       CreateStringsWithConcat:    100ms    102ms    0.10us    0.572ms
       CreateUnicodeWithConcat:    119ms    120ms    0.30us    0.227ms
                  DictCreation:     76ms     77ms    0.19us    0.228ms
             DictWithFloatKeys:    193ms    195ms    0.22us    0.422ms
           DictWithIntegerKeys:     72ms     74ms    0.06us    0.567ms
            DictWithStringKeys:     68ms     70ms    0.06us    0.572ms
                      ForLoops:     63ms     64ms    2.55us    0.043ms
                    IfThenElse:     75ms     76ms    0.06us    0.429ms
                   ListSlicing:     99ms    102ms    7.30us    0.062ms
                NestedForLoops:     83ms     85ms    0.06us    0.017ms
          NormalClassAttribute:     91ms     93ms    0.08us    0.287ms
       NormalInstanceAttribute:     92ms     93ms    0.08us    0.287ms
           PythonFunctionCalls:    105ms    108ms    0.33us    0.170ms
             PythonMethodCalls:    133ms    136ms    0.60us    0.088ms
                     Recursion:    129ms    132ms    2.65us    0.284ms
                  SecondImport:     93ms     96ms    0.96us    0.114ms
           SecondPackageImport:    108ms    109ms    1.09us    0.114ms
         SecondSubmoduleImport:    132ms    137ms    1.37us    0.112ms
       SimpleComplexArithmetic:    110ms    111ms    0.13us    0.225ms
        SimpleDictManipulation:     77ms     79ms    0.07us    0.282ms
         SimpleFloatArithmetic:     90ms     92ms    0.07us    0.338ms
      SimpleIntFloatArithmetic:     71ms     72ms    0.05us    0.341ms
       SimpleIntegerArithmetic:     72ms     75ms    0.06us    0.342ms
        SimpleListManipulation:     66ms     67ms    0.06us    0.370ms
          SimpleLongArithmetic:     87ms     87ms    0.13us    0.170ms
                    SmallLists:    134ms    136ms    0.20us    0.227ms
                   SmallTuples:    119ms    120ms    0.22us    0.262ms
         SpecialClassAttribute:     89ms     90ms    0.08us    0.287ms
      SpecialInstanceAttribute:    102ms    104ms    0.09us    0.286ms
                StringMappings:    152ms    154ms    0.61us    0.299ms
              StringPredicates:    123ms    125ms    0.18us    1.497ms
                 StringSlicing:    130ms    137ms    0.24us    0.506ms
                     TryExcept:     71ms     72ms    0.03us    0.427ms
                TryRaiseExcept:    166ms    174ms    2.72us    0.228ms
                  TupleSlicing:    117ms    119ms    0.45us    0.039ms
               UnicodeMappings:    112ms    113ms    3.14us    0.429ms
             UnicodePredicates:    108ms    109ms    0.20us    1.785ms
             UnicodeProperties:     96ms     98ms    0.24us    1.502ms
                UnicodeSlicing:    142ms    145ms    0.30us    0.450ms
-------------------------------------------------------------------------------
Totals:                           5437ms   5574ms

```