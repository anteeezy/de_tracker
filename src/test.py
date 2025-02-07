from data_objects import Day, Days, Player
import datetime

day1 = Day(datetime.date(2008, 6, 24), 1,0,0, 5000)
day2 = Day(datetime.date(2008, 6, 25), 1,0,0, 5320)

days1 = Days([day1, day2])

player1 = Player('anteezy', days1)

def test_player():
    assert player1.name == 'anteezy'
    assert player1.played_days.days == [Day(datetime.date(2008, 6, 24), 1,0,0, 5000), Day(datetime.date(2008, 6, 25), 1,0,0, 5320)]
    assert player1.played_days.days[0].mmr == 5000
