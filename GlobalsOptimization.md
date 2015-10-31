
```
import new
from dis import opmap, opname, HAVE_ARGUMENT, EXTENDED_ARG
import dis
import compiler
twobyte = compiler.pycodegen.pyassem.twobyte

      
def opcode_iter(codeobj):
    """
        Generator yielding (opcode, argument) pairs
        for a code object
    """
    code = list(reversed(codeobj.co_code))
    extended_arg = 0
    while code:
        op = ord(code.pop())
        if op >= HAVE_ARGUMENT:
            oparg = ord(code.pop()) + ord(code.pop())*256 + extended_arg
            extended_arg = 0
            if op == EXTENDED_ARG:
                extended_arg = oparg*65536L
        else:
            oparg = None
        yield op, oparg
    
def find_globals(codeobj):
    load_global = opmap["LOAD_GLOBAL"]
    return [
        (codeobj.co_names[arg], arg) for op, arg in opcode_iter(codeobj) if op == load_global
    ]
    
def optimize_globals(func):
    """ Decorator optimizes a function by 
        replacing all global lookups resolvable
        at the time of execution with constants.
    """
    codeobj = func.func_code
    old_consts = codeobj.co_consts
    optimized = []
    new_consts = []
    new_offset_map = {}
    for uglobal, offset in find_globals(codeobj):
        print "looking up %s(%s)" % (uglobal, offset),
        if offset in optimized:
            print 'already optimized'
            continue
        try:
            try:
                v = func.func_globals[uglobal]
            except KeyError:
                v = __builtins__[uglobal]
        except KeyError:
            print uglobal, "not optimized"
            pass
        else:
            print "found as ", v
            optimized.append(offset)
            new_offset_map[offset] = len(new_consts)
            new_consts.append(v)
    newcodedata = []
    new_consts = old_consts + tuple(new_consts)
    offset = len(old_consts)
    for op, arg in opcode_iter(codeobj):
        if op == opmap["LOAD_GLOBAL"] and arg in optimized:
            newcodedata.append(opmap["LOAD_CONST"])
            ofs = new_offset_map[arg] + offset
            newcodedata.extend(reversed(twobyte(ofs)))
        else:
            newcodedata.append(op)
            if arg is not None:
                newcodedata.extend(reversed(twobyte(arg)))
    newcodestring = ''.join(map(chr, newcodedata))
    newcode = new.code(
        codeobj.co_argcount,
        codeobj.co_nlocals,
        codeobj.co_stacksize,
        codeobj.co_flags,
        newcodestring,
        #codeobj.co_consts,
        new_consts,
        codeobj.co_names,
        codeobj.co_varnames,
        codeobj.co_filename,
        codeobj.co_name,
        codeobj.co_firstlineno,
        codeobj.co_lnotab,
        codeobj.co_freevars,
        codeobj.co_cellvars
    )
    return new.function(
        newcode,
        func.func_globals,
        func.func_name,
        func.func_defaults,
        func.func_closure
    )
    

x = 10
z = 10
def a_global():
    for a in xrange(1000):
        y = x + z
    
def a_argument(x=x):
    y = x + z

@optimize_globals
def a_optimized():
    for a in xrange(1000):
            y = x + z

if __name__ == '__main__':
    x = dis
    def a():
        foo = 10
        print x
        #print y
        print foo
    #~ na = optimize_globals(a)
    #~ print dis.dis(na)
    #~ print "-" * 10
    #~ print dis.dis(a)
    #~ a()
    #~ na()
```