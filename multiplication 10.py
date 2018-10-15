def greater(a,b):
	assert a<b, "a is greater than b"

try:
	greater(22,2)
except AssertionError as e:
	print(e)
