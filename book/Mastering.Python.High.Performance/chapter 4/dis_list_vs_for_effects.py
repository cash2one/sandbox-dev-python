import dis
import inspect
import timeit


programs = dict(
    loop="""
total_sum = 0
def add(to, val):
	to += val
for x in range(100):
	add(total_sum, x)
""",
    comprehension="""
total_sum = 0
def add(to, val):
	to += val
[add(total_sum, x) for x in range(100) ]
    	""",
)


for name, text in programs.iteritems():
    print name, timeit.Timer(stmt=text).timeit()
    code = compile(text, '<string>', 'exec')
    dis.disassemble(code)