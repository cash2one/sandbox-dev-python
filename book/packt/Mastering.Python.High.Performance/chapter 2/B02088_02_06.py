import pstats
p = pstats.Stats('stats')
p.strip_dirs().sort_stats(-1).print_stats()