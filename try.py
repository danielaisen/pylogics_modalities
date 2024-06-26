from pylogics.parsers import parse_pltl

formula = "Z a"

f = parse_pltl(formula)
print(f)