from itertools import permutations

##################################
#
# Edit this to load a different file
#
path_to_file = 'pubs.txt'
#
##################################

def load_distances_from_file(path):
    dic = {}
    with open(path) as f:
        for line in f:
            a, b, d = line.split()
            dic[(a,b)] = int(d)
    return dic

def tbp(pubs,paths):
    best_dist = 9999999999 #yes really
    best_perm = None
    for perm in permutations(pubs):
        s = 0 
        for i in range(len(perm)-1):
            a = perm[i]
            b = perm[i+1]
            val = paths.get((a,b))
            if val == None:
                val = paths[(b,a)]
            s += val
        if s < best_dist:
            best_dist = s
            best_perm = perm
    return best_perm,best_dist

def present(perm,dist):
    print("The first shortest choice is:")
    for pub in perm:
        print(pub)
    print('For a total distance of {} units'.format(dist))
    
if __name__ == '__main__':
    inp = input('give me 5 pubs seperated with spaces: ')
    pubs = inp.split()

    if len(pubs) == 5:
        paths = load_distances_from_file(path_to_file)
        perm,dist = tbp(pubs,paths)
        present(perm,dist)
    else:
        print('That is not five pubs.')
