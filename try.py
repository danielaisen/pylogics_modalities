from pylogics.parsers import parse_pltl

formula = "Y a"

f = parse_pltl(formula)
print(f)

formula = "Z a"

f = parse_pltl(formula)
print(f)