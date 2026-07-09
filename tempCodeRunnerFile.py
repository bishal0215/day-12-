list_comp = [ x * x for x in range (5)]
print(list_comp)

gen_exp = ( x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))