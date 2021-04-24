from .station import MINUTE, Station
from .lines import *

import math

# Assume an average of 5min per train for 18h each day.
TRAIN_FREQUENCY = 18 * 12


def TTCStation(name, idle_time, daily_ridership):
    idle_time = (idle_time, idle_time / math.tau)
    ridership = daily_ridership / TRAIN_FREQUENCY
    ridership = (ridership, ridership / math.tau)

    return Station(name, idle_time, ridership)


def TTCInterior(name, idle_time, daily_ridership):
    obverse = TTCStation(name, idle_time, daily_ridership)
    reverse = TTCStation(name, idle_time, daily_ridership)

    return [obverse, reverse]


def TTCTerminus(name, idle_time, daily_ridership):
    return [TTCStation(name, idle_time, daily_ridership)]


# Average daily ridership in 2018 from
# http://www.ttc.ca/PDF/Transit_Planning/Subway%20ridership%20-%202018.pdf

# Line 1: Yonge-University-Spadina
BloorYonge1 = TTCInterior("Bloor-Yonge (1)", 31, 204630)
College = TTCInterior("College", 16, 44370)
Davisville = TTCInterior("Davisville", 14, 25990)
DownsviewPark = TTCInterior("Downsview Park", 12, 2520)
Dundas = TTCInterior("Dundas", 14, 73560)
Dupont = TTCInterior("Dupont", 14, 8500)
Eglinton = TTCInterior("Eglinton", 17, 68520)
EglintonWest = TTCInterior("Eglinton West", 15, 21430)
Finch = TTCTerminus("Finch", 6 * MINUTE + 27, 99350)
FinchWest = TTCInterior("Finch West", 18, 17660)
Glencairn = TTCInterior("Glencairn", 12, 6940)
Highway407 = TTCInterior("Highway 407", 13, 3340)
King = TTCInterior("King", 13, 64730)
Lawrence = TTCInterior("Lawrence", 14, 22340)
LawrenceWest = TTCInterior("Lawrence West", 13, 22340)
Museum = TTCInterior("Museum", 13, 11840)
NYCentre = TTCInterior("North York Centre", 14, 25380)
Osgoode = TTCInterior("Osgoode", 14, 23670)
PioneerVillage = TTCInterior("Pioneer Village", 14, 17320)
Queen = TTCInterior("Queen", 14, 48700)
QueensPark = TTCInterior("Queen's Park", 17, 46470)
Rosedale = TTCInterior("Rosedale", 15, 7770)
SheppardWest = TTCInterior("Sheppard West", 20, 41600)
SheppardYonge1 = TTCInterior("Sheppard-Yonge (1)", 23, 79720)
Spadina1 = TTCInterior("Spadina (1)", 14, 12620)
StAndrew = TTCInterior("St. Andrew", 15, 57480)
StClair = TTCInterior("St. Clair", 14, 36620)
StClairWest = TTCInterior("St. Clair West", 13, 27980)
StGeorge1 = TTCInterior("St. George (1)", 20, 130850)
StPatrick = TTCInterior("St. Patrick", 15, 34060)
Summerhill = TTCInterior("Summerhill", 14, 5710)
Union = TTCInterior("Union", 23, 143740)
Yorkdale = TTCInterior("Yorkdale", 15, 22860)
YorkMills = TTCInterior("York Mills", 16, 29660)
YorkUniversity = TTCInterior("York University", 17, 43130)
Vaughan = TTCTerminus("Vaughan Metropolitan Centre", 7 * MINUTE + 13, 14790)
Wellesley = TTCInterior("Wellesley", 14, 23510)
Wilson = TTCInterior("Wilson", 19, 29260)

# Line 2: Bloor-Danforth
Bathurst = TTCInterior("Bathurst", 16, 26800)
Bay = TTCInterior("Bay", 14, 32690)
BloorYonge2 = TTCInterior("Bloor-Yonge (2)", 28, 196460)
Broadview = TTCInterior("Broadview", 17, 32670)
CastleFrank = TTCInterior("Castle Frank", 13, 9760)
Chester = TTCInterior("Chester", 14, 5800)
Christie = TTCInterior("Christie", 15, 12510)
Coxwell = TTCInterior("Coxwell", 14, 15480)
Donlands = TTCInterior("Donlands", 14, 11250)
Dufferin = TTCInterior("Dufferin", 18, 28620)
DundasWest = TTCInterior("Dundas West", 15, 27540)
Greenwood = TTCInterior("Greenwood", 14, 11080)
HighPark = TTCInterior("High Park", 14, 12080)
Islington = TTCInterior("Islington", 18, 41270)
Jane = TTCInterior("Jane", 14, 20110)
Keele = TTCInterior("Keele", 14, 16990)
Kennedy2 = TTCTerminus("Kennedy (2)", 5 * MINUTE + 41, 80070)
Kipling = TTCTerminus("Kipling", 5 * MINUTE + 18, 49340)
Lansdowne = TTCInterior("Lansdowne", 13, 19000)
MainStreet = TTCInterior("Main Street", 15, 23950)
OldMill = TTCInterior("Old Mill", 13, 8850)
Ossington = TTCInterior("Ossington", 15, 30100)
Pape = TTCInterior("Pape", 17, 27080)
RoyalYork = TTCInterior("Royal York", 15, 22800)
Runnymede = TTCInterior("Runnymede", 14, 20110)
Sherbourne = TTCInterior("Sherbourne", 16, 31030)
Spadina2 = TTCInterior("Spadina (2)", 17, 31940)
StGeorge2 = TTCInterior("St. George (2)", 24, 125180)
VictoriaPark = TTCInterior("Victoria Park", 15, 30780)
Warden = TTCInterior("Warden", 17, 39980)
Woodbine = TTCInterior("Woodbine", 15, 14960)

# Line 3: Scarborough
Ellesmere = TTCInterior("Ellesmere", 13, 1770)
Kennedy3 = TTCTerminus("Kennedy (3)", 25, 31120)
LawrenceEast = TTCInterior("Lawrence East", 14, 7930)
McCowan = TTCTerminus("McCowan", 3 * MINUTE, 3860)
Midland = TTCInterior("Midland", 13, 2440)
ScarboroughCentre = TTCInterior("Scarborough Centre", 14, 23050)

# Line 4: Sheppard
Bayview = TTCInterior("Bayview", 14, 8530)
Bessarion = TTCInterior("Bessarion", 14, 2990)
DonMills = TTCTerminus("Don Mills", 5 * MINUTE + 14, 37050)
Leslie = TTCInterior("Leslie", 14, 5990)
SheppardYonge4 = TTCTerminus("Sheppard-Yonge (4)", 4 * MINUTE + 49, 45750)

# Station ordering.
Line1 = [
    Vaughan, Highway407, PioneerVillage, YorkUniversity, FinchWest,
    DownsviewPark, SheppardWest, Wilson, Yorkdale, LawrenceWest, Glencairn,
    EglintonWest, StClairWest, Dupont, Spadina1, StGeorge1, Museum, QueensPark,
    StPatrick, Osgoode, StAndrew, Union, King, Queen, Dundas, College,
    Wellesley, BloorYonge1, Rosedale, Summerhill, StClair, Davisville, Eglinton,
    Lawrence, YorkMills, SheppardYonge1, NYCentre, Finch
]
Line2 = [
    Kipling, Islington, RoyalYork, OldMill, Jane, Runnymede, HighPark, Keele,
    DundasWest, Lansdowne, Dufferin, Ossington, Christie, Bathurst, Spadina2,
    StGeorge2, Bay, BloorYonge2, Sherbourne, CastleFrank, Broadview, Chester,
    Pape, Donlands, Greenwood, Coxwell, Woodbine, MainStreet, VictoriaPark,
    Warden, Kennedy2
]
Line3 = [Kennedy3, LawrenceEast, Ellesmere, Midland, ScarboroughCentre, McCowan]
Line4 = [SheppardYonge4, Bayview, Bessarion, Leslie, DonMills]

NetworkWrapped = [s[0] for s in Line1 + Line2 + Line3 + Line4]

Line1 = flatten(natural_connections(Line1))
Line2 = flatten(natural_connections(Line2))
Line3 = flatten(natural_connections(Line3))
Line4 = flatten(natural_connections(Line4))

# Entire subway system network.
Network = Line1 + Line2 + Line3 + Line4
NetworkLengths = [len(Line1), len(Line2), len(Line3), len(Line4)]

TerminusIndices = [-1]
for l in NetworkLengths:
    prev = TerminusIndices[-1]
    start = prev + 1
    end = prev + l
    TerminusIndices.append(start)
    TerminusIndices.append(end)
TerminusIndices = set(TerminusIndices[1:])

# Sanity check.
if __name__ == "__main__":
    for line in [Line1, Line2, Line3, Line4]:
        for station in line:
            print(station.name)
            print("idle time: ", station.idle_time)
            print("ridership: ", station.ridership)
            for i in range(5):
                print("\t", station.generate_observation())
            print()
