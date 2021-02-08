RULES = [
    (#1 If has spine, vertebrate. Necessary?:"is-invertebrate ?animal False"
        "has-spine-implies-vertebrate", 
        ["has-spine ?animal True"], 
        ["is-vertebrate ?animal True"]
    ),
    (#2 If has no spine, not vertebrate. (invertebrate) Necessary?:"is-invertebrate ?animal True"
        "has-no-spine-implies-invertebrate",
        ["has-spine ?animal False"],
        ["is-vertebrate ?animal False"]
    ),
    (#3 if can control body temp, warm blooded
        "can-control-body-temp-implies-warm-blooded",
        ["can-control-body-temp ?animal True"],
        ["is-warm-blooded ?animal True",
             "is-amphibian ?animal False", "is-fish ?animal False", "is-reptile ?animal False"
        ]
    ),
    (#4 if cannnot control body temp, not warm blooded (cold blooded)
        "cannot-control-body-tmp-implies-cold-blooded",
        ["can-control-body-temp ?animal False"],
        ["is-warm-blooded ?animal False"
            "is-bird ?animal False", "is-mammal ?animal False",
        ]
    ),
    (#5 if born from egg, oviparous(animals born from egg) (includes amphibian, fish, reptiles,birds)
        "born-from-egg-implies-oviparous",
        ["born-from-egg ?animal True"],
        ["is-oviparous ?animal True"]
    ),
    (#6 if born as live, viviparous (animals give birth to live offsprings) (includes mammals)
        "not-born-from-egg-implies-viviparous",
        ["born-from-egg ?animal False"],
        ["is-oviparous ?animal False"]
    ),
    (#7 if breath throughout gills at some point in a life, gill-breathing
        "breath-through-gill-implies-gill-breathing",
        ["breath-through-gill ?animal True"],
        ["gill-breathing ?animal True"]
    ),
    (#7b if not breath throughout gills at some point in a life, gill-breathing false
        "not-breath-through-gill-implies-gill-breathing",
        ["breath-through-gill ?animal False"],
        ["gill-breathing ?animal False"]
    ),
    (#8 if breath throughout lungs at some point in a life, lung-breathing
        "breath-through-lung-implies-lung-breathing",
        ["breath-through-lung ?animal True"],
        ["lung-breathing ?animal True"]
    ),
    (#8b if not breath throughout lungs at some point in a life, lung-breathing false
        "not-breath-through-lung-implies-lung-breathing",
        ["breath-through-lung ?animal False"],
        ["lung-breathing ?animal False"]
    ),
    (#9 if breath throughout skin at some point in a life, skin-breathing
        "breath-through-skin-implies-skin-breathing",
        ["breath-through-skin ?animal True"],
        ["skin-breathing ?animal True"]
    ),
    (#10 if vertebrate, warm-blooded, viviparous (not oviparous), then mammals
        "vertebrate-warm-blooded-viviparous-imply-mammal",
        ["is-vertebrate ?animal True", "is-warm-blooded ?animal True", "is-oviparous ?animal False"],
        ["is-mammal ?animal True"]
    ),
    (#11 if vertebrate, warm-blooded, oviparous, then bird
        "vertebrate-warm-blooded-oviparous-imply-bird",
        ["is-vertebrate ?animal True", "is-warm-blooded ?animal True", "is-oviparous ?animal True"],
        ["is-bird ?animal True"]
    ),
    (#12 if vertebrate, cold-blooded, gills, not lung, then fish
        "vertebrate-cold-blooded-gills-not-lung-imply-fish",
        [
            "is-vertebrate ?animal True", 
            "is-warm-blooded ?animal False", 
            "gill-breathing ?animal True",
            "lung-breathing ?animal False"
        ],
        ["is-fish ?animal True"]
    ),
    (#12 if vertebrate, cold-blooded, not gills, lung, then reptile
        "vertebrate-cold-blooded-not-gills-lung-imply-reptile",
        [
            "is-vertebrate ?animal True", 
            "is-warm-blooded ?animal False", 
            "gill-breathing ?animal False",
            "lung-breathing ?animal True"
        ],
        ["is-reptile ?animal True"]
    ),
    (#12 if vertebrate, cold-blooded, gills, lung, skin, then amphibian
        "vertebrate-cold-blooded-gills-lung-imply-reptile",
        [
            "is-vertebrate ?animal True", 
            "is-warm-blooded ?animal False", 
            "gill-breathing ?animal True",
            "lung-breathing ?animal True"
        ],
        ["is-amphibian ?animal True"]
    )
]

def run_ps(wm, rules):
    """
    Input:
        wm: working memory
        rules: a list of rules
    """

def substitute(subs, pattern):
    """
    Input 
        substitution: 
            eg. [('?y', 'mary'), ('?x', 'john')] 
        pattern: 
            eg. '?x gave (son-of ?y) ?z' 
    Output: 
        eg. 'john gave (son-of mary) ?z
    """
    pattern = pattern.split()
    for s in subs:
        i = 0
        while i < len(pattern):
            if pattern[i] == s[0]:
                pattern[i] = s[1]
            i += 1
    
    return " ".join(pattern)
        
def is_var (string):
    """check if the string is a variable"""
    if (string[0] == '?'):
        return True
    return False

def unify(pattern1, pattern2, subs):
    """
    Input:
        two patterns and a substitution 
    Output:
        an updated substitution (possibly the empty list) or False.
    """
    pattern1 = pattern1.split()
    pattern2 = pattern2.split()

    var = [] # a list for recording variable positions
    matching = True # a flag for checking if the two patterns matching

    if len(pattern1) == len(pattern2):
        for i in range(len(pattern1)):
            if is_var(pattern1[i]) or is_var(pattern2[i]):
                var.append(i)
            else:
                if pattern1[i] != pattern2[i]:
                    matching = False
        
        if matching:
            for i in var:
                if is_var(pattern1[i]) and (not is_var(pattern2[i])):
                    subs.append((pattern1[i],pattern2[i]))
                elif is_var(pattern2[i]) and (not is_var(pattern1[i])):
                    subs.append((pattern2[i],pattern1[i]))
    
    return subs




if __name__ == "__main__":
    subs = []
    pattern1 = "has-spine ?animal True"
    pattern2 = "has-spine dog True"

    subs = unify(pattern1,pattern2,subs)
    print(subs)

    print(substitute(subs,pattern1))