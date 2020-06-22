from random import *

def populationGraph(recessive, dominant, mixed):
    import pylab
    numOrganisms = recessive[0] + dominant[0] + mixed[0]
    pylab.plot(range(len(recessive)), recessive, label="tt")
    pylab.plot(range(len(dominant)), dominant, label="TT")
    pylab.plot(range(len(mixed)), mixed, label="Tt and tT")
    pylab.legend(loc='upper left')
    pylab.axis([0,len(recessive),0,numOrganisms])
    pylab.xlabel('Number of Generations')
    pylab.ylabel('Number of Organisms')
    pylab.show()

def InitializePopulation(popsize, p):
    initialpop = []
    for i in range(popsize):
        alleleone = []
        for x in range(2):
            if random() < p:
                allele = 'T'
            else:
                allele = 't'
            alleleone.append(allele)
        alleleoneready = ''.join(alleleone)
        initialpop.append(alleleoneready)
#    print(initialpop)
    return(initialpop)

def countGenotypes(population):
    T = population.count('TT')
    mixT = population.count('Tt')
    mixT2 = population.count('tT')
    mixes = mixT + mixT2
    t = population.count('tt')
    total = T + mixT + mixT2 + t

    print("TT:", round(T/total, 3), "| Tt or tT:", round(mixes/total, 3), "| tt:", round(t/total,3))

def oneGeneration(population, prefmate, natselect, natselectrate):
    parentpick = []
    nextgen = []
    for m in range(len(population)):
        parentpick.append(m)
#    print(parentpick)
    allelepick = [0,1]
    for l in range(len(population)):
        p1 = population[choice(parentpick)]
        p2 = population[choice(parentpick)]
#        print(p1, p2)
        if prefmate == "no":
            alle1 = p1[choice(allelepick)]
            alle2 = p2[choice(allelepick)]
            kid = alle1 + alle2
            nextgen.append(kid)
        elif prefmate == "yes":
            if ('T' in p1 and 'T' in p2) or ('tt' in p1 and 'tt' in p2):
                alle1 = p1[choice(allelepick)]
                alle2 = p2[choice(allelepick)]
                kid = alle1 + alle2
                nextgen.append(kid)
#                print(kid, 'match')
            else:
                p3 = population[choice(parentpick)]
                alle1 = p1[choice(allelepick)]
                alle2 = p3[choice(allelepick)]
                kid = alle1 + alle2
                nextgen.append(kid)
#                print(p3, kid, 'no match')
#    print(nextgen, 'pre nat select')
    if natselect == "tall":
#        print(natselectrate)
#        print(natselectrate/100)
#        print(len(nextgen))
        killoff = (natselectrate/100) * float(len(population))
#        print(killoff)
        for i in range(int(killoff)):
            try:
                nextgen.pop(nextgen.index("TT"))
            except ValueError:
                try:
                    nextgen.pop(nextgen.index("Tt"))
                except ValueError:
                    try:
                        nextgen.pop(nextgen.index("tT"))
                    except ValueError:
                       nextgen = nextgen
    elif natselect == "short":
        killoff = (natselectrate/100) * float(len(population))
        for i in range(int(killoff)):
            try:
                nextgen.pop(nextgen.index("tt"))
            except ValueError:
                nextgen = nextgen

#    print(nextgen)
    return(nextgen)

def manyGenerations(population, numGenerations, prefmate, natselect, natselectrate, graph):
    rec = []
    dom = []
    mix = []
    for q in range(int(numGenerations)):
        population = oneGeneration(population, prefmate, natselect, natselectrate)
        aT = population.count('TT')
        amixT = population.count('Tt')
        amixT2 = population.count('tT')
        amixes = amixT + amixT2
        at = population.count('tt')
        rec.append(at)
        dom.append(aT)
        mix.append(amixes)

#    print(rec)
#    print(dom)
#    print(mix)
    if graph == 'yes':
        populationGraph(rec, dom, mix)


    return population


def main():
    popsize = int(input("Population Size?"))
    p = float(input("p?"))
    numGenerations = input("Number of Gens?")
    prefmate = input("Preferential mating? Y/N").lower().strip(".,![]()")
    natselect = input("Natural selection? against: tall, short, none").lower().strip(".,![]()")
    if natselect == 'yes':
        natselectrate = int(input("% to kill off each generation?").lower().strip(".,![]()"))
    else:
        natselectrate = 0
    graph = input("Do you want to graph your results?").lower().strip(".,!?/")
    population = InitializePopulation(popsize, p)
    countGenotypes(population)
    countGenotypes(manyGenerations(population, numGenerations, prefmate, natselect, natselectrate, graph))



main()
