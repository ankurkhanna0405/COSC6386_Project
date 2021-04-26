from fuzzingbook.SymbolicFuzzer import  AdvancedSymbolicFuzzer
from examples.GCD import gcd
from fuzzingbook.ControlFlow import PyCFG, CFGNode, to_graph, gen_cfg
import inspect
from graphviz import Source, Graph


MAX_TRIES=10
MAX_ITER=10
MAX_DEPTH=10

#Fuzzer for GCD.py example , the example involves a loop and hence we need Advanced Syymbolic fuzzer
print(" Fuzzer output for GCD example")


adv_fuzzer_gcd = AdvancedSymbolicFuzzer(gcd,max_tries=10,
   max_iter=10,
   max_depth=10)

all_paths = adv_fuzzer_gcd.get_all_paths(adv_fuzzer_gcd.fnenter)


for i in range(len(all_paths)):
    
    print("Path No:", i)
    print("Constraint found is:", adv_fuzzer_gcd.extract_constraints(all_paths[i].get_path_to_root()))
    print("Z3 solver solution for the above constraint is:", adv_fuzzer_gcd.solve_path_constraint(all_paths[i].get_path_to_root()))


print("**********************************-------------------------------**************************************************8")