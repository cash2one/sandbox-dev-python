from numba import jit, float32, int8, autojit
import numpy
import operator


@jit(nopython=True)
def _get_array_multi(arr1, arr2, final):
	for x, idx1 in enumerate(arr1):
		for y, idx2 in enumerate(arr2):
			final[idx1*idx2] = x * y #.append(x ** y)
	return final

@jit(nopython=True)
def _add_array_values(final, value): 
	for x in final:
		value += x
	return value

#@jit(nopython=True)
#@autojit(float32(int8[:], int8[:]), nopython=True)
def array_multi(arr1, arr2):
	total_value = 0
	final = numpy.zeros( (len(arr1) * len(arr2)) + 1) #[0] * (len(arr1) * len(arr2))

	_get_array_multi(arr1, arr2, final)
	return _add_array_values(final, total_value )	


arr1 = numpy.arange(1000)
arr2 = numpy.arange(1000)
final = []

array_multi(arr1, arr2)