from baseball_team import Baseball_Team

Carp=Baseball_Team("Carp",88,51,4)
Tigers=Baseball_Team("Tigers",78,61,4)
BayStars=Baseball_Team("BayStars",73,65,5)
Giants=Baseball_Team("Giants",72,68,3)
Dragons=Baseball_Team("Dragons",59,79,5)
Swallows=Baseball_Team("Swallows",45,96,2)

print("{0:8s}".format("team"),"{0:3s}".format("win"),"{0:3s}".format("lose"),"{0:3s}".format("draw"),"{0:3s}".format("rate"))
#print("team\twin\tlose\tdraw\trate")
Carp.show_team_result()
Tigers.show_team_result()
BayStars.show_team_result()
Giants.show_team_result()
Dragons.show_team_result()
Swallows.show_team_result()