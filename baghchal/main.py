from hungrytigeragent import HungryTigerAgent
from game import Game
import random
from matchup import Matchup
from hungrytigeragent import HungryTigerAgent
from stats import Stats
from sidehugginggoat import SideHuggingGoat

matchup = Matchup()
# matchup.tigerAgent = HungryTigerAgent(matchup.game)
matchup.goatAgent = sideHuggingGoat(matchup.game)
stats = Stats(matchup, 1000)
stats.playAll()
stats.summarize()
