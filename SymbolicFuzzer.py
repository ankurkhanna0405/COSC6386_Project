from fuzzingbook.SymbolicFuzzer import  SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
from examples.pyth_triplet import PythogareanTriplets
from examples.check_triangle import check_triangle
from fuzzingbook.ControlFlow import PyCFG, CFGNode, to_graph, gen_cfg
import inspect
from graphviz import Source, Graph

def show_cfg(fn, **kwargs):
    return Source(to_graph(gen_cfg(inspect.getsource(fn)), **kwargs))

# Simple symbolic fuzzer for example PythogareanTriplets.py
print(" Fuzzer output for PythogareanTriplets")

simp_fzzr_pyth = SimpleSymbolicFuzzer(PythogareanTriplets)
paths = simp_fzzr_pyth.get_all_paths(simp_fzzr_pyth.fnenter)

for i in range(len(paths)):
    print("Path",i)
    print("Constraint found is: ",simp_fzzr_pyth.extract_constraints(paths[i]))
    print("Z3 solver solution for the above constraint is:",simp_fzzr_pyth.solve_path_constraint(paths[i]))
print("*************************----------------------------------*****************************************")
# Simple symbolic fuzzer for example CheckTriangle.py
print(" Fuzzer output for Check Triangle")

simp_fzzr_triangle = SimpleSymbolicFuzzer(check_triangle)
paths = simp_fzzr_triangle.get_all_paths(simp_fzzr_triangle.fnenter)

for i in range(len(paths)):
    print("Path",i)
    print("Constraint found is: ",simp_fzzr_triangle.extract_constraints(paths[i]))
    print("Z3 solver solution for the above constraint is:",simp_fzzr_triangle.solve_path_constraint(paths[i]))
