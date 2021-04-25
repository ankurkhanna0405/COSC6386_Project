from fuzzingbook.SymbolicFuzzer import  SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
from examples.pyth_triplet import PythogareanTriplets

#func = examples.pyth_triplet

symfz_ct = SimpleSymbolicFuzzer(PythogareanTriplets)
paths = symfz_ct.get_all_paths(symfz_ct.fnenter)


print(symfz_ct.extract_constraints(paths[0]))
print(symfz_ct.solve_path_constraint(paths[0]))