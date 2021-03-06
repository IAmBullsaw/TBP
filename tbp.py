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
        for i,line in enumerate(f):
            # Ignore comments or empty lines.
            if '#' == line[0] or line == "" or line == "\n":
                continue
            # We need to be able to unpack at MOST 3 values
            count = 0
            for c in line:
                if c == ',':
                    count += 1
            if count == 2:
                a, b, d = line.split(',')
                dic[(a,b)] = int(d)
            else:
                print("Error: pubs.txt is not well formed.\nLine number: {}\nLine: {}".format(i, line))
                dic = {}
                break;
    return dic

def validate_data(pubs,paths):
    for pub in pubs:
        valid = False
        for k in paths.keys():
            if pub == k[0] or pub == k[1]:
                valid = True
                break
        if not valid:
            return False, pub
    return True, None
        

def tbp(pubs,paths):
    best_dist = 9999999999 #yes really
    best_perm = None
    for perm in permutations(pubs):
        perm = list(perm)
        perm.insert(0,'me')
        s = 0 
        for i in range(len(perm)-1):
            a = perm[i]
            b = perm[i+1]
            val = paths.get((a,b))
            if val == None:
                val = paths.get((b,a))
            if val == None:
                if a == b:
                    raise Exception('You are trying to visit the pub "{}" twice. I can not compute.'.format(a))
                else:   
                    raise Exception('Pub entry "{}" did not exist'.format((a,b)))
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

    done = False
    paths = load_distances_from_file(path_to_file)
    if paths != {}:
        while not done:
            inp = input('Enter some unique pubs seperated with commas (q,ls): ')
            if inp == 'q':
                done = True
            elif inp == 'ls':
                s = set()
                for k,v in paths:
                    s.add(k)
                    s.add(v)
                print("Available pubs:")
                s.remove('me')
                for p in s:
                    print('\t'+p)
            else:    
                pubs = inp.split(',')
                if len(pubs) > 1:
                    valid, who = validate_data(pubs,paths)
                    if valid:
                        try:
                            perm,dist = tbp(pubs,paths)
                            present(perm,dist)
                        except Exception as e:
                            print(e)
                    else:
                        print('Could not find pub "{}" in file.'.format(who))
                else:
                    print('That is not correct input. Please input at least two pubs.')
        print("Thank you. Have fun!")
