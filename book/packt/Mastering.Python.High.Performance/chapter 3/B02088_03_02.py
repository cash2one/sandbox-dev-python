import cProfile
import pstats
import sys

from  B02088_02_16 import build_twit_stats

profiler = cProfile.Profile()
profiler.enable()


build_twit_stats()
profiler.create_stats()
stats = pstats.Stats(profiler)
stats.strip_dirs().sort_stats('cumulative').dump_stats('tweet-stats.prof') #saves the stats into a file called tweet-stats.prof, instead of printing them into stdout