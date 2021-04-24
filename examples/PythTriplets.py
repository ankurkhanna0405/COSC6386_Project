

import fuzzingbook_utils
from ControlFlow import PyCFG, CFGNode, to_graph, gen_cfg
import inspect
from graphviz import Source, Graph



def PythogareanTriplets(a:int ,b: int, c:int) -> str:
    if (a*a + b*b ) == (c*c):
        return "Pyth Triplet"
    else:
        return "Not Triplet"




def show_cfg(fn, **kwargs):
    return Source(to_graph(gen_cfg(inspect.getsource(fn)), **kwargs))


show_cfg(PythogareanTriplets)


import z3



def get_annotations(fn):
    sig = inspect.signature(fn)
    return ([(i.name, i.annotation)
             for i in sig.parameters.values()], sig.return_annotation)



params, ret = get_annotations(PythogareanTriplets)
params, ret



SYM_VARS = {
    int: (
        z3.Int, z3.IntVal), float: (
            z3.Real, z3.RealVal), str: (
                z3.String, z3.StringVal)}



def get_symbolicparams(fn):
    params, ret = get_annotations(fn)
    return [SYM_VARS[typ][0](name)
            for name, typ in params], SYM_VARS[ret][0]('__return__')



(a,b,c), r = get_symbolicparams(PythogareanTriplets)
a,b,c, r


z3.solve(a>0,b>0,c>0, a*a + b*b == c*c)




