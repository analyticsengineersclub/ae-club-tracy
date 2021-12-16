# debugging exercise

# print
for i in range(10):
	print(i)
	x = denoms[i]
	print(x)
	result = 100 / x

# using pdb
for i in range(10):
	import pdb; pdb.set_trace()
	print(f'i: {i}')
	x = denoms[i]
	print(f'denom: {x}')
	result = 100 / x