from fuzzingbook.SymbolicFuzzer import  AdvancedSymbolicFuzzer
from examples.GCD import gcd
from examples.absolute_value import abs_value
from fuzzingbook.ControlFlow import PyCFG, CFGNode, to_graph, gen_cfg
import inspect
from graphviz import Source, Graph
from examples.pass_fail import pass_fail


MAX_TRIES=10 # maximum number of iterations
MAX_ITER=10  # maximum number of tries to get a output
MAX_DEPTH=10   # maximum depth the tool (program) should go in to trace the execution

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


print("**********************************-------------------------------**************************************************")



print(" Fuzzer output for pass_fail value example")


adv_fuzzer_pass = AdvancedSymbolicFuzzer(pass_fail,max_tries=10,
   max_iter=10,
   max_depth=10)

all_paths = adv_fuzzer_pass.get_all_paths(adv_fuzzer_pass.fnenter)


for i in range(len(all_paths)):
    
    print("Path No:", i)
    print("Constraint found is:", adv_fuzzer_pass.extract_constraints(all_paths[i].get_path_to_root()))
    print("Z3 solver solution for the above constraint is:", adv_fuzzer_pass.solve_path_constraint(all_paths[i].get_path_to_root()))

print("**********************************-------------------------------**************************************************")