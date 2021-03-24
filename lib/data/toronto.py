from station import *

# Assume an average of 5min per train for 18h each day.
TRAIN_FREQUENCY = 18 * 12


def TTCStation(name,
               idle_time,
               daily_ridership,
               platforms=2,
               rails=2,
               natural_light=False):
    # TODO: define or generate legitimate variances
    if type(idle_time) == int:
        idle_time = (idle_time, 1.5)
    if type(daily_ridership) == int:
        daily_ridership = (daily_ridership, daily_ridership / 5)
    ridership = (daily_ridership[0] / TRAIN_FREQUENCY,
                 daily_ridership[1] / TRAIN_FREQUENCY)

    return Station(name, idle_time, ridership, platforms, rails, natural_light)


# Average daily ridership in 2018 from
# http://www.ttc.ca/PDF/Transit_Planning/Subway%20ridership%20-%202018.pdf

# Line 1: Yonge-University-Spadina
BloorYonge1 = Station("Bloor-Yonge", 31, 204630)
College = TTCStation("College", 16, 44370)
Davisville = TTCStation("Davisville", 14, 25990, 3, 3, True)
DownsviewPark = TTCStation("Downsview Park", 12, 2520, 1, natural_light=True)
Dundas = TTCStation("Dundas", 14, 73560)
Dupont = TTCStation("Dupont", 14, 8500)
Eglinton = TTCStation("Eglinton", 17, 68520, 1)
EglintonWest = TTCStation("Eglinton West", 15, 21430, natural_light=True)
Finch = TTCStation("Finch", 6 * MINUTE + 27, 99350, 1)
FinchWest = TTCStation("Finch West", 18, 17660, 1)
Glencairn = TTCStation("Glencairn", 12, 6940, 1, natural_light=True)
Highway407 = TTCStation("Highway 407", 13, 3340, 1, natural_light=True)
King = TTCStation("King", 13, 64730)
Lawrence = TTCStation("Lawrence", 14, 22340, 1)
LawrenceWest = TTCStation("Lawrence West", 13, 22340, 1, natural_light=True)
Museum = TTCStation("Museum", 13, 11840, 1)
NYCentre = TTCStation("North York Centre", 14, 25380)
Osgoode = TTCStation("Osgoode", 14, 23670, 1)
PioneerVillage = TTCStation("Pioneer Village", 14, 17320)
Queen = TTCStation("Queen", 14, 48700)
QueensPark = TTCStation("Queen's Park", 17, 46470, 1)
Rosedale = TTCStation("Rosedale", 15, 7770, natural_light=True)
SheppardWest = TTCStation("Sheppard West", 20, 41600, 1, natural_light=True)
SheppardYonge1 = TTCStation("Sheppard-Yonge", 23, 79720, 1)
Spadina1 = TTCStation("Spadina", 14, 12620)
StAndrew = TTCStation("St. Andrew", 15, 57480, 1)
StClair = TTCStation("St. Clair", 14, 36620)
StClairWest = TTCStation("St. Clair West", 13, 27980)
StGeorge1 = TTCStation("St. George", 20, 130850, 1)
StPatrick = TTCStation("St. Patrick", 15, 34060, 1)
Summerhill = TTCStation("Summerhill", 14, 5710)
Union = TTCStation("Union", 23, 143740)
Yorkdale = TTCStation("Yorkdale", 15, 22860, 1, natural_light=True)
YorkMills = TTCStation("York Mills", 16, 29660, 1)
YorkUniversity = TTCStation("York University", 17, 43130, 1, natural_light=True)
Vaughan = TTCStation("Vaughan Metropolitan Centre", 7 * MINUTE + 13, 14790, 1)
Wellesley = TTCStation("Wellesley", 14, 23510)
Wilson = TTCStation("Wilson", 19, 29260, 1, natural_light=True)

# Line 2: Bloor-Danforth
Bathurst = TTCStation("Bathurst", 16, 26800)
Bay = TTCStation("Bay", 14, 32690)
BloorYonge2 = TTCStation("Bloor-Yonge", 28, 196460)
Broadview = TTCStation("Broadview", 17, 32670)
CastleFrank = TTCStation("Castle Frank", 13, 9760)
Chester = TTCStation("Chester", 14, 5800)
Christie = TTCStation("Christie", 15, 12510)
Coxwell = TTCStation("Coxwell", 14, 15480)
Donlands = TTCStation("Donlands", 14, 11250)
Dufferin = TTCStation("Dufferin", 18, 28620)
DundasWest = TTCStation("Dundas West", 15, 27540)
Greenwood = TTCStation("Greenwood", 14, 11080)
HighPark = TTCStation("High Park", 14, 12080, natural_light=True)
Islington = TTCStation("Islington", 18, 41270, 1)
Jane = TTCStation("Jane", 14, 20110)
Keele = TTCStation("Keele", 14, 16990, natural_light=True)
Kennedy2 = TTCStation("Kennedy", 5 * MINUTE + 41, 80070)
Kipling = TTCStation("Kipling", 5 * MINUTE + 18, 49340, 1, natural_light=True)
Lansdowne = TTCStation("Lansdowne", 13, 19000)
MainStreet = TTCStation("Main Street", 15, 23950)
OldMill = TTCStation("Old Mill", 13, 8850, natural_light=True)
Ossington = TTCStation("Ossington", 15, 30100)
Pape = TTCStation("Pape", 17, 27080)
RoyalYork = TTCStation("Royal York", 15, 22800)
Runnymede = TTCStation("Runnymede", 14, 20110)
Sherbourne = TTCStation("Sherbourne", 16, 31030)
Spadina2 = TTCStation("Spadina", 17, 31940)
StGeorge2 = TTCStation("St. George", 24, 125180, 1)
VictoriaPark = TTCStation("Victoria Park", 15, 30780, natural_light=True)
Warden = TTCStation("Warden", 17, 39980, 1, natural_light=True)
Woodbine = TTCStation("Woodbine", 15, 14960)

# Line 3: Scarborough
Ellesmere = TTCStation("Ellesmere", 13, 1770)
Kennedy3 = TTCStation("Kennedy", 25, 31120)
LawrenceEast = TTCStation("Lawrence East", 14, 7930)
McCowan = TTCStation("McCowan", 3 * MINUTE, 3860)
Midland = TTCStation("Midland", 13, 2440)
ScarboroughCentre = TTCStation("Scarborough Centre", 14, 23050)

# Line 4: Sheppard
Bayview = TTCStation("Bayview", 14, 8530)
Bessarion = TTCStation("Bessarion", 14, 2990)
DonMills = TTCStation("Don Mills", 5 * MINUTE + 14, 37050, 1)
Leslie = TTCStation("Leslie", 14, 5990)
SheppardYonge4 = TTCStation("Sheppard-Yonge", 4 * MINUTE + 49, 45750, 3)

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

# Natural line connections.
for line in [Line1, Line2, Line3, Line4]:
    for i in range(len(line) - 1):
        line[i].connect(line[i + 1])

# Transfer connections.
BloorYonge1.connect(BloorYonge2)
Kennedy2.connect(Kennedy3)
SheppardYonge1.connect(SheppardYonge4)
Spadina1.connect(Spadina2)
StGeorge1.connect(StGeorge2)

# Sanity check.
for line in [Line1, Line2, Line3, Line4]:
    for station in line:
        print(station.name, station.ridership)
    print()
