
import matplotlib.pyplot as plt
from random import uniform
import math as math
from Classes import *

# util

def exponential(lam):
    u = uniform(0,1)
    logaritm = math.log(u)
    exponential = -(1/lam) * logaritm

    return exponential

# generar las poblaciones

# men_a = 5000
# women_a = 5000
men_a = int(input("cantidad de hombres:  ")) 
women_a = int(input("cantidad de mujeres:  ")) 

people = []
grievers = []
couples = []


women = []    
for _ in range(women_a):
    age = int(uniform(0,100))
    w = Person(age,"woman")
    women.append(w)

men = []    
for _ in range(men_a):
    age = int(uniform(0,100))
    m = Person(age,"man")
    men.append(m)

people = women + men

# sacar los niños deseados, estan cambiadas algunas probabilidades para equilibrar
def child_wished(people):
    for p in people:
        if not p.child_wished:
            u = uniform(0,1)
            if u < 0.05:
                p.child_wished = int(uniform(5,20))
            elif u <= 0.10:
                p.child_wished = 5 
            elif u <= 0.25:
                p.child_wished = 4
            elif u <= 0.40:
                p.child_wished = 3
            elif u <= 0.75:
                p.child_wished = 2
            else:
                p.child_wished = 1
 
child_wished(people)          

# funciones de conteo

# los solteros

def get_bachelors():

    loners = []
    for p in people:
        if (p.couple == None) & (not p.grief) :
            loners.append(p)
    # print("loners:  ",len(loners))
    avg = 0
    for p in people:
        avg += p.age
    # print("average age:  ",int(avg/len(people)))

    men_bachelors = []
    women_bachelors = []
    bachelors = []

    for lon in loners:
        if (lon.age >= 12)&(lon.age < 15):
            u = uniform(0,1)
            if u <= 0.6:
                bachelors.append(lon)
        if (lon.age >= 15)&(lon.age < 21):
            u = uniform(0,1)
            if u <= 0.65:
                bachelors.append(lon)
        if (lon.age >= 21)&(lon.age < 35):
            u = uniform(0,1)
            if u <= 0.8:
                bachelors.append(lon)
        if (lon.age >= 35)&(lon.age < 45):
            u = uniform(0,1)
            if u <= 0.6:
                bachelors.append(lon)
        if (lon.age >= 45)&(lon.age < 60):
            u = uniform(0,1)
            if u <= 0.5:
                bachelors.append(lon)
        if (lon.age >= 60)&(lon.age < 120):
            u = uniform(0,1)
            if u <= 0.2:
                bachelors.append(lon)

    for b in bachelors:
        if b.sex == "man":
            men_bachelors.append(b)
        else:
            women_bachelors.append(b)

    # print ("men_bach:  ", len(men_bachelors), "women_bach:  ", len(women_bachelors))

    form_couples(men_bachelors,women_bachelors)
    
# las parejas

def form_couples(men_bachelors, women_bachelors):
    for man in men_bachelors:
        for woman in women_bachelors:
            age_jump = abs(man.age - woman.age)
            if (age_jump >= 0)&(age_jump < 5):
                u = uniform(0,1)
                if u <= 0.45:
                    women_bachelors.remove(woman)
                    c = Couple(man,woman)
                    couples.append(c)
                    break
            if (age_jump >= 5)&(age_jump < 10):
                u = uniform(0,1)
                if u <= 0.4:
                    women_bachelors.remove(woman)
                    c = Couple(man,woman)
                    couples.append(c)
                    break
            if (age_jump >= 10)&(age_jump < 15):
                u = uniform(0,1)
                if u <= 0.35:
                    women_bachelors.remove(woman)
                    c = Couple(man,woman)
                    couples.append(c)
                    break
            if (age_jump >= 15)&(age_jump < 20):
                u = uniform(0,1)
                if u <= 0.25:
                    women_bachelors.remove(woman)
                    c = Couple(man,woman)
                    couples.append(c)
                    break
            if (age_jump >= 20):
                u = uniform(0,1)
                if u <= 0.15:
                    women_bachelors.remove(woman)
                    c = Couple(man,woman)
                    couples.append(c)
                    break
        if not len(women_bachelors):
            break

    # print("couples:  ", len(couples))
    
    get_breakups()

# las rupturas, y el tiempo de duelo

def get_breakups():
    for couple in couples:
        u = uniform(0,1)
        if u <= 0.2:
            couples.remove(couple)
            couple.breakup()
            grievers.append(couple.woman)
            grievers.append(couple.man)

    # print("couples after breakups: ", len(couples))
    # print("grievers:  ", len(grievers))
    set_grief_time()
    posible_parents()

def set_grief_time():
    for griever in grievers:
        if (griever.age >= 12)&(griever.age < 15):
            # 3 meses es 1/4 de año.. x tanto lambda es 4
            griever.alone_time = int(exponential(4))

        if (griever.age >= 15)&(griever.age < 21):
            griever.alone_time = int(exponential(2))

        if (griever.age >= 21)&(griever.age < 35):
            griever.alone_time = int(exponential(2))

        if (griever.age >= 35)&(griever.age < 45):
            griever.alone_time = int(exponential(1))

        if (griever.age >= 45)&(griever.age < 60):
            griever.alone_time = int(exponential(0.5))

        if (griever.age >= 60)&(griever.age < 125):
            griever.alone_time = int(exponential(0.25))

# los posibles padres

def posible_parents():
    posible_parents = []
    for couple in couples:
        man_children = couple.man.children
        woman_children = couple.woman.children
        if (couple.man.child_wished >= man_children)&(couple.woman.child_wished >= woman_children):
            posible_parents.append(couple)
    
    # print("pos_par:  ", len(posible_parents))  
    get_pregnanted(posible_parents)

# las parejas embarazadas

def get_pregnanted(posible_parents):
    pregnant = []

    for couple in posible_parents:
        if (couple.woman.age >= 12)&(couple.woman.age < 15):
            u = uniform(0,1)
            if u <= 0.2:
                pregnant.append(couple)
        if (couple.woman.age >= 15)&(couple.woman.age < 21):
            u = uniform(0,1)
            if u <= 0.45:
                pregnant.append(couple)
        if (couple.woman.age >= 21)&(couple.woman.age < 35):
            u = uniform(0,1) 
            if u <= 0.8:
                pregnant.append(couple)
        if (couple.woman.age >= 35)&(couple.woman.age < 45):
            u = uniform(0,1)
            if u <= 0.4:
                pregnant.append(couple)
        if (couple.woman.age >= 45)&(couple.woman.age < 60):
            u = uniform(0,1)
            if u <= 0.2:
                pregnant.append(couple)
        if (couple.woman.age >= 60)&(couple.woman.age < 120):
            u = uniform(0,1)
            if u <= 0.05:
                pregnant.append(couple)

    # print("pregnant:  ", len(pregnant))
    children_per_pregnancy(pregnant)

# niños por embarazo(multiples)

def children_per_pregnancy(pregnant):
    new_born = 0
    for p in pregnant:
        u = uniform(0,1)
        if u < 0.02:
            new_born += 5
            p.woman.children = 5
            p.man.children = 5
        elif u <= 0.06:
            new_born += 4
            p.woman.children = 4
            p.man.children = 4
        elif u <= 0.14:
            new_born += 3
            p.woman.children = 3
            p.man.children = 3
        elif u <= 0.31:
            new_born += 2
            p.woman.children = 2
            p.man.children = 2
        else: 
            new_born += 1
            p.woman.children = 1
            p.man.children = 1

    # print("new born: ",new_born)
    add_birth(new_born)

# niños nacidos

def add_birth(new_born):
    for _ in range(new_born):
        u = uniform(0,1)
        if u > 0.5:
            p = Person(0,"man")
            men.append(p)
        else:
            p = Person(0,"woman")
            women.append(p)
        people.append(p) 
    update_people()

# actualizar la poblacion(edades, gente en duelo, etc)

def update_people():
    for p in people:
        p.age += 1
    for griever in grievers:
        if not griever.alone_time:
            griever.grief = False
            grievers.remove(griever)
        else:
            griever.alone_time -= 1
    dead(women,men)

# los muertos

def dead(women,men):
    dead = []
    for woman in women:
        if (woman.age >= 0)&(woman.age < 12):
            u = uniform(0,1)
            if u <= 0.25:
                people.remove(woman)
                women.remove(woman)
                dead.append(woman)
        if (woman.age >= 12)&(woman.age < 45):
            u = uniform(0,1)
            if u <= 0.15:
                people.remove(woman)
                women.remove(woman)
                dead.append(woman)
        if (woman.age >= 45)&(woman.age < 76):
            u = uniform(0,1)
            if u <= 0.35:
                people.remove(woman)
                women.remove(woman)
                dead.append(woman)
        if (woman.age >= 76)&(woman.age < 120):
            u = uniform(0,1)
            if u <= 0.65:
                people.remove(woman)
                women.remove(woman)
                dead.append(woman)
    for man in men:
        if (man.age >= 0)&(man.age < 12):
            u = uniform(0,1)
            if u <= 0.25:
                people.remove(man)
                men.remove(man)
                dead.append(man)
        if (man.age >= 12)&(man.age < 45):
            u = uniform(0,1)
            if u <= 0.1:
                people.remove(man)
                men.remove(man)
                dead.append(man)
        if (man.age >= 45)&(man.age < 76):
            u = uniform(0,1)
            if u <= 0.3:
                people.remove(man)
                men.remove(man)
                dead.append(man)
        if (man.age >= 76)&(man.age < 120):
            u = uniform(0,1)
            if u <= 0.7:
                people.remove(man)
                men.remove(man)
                dead.append(man)

    for d in dead:
        if d.grief:
            grievers.remove(d)

        if not(d.couple == None):
            d.couple.couple = None
            d.couple.grief = True
            grievers.append(d.couple)
    for cp in couples:
        if (cp.woman.couple == None)|(cp.man.couple == None):
            couples.remove(cp)

    # print("dead:  ",len(dead))

list_w, list_y, list_m = [],[],[]
for y in range(100):
    list_w.append(len(women))
    list_m.append(len(men))
    # print("people: ",len(people))
    get_bachelors()
    # print("people after {} years: ".format(y+1),len(people), "  women :  ",len(women)," men:  ", len(men))
    list_y.append(y+1)
    if not len(people):
        break

plt.plot(list_y,list_m,label= 'Men')
plt.plot(list_y,list_w, label = 'Women')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
