import dis
import inspect
import timeit


programs = dict(
    loop="""
multiples_of_two = []
for x in range(100):
	if x % 2 == 0:
		multiples_of_two.append(x)
""",
    comprehension='multiples_of_two = [x for x in range(100) if x % 2 == 0]',
)


for name, text in programs.iteritems():
    print name, timeit.Timer(stmt=text).timeit()
    code = compile(text, '<string>', 'exec')
    dis.disassemble(code)