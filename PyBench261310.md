
```
-------------------------------------------------------------------------------
PYBENCH 2.0
-------------------------------------------------------------------------------
* using CPython 2.6a0 (trunk:59136, Nov 23 2007, 11:55:40) [MSC v.1310 32 bit (Intel)]
* disabled garbage collection
* system check interval set to maximum: 2147483647
* using timer: time.clock

Calibrating tests. Please wait... done.

Running 10 round(s) of the suite at warp factor 10:

* Round 1 done in 5.853 seconds.
* Round 2 done in 5.877 seconds.
* Round 3 done in 5.967 seconds.
* Round 4 done in 5.897 seconds.
* Round 5 done in 5.909 seconds.
* Round 6 done in 5.855 seconds.
* Round 7 done in 5.862 seconds.
* Round 8 done in 5.860 seconds.
* Round 9 done in 5.923 seconds.
* Round 10 done in 5.941 seconds.

-------------------------------------------------------------------------------
Benchmark: 2007-11-23 11:58:03
-------------------------------------------------------------------------------

    Rounds: 10
    Warp:   10
    Timer:  time.clock

    Machine Details:
       Platform ID:    Windows-XP-5.1.2600
       Processor:      
    
    Python:
       Implementation: CPython
       Executable:     C:\pbuild2.6\trunk\PCbuild\python.exe
       Version:        2.6.0
       Compiler:       MSC v.1310 32 bit (Intel)
       Bits:           32bit
       Build:          Nov 23 2007 11:55:40 (#trunk:59136)
       Unicode:        UCS2


Test                             minimum  average  operation  overhead
-------------------------------------------------------------------------------
          BuiltinFunctionCalls:    127ms    129ms    0.25us    0.158ms
           BuiltinMethodLookup:     97ms     98ms    0.09us    0.219ms
                 CompareFloats:     77ms     77ms    0.06us    0.219ms
         CompareFloatsIntegers:     84ms     85ms    0.09us    0.163ms
               CompareIntegers:     77ms     78ms    0.04us    0.330ms
        CompareInternedStrings:     84ms     87ms    0.06us    0.820ms
                  CompareLongs:     68ms     70ms    0.07us    0.192ms
                CompareStrings:    102ms    107ms    0.11us    0.543ms
                CompareUnicode:     76ms     77ms    0.10us    0.425ms
                 ConcatStrings:    178ms    181ms    0.36us    0.361ms
                 ConcatUnicode:    174ms    213ms    0.71us    0.265ms
               CreateInstances:    130ms    131ms    1.17us    0.222ms
            CreateNewInstances:    108ms    111ms    1.32us    0.225ms
       CreateStringsWithConcat:     97ms     98ms    0.10us    0.544ms
       CreateUnicodeWithConcat:    112ms    114ms    0.28us    0.216ms
                  DictCreation:     73ms     74ms    0.18us    0.210ms
             DictWithFloatKeys:    186ms    188ms    0.21us    0.397ms
           DictWithIntegerKeys:     69ms     71ms    0.06us    0.545ms
            DictWithStringKeys:     65ms     66ms    0.06us    0.528ms
                      ForLoops:     57ms     59ms    2.38us    0.040ms
                    IfThenElse:     73ms     74ms    0.06us    0.461ms
                   ListSlicing:     99ms    101ms    7.25us    0.057ms
                NestedForLoops:     78ms     79ms    0.05us    0.016ms
          NormalClassAttribute:     92ms     93ms    0.08us    0.275ms
       NormalInstanceAttribute:     85ms     87ms    0.07us    0.291ms
           PythonFunctionCalls:     93ms     94ms    0.28us    0.164ms
             PythonMethodCalls:    129ms    133ms    0.59us    0.084ms
                     Recursion:    120ms    123ms    2.45us    0.263ms
                  SecondImport:    113ms    114ms    1.14us    0.105ms
           SecondPackageImport:    124ms    126ms    1.26us    0.109ms
         SecondSubmoduleImport:    155ms    159ms    1.59us    0.109ms
       SimpleComplexArithmetic:    100ms    105ms    0.12us    0.211ms
        SimpleDictManipulation:     76ms     77ms    0.06us    0.263ms
         SimpleFloatArithmetic:    104ms    104ms    0.08us    0.318ms
      SimpleIntFloatArithmetic:     78ms     79ms    0.06us    0.315ms
       SimpleIntegerArithmetic:     78ms     79ms    0.06us    0.318ms
        SimpleListManipulation:     68ms     70ms    0.06us    0.357ms
          SimpleLongArithmetic:     85ms     89ms    0.13us    0.157ms
                    SmallLists:    131ms    135ms    0.20us    0.210ms
                   SmallTuples:    103ms    105ms    0.19us    0.238ms
         SpecialClassAttribute:     91ms     92ms    0.08us    0.270ms
      SpecialInstanceAttribute:    164ms    166ms    0.14us    0.269ms
                StringMappings:    374ms    377ms    1.50us    0.289ms
              StringPredicates:    149ms    151ms    0.22us    1.681ms
                 StringSlicing:    128ms    129ms    0.23us    0.522ms
                     TryExcept:     62ms     63ms    0.03us    0.396ms
                TryRaiseExcept:    201ms    205ms    3.20us    0.217ms
                  TupleSlicing:    108ms    110ms    0.42us    0.037ms
               UnicodeMappings:     89ms     90ms    2.50us    0.438ms
             UnicodePredicates:     98ms    101ms    0.19us    1.972ms
             UnicodeProperties:    124ms    126ms    0.31us    1.652ms
                UnicodeSlicing:    143ms    146ms    0.30us    0.423ms
-------------------------------------------------------------------------------
Totals:                           5757ms   5894ms


```