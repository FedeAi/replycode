import pandas as pd

fn = "a_solar.txt"
f = open(fn, "r")

# Line 1
l1 = f.readline()
print(l1)

W = int(l1.split()[0])
H = int(l1.split()[1])

map_conv = {'#': 0, '_': 1, 'M': 2}


def read_map(f):
    map_int = []
    map_c = []
    for x in range(H):
        line = f.readline()
        int_line = [map_conv[i] for i in list(line)[:-1]]
        char_line = list(line)[:-1]
        map_int.append(int_line)
        map_c.append(char_line)
    return map_int, map_c


map_int, map_c = read_map(f)

D = int(f.readline().split()[0])


class Developer:
    def __init__(self, compagnia="", bonus=0, n_skills=0, skills=[]):
        self.compagnia = compagnia
        self.bonus = bonus
        self.n_skills = n_skills
        self.skills = skills


developers = []
for n in range(D):
    l = f.readline()
    l_split = l.split()
    print(l_split)
    developer = Developer()
    developer.compagnia = l_split[0]
    developer.bonus = int(l_split[1])
    developer.n_skills = int(l_split[2])
    developer.skills = l_split[3:]
    developers.append(developer)


class ProjecManager:
    def __init__(self, compagnia="", bonus=0):
        self.compagnia = compagnia
        self.bonus = bonus


M = int(f.readline().split()[0])

pms = []
for n in range(M):
    l = f.readline()
    l_split = l.split()
    print(l_split)
    pm = ProjecManager()
    pm.compagnia = l_split[0]
    pm.bonus = int(l_split[1])
    pms.append(pm)

compagnia = [pm.compagnia for pm in pms]
bonus = [pm.bonus for pm in pms]
d = {'compagnia': compagnia, 'bonus': bonus}
pms_pandas = pd.DataFrame(d)

compagnia = [dev.compagnia for dev in developers]
bonus = [dev.bonus for dev in developers]
n_skills = [dev.n_skills for dev in developers]
skills = [dev.skills for dev in developers]
d = {'compagnia': compagnia, 'bonus': bonus, 'n_skills': n_skills, 'skills': skills}
dev_pandas = pd.DataFrame(d)

dev_pandas_sorted = dev_pandas.sort_values('compagnia', ascending=False)
pms_pandas_sorted = pms_pandas.sort_values('compagnia', ascending=False)


def points_dev_dev(developer1=Developer(), developer2=Developer()):
    common_skills = 0
    for i in range(developer1.n_skills):
        for j in range(i, developer2.n_skills):
            if developer1.skills[i] == developer2.skills[j]:
                common_skills = common_skills + 1
    diff_skills = developer1.n_skills + developer2.n_skills - (common_skills * 2)
    if developer1.compagnia == developer2.compagnia:
        bonus_potential = developer1.bonus * developer2.bonus
    else:
        bonus_potential = 0
    working_potential = common_skills * diff_skills
    points = bonus_potential + working_potential
    return points


def points_pm(developer1, developer2):
    if developer1.compagnia == developer2.compagnia:
        bonus_potential = developer1.bonus * developer2.bonus
    else:
        bonus_potential = 0
    return bonus_potential


def points_dev_dev_pandas(developer1, developer2):
    common_skills = 0
    for i in range(developer1['n_skills']):
        for j in range(i, developer2['n_skills']):
            if developer1['skills'][i] == developer2['skills'][j]:
                common_skills = common_skills + 1
    diff_skills = developer1['n_skills'] + developer2['n_skills'] - (common_skills * 2)
    if developer1['compagnia'] == developer2['compagnia']:
        bonus_potential = developer1['bonus'] * developer2['bonus']
    else:
        bonus_potential = 0
    working_potential = common_skills * diff_skills
    points = bonus_potential + working_potential
    return points


def points_pm_pandas(developer1, developer2):
    if developer1['compagnia'] == developer2['compagnia']:
        bonus_potential = developer1['bonus'] * developer2['bonus']
    else:
        bonus_potential = 0
    return bonus_potential


print(points_dev_dev_pandas(dev_pandas_sorted.iloc[0], dev_pandas_sorted.iloc[1]))


def sortSecond(val):
    return val[2]


couple_points = []


def find_couples():
    for i in range(len(dev_pandas_sorted)):
        for j in range(i, len(dev_pandas_sorted)):
            points = points_dev_dev_pandas(dev_pandas_sorted.iloc[i], dev_pandas_sorted.iloc[j])
            couple_points.append([dev_pandas_sorted.index[i], dev_pandas_sorted.index[j], points, 0])
    couple_points.sort(key=sortSecond)

find_couples() # Call the function

def find_n_best_matches(n, couple_points, dev_pandas_sorted):
    idx = array[0][0]
    matches = find_matches(idx,couple_points)
    n = n if len(matches) >= n else len(matches)
    for match in matches[:n]:
        couple_points.pop(match[1])
        developers.drop(match[0][1], inplace=True)
    return n, [array[0],matches[:n][0]], couple_points

def find_matches(elemid, array):
    ids =[]
    matches = [(elem,n) for n,elem in enumerate(array) if elem[1]==elemid]
    #matches = sorted(matches, key=lambda x: x[2])
    return matches
