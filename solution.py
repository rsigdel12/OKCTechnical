# non-corner 3's y > 7.8, 23.75 ft away from basket
# corner 3's y <= 7.8, 22 ft away from basket
from cmath import sqrt
import csv

# team A variables
totalC3A = 0
C3AMakes = 0
TeamAShots = 0
totalNC3A = 0
NC3AMakes = 0
total2ptA = 0
made2ptA = 0


# team B variables
totalC3B = 0
C3BMakes = 0
TeamBShots = 0
totalNC3B = 0
NC3BMakes = 0
total2ptB = 0
made2ptB = 0

with open("shots_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for column in csv_reader:
        team = column[0]
        Xcord = column[1]
        Ycord = column[2]
        madeShot = column[3]

        if team == "Team A":
            TeamAShots = TeamAShots + 1

            distanceA = sqrt(pow(float(Xcord), 2) + pow(float(Ycord), 2))
            distanceA = distanceA.real
            # Corner 3's
            if distanceA > 22 and abs(float(Ycord)) <= 7.8:
                totalC3A = totalC3A + 1
                if madeShot == "1":
                    C3AMakes = C3AMakes + 1
            # Non-corner 3's
            elif distanceA > 23.75 and abs(float(Ycord)) > 7.8:
                totalNC3A = totalNC3A + 1
                if madeShot == "1":
                    NC3AMakes = NC3AMakes + 1
            # 2pt
            else:
                total2ptA = total2ptA + 1
                if madeShot == "1":
                    made2ptA = made2ptA + 1
        if team == "Team B":
            TeamBShots = TeamBShots + 1

            distanceB = sqrt(pow(float(Xcord), 2) + pow(float(Ycord), 2))
            distanceB = distanceB.real
            # Corner 3's
            if distanceB > 22 and abs(float(Ycord)) <= 7.8:
                totalC3B = totalC3B + 1
                if madeShot == "1":
                    C3BMakes = C3BMakes + 1
            # Non-corner 3's
            elif distanceB > 23.75 and abs(float(Ycord)) > 7.8:
                totalNC3B = totalNC3B + 1
                if madeShot == "1":
                    NC3BMakes = NC3BMakes + 1
            # 2pt
            else:
                total2ptB = total2ptB + 1
                if madeShot == "1":
                    made2ptB = made2ptB + 1

TotalMadeShotsA = made2ptA + NC3AMakes + C3AMakes
TotalMadeShotsB = made2ptB + NC3BMakes + C3BMakes

print("Team A shot " + str(float(total2ptA)/TeamAShots) + " of their shots from 2pt. They shot " +
      str(float(totalC3A)/TeamAShots) + " from corner 3's, and " + str(float(totalNC3A)/TeamAShots) + " from non-corner 3's")
print("Their eFG from 2pt was " + str(float(made2ptA + (.5 * 0))/total2ptA))
print("Their eFG from Non-corner 3's was " +
      str(float(NC3AMakes + (.5 * NC3AMakes))/totalNC3A))
print("Their eFG from corner 3's was " +
      str(float(C3AMakes + (.5 * C3AMakes))/totalC3A))
print(' ')
print(' ')
print("Team B shot " + str(float(total2ptB)/TeamBShots) + " of their shots from 2pt. They shot " +
      str(float(totalC3B)/TeamBShots) + " from corner 3's, and " + str(float(totalNC3B)/TeamBShots) + " from non-corner 3's")
print("Their eFG from 2pt was " + str(float(made2ptB + (.5 * 0))/total2ptB))
print("Their eFG from Non-corner 3's was " +
      str(float(NC3BMakes + (.5 * NC3BMakes))/totalNC3B))
print("Their eFG from corner 3's was " +
      str(float(C3BMakes + (.5 * C3BMakes))/totalC3B))
