team_a = {11, 22, 33, 44, 55, 66}
team_b = {11, 33, 55}
team_c = {1, 2, 3, 4, 9, 11, 55, 66}
team_d = {8, 9, 7}

print("A and B disjoint:", team_a.isdisjoint(team_b))
print("A and C disjoint:", team_a.isdisjoint(team_c))
print("A and D disjoint:", team_a.isdisjoint(team_d))