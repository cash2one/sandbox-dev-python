import cProfile
import pstats

#from B02088_02_14 import build_twit_stats
from B02088_02_16 import build_twit_stats

profiler = cProfile.Profile()
profiler.enable()

build_twit_stats()

profiler.create_stats()
stats = pstats.Stats(profiler)
stats.strip_dirs().sort_stats('cumulative').print_stats()