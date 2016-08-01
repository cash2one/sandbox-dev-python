import cProfile

def runRe():
    import re
    re.compile("foo|bar")

prof = cProfile.Profile() 
prof.enable() 
runRe()
prof.create_stats()
prof.print_stats()