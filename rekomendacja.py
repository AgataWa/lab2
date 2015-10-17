users = {
    "Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5,
             "The Strokes": 2.5, "Vampire Weekend": 2.0},
    "Bonia": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
              "Vampire Weekend": 3.0},
    "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
               "Slightly Stoopid": 1.0},
    "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0, "Vampire Weekend": 2.0},
    "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
    "Fruzia": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
               "The Strokes": 4.0, "Vampire Weekend": 4.0},
    "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0,
              "The Strokes": 5.0},
    "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}


def manhattan(rating1, rating2):
    distance = 0
    compare = False
    for k in rating1.keys():
        if k in rating2.keys():
            compare = True
            distance += abs(rating1[k] - rating2[k])
    if compare:
        return distance
    else:
        return -1


def computeNearestNeighbor(username, users):
    distances = []
    for i in users.keys():
        if i != username:
            dist = manhattan(users[username], users[i])
            distances.append([dist, i])
    distances.sort()
    nameOfNearestNeighbor = distances[0][1]
    return nameOfNearestNeighbor


def recommend(username, users):
    nearest = computeNearestNeighbor(username, users)
    recommendations = []
    for k in users[nearest].keys():
        if k not in users[username].keys():
            recommendations.append([k, users[nearest][k]])
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)


def test():
    assert (manhattan(users["Ania"], users["Bonia"]) == 9.0)
    assert (manhattan(users["Dominika"], users["Ela"]) == 4.5)
    assert (computeNearestNeighbor("Dominika", users) == "Hela")
    assert (computeNearestNeighbor("Gosia", users) == "Celina")
    assert (recommend("Celina", users) == [['The Strokes', 4.0], ['Vampire Weekend', 1.0]])
    assert (recommend("Fruzia", users) == [['Blues Traveler', 3.0]])


test()


print(recommend('Hela', users))
print(recommend('Celina', users))
