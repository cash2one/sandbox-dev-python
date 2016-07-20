import cProfile

def runRe():
    import re 
    cProfile.run('re.compile("foo|bar")')

runRe()