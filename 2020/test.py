fn = "a_solar.txt"
f = open(fn, "r")

#Line 1
l1 = f.readline()
print(l1)

W = int(l1.split()[0])
H = int(l1.split()[1])

map_conv = {'#' : 0, '_':1, 'M':2}
def read_map(f):
    map_int = []
    map_c = []
    for x in range(H):
        line = f.readline()
        int_line = [map_conv[i] for i in list(line)[:-1] ] 
        char_line = list(line)[:-1]
        map_int.append(int_line)
        map_c.append(char_line)
    return map_int, map_c

map_int, map_c = read_map(f)

D = int(f.readline().split()[0]) 

class Developer:
    def __init__(self,compagnia="",bonus=0,n_skills=0, skills=[] ):
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
    def __init__(self,compagnia="",bonus=0):
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
    
