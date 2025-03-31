#TRAFFIC LIGHT PROBLEM FROM 'DATA STRUCTURES AND ALGORITHMS' BY HOPCROFT, ET AL.
#We consider 3 roads, say a, b, c; ab is a path from a to b, and so on
#we have a graph with list of incompatible paths for a given path
#we have to assign a color to each new path if incompatible with previous assigned ones
#This is not a true greedy algorithm!
curr_color = 0 #color assignment
ab = bc = ca = ba = cb = ac = 0 #initializing paths
tcolor = {'ab':0, 'bc':0, 'ca':0, 'ba':0, 'cb':0, 'ac':0} #path to color assignments
tgraph = {'ab':['ba','bc','ac'], 'bc':['ab','ca','ac'],'ca':['bc','ac'], \
          'ba':['ab'],'cb':[], 'ac':['ab','bc','ca']} #incompatible path list for a path
for i in tgraph:
    print(i, ' - ', tgraph[i])
    #if not assigned a color for new path, assign new for incompatible, else same color
    if tcolor[i] == 0 and tgraph[i] != []: #has one or more incompatible path(s)
        curr_color += 1 #pick up a new color
        tcolor[i] = curr_color
    elif tcolor[i] == 0 and tgraph[i] == []: #no dependence on other paths
        tcolor[i] = curr_color
print (tcolor)
