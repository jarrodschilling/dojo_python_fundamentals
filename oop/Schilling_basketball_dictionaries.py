players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

class Player:
    def __init__(self, my_dict):
        self.name = my_dict['name']
        self.age = my_dict['age']
        self.position = my_dict['position']
        self.team = my_dict['team']

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            player = Player(player)
            new_team.append(player)

        return new_team


print(Player.get_team(players))


# new_team = []
# for player in players:
#     player = Player(player)
#     new_team.append(player)

# print(new_team)
# print(new_team[2].age)



# kevin = {
#     "name": "Kevin Durant", 
#     "age":34, 
#     "position": "small forward", 
#     "team": "Brooklyn Nets"
# }
# jason = {
#     "name": "Jason Tatum", 
#     "age":24, 
#     "position": "small forward", 
#     "team": "Boston Celtics"
# }
# kyrie = {
#     "name": "Kyrie Irving", 
#     "age":32, "position": "Point Guard", 
#     "team": "Brooklyn Nets"
# }
    


# player_kevin = Player(kevin)
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)
