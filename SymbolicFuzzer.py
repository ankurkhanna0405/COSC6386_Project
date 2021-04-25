from fuzzingbook.SymbolicFuzzer import  SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
from examples.pyth_triplet import PythogareanTriplets
from fuzzingbook.ControlFlow import PyCFG, CFGNode, to_graph, gen_cfg
import inspect
from graphviz import Source, Graph

def show_cfg(fn, **kwargs):
    return Source(to_graph(gen_cfg(inspect.getsource(fn)), **kwargs))

#func = examples.pyth_triplet

symfz_ct = SimpleSymbolicFuzzer(PythogareanTriplets)
paths = symfz_ct.get_all_paths(symfz_ct.fnenter)


print(symfz_ct.extract_constraints(paths[0]))
print(symfz_ct.solve_path_constraint(paths[0]))
show_cfg(PythogareanTriplets)