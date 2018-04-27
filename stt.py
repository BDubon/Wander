from nba_py import shotchart
from nba_py.player import get_player
import nba_py
import json

def test():
    pid = get_player('Kevin', 'Durant')
    assert shotchart.ShotChart(pid)
    print(pid)


test()

r = nba_py.Scoreboard(month=6, day=28, year=2017, league_id='00', offset=0)
#js = json.load(r)
print(type(r))
