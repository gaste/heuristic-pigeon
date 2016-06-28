var = {1: 'false', 'false': 1}
P = []  # list of all pigeon-constants
H = []  # list of all hole-constants


def addedVarName(v, name):
    global var, H, P
    var.update({v: name, name: v})
    if name.startswith("pigeon"):
        P.append(name[7:-1])
    if name.startswith("hole"):
        H.append(name[5:-1])


def onFinishedParsing():
    # no simplification
    return [v for v in var.keys()
            if isinstance(v, int)]


def choiceVars():
    global var, H, P
    if len(P) > len(H):
        return [4, 0]  # force incoherence
    # assign pigeon i to hole i
    return [var["inHole(%s,%s)" % (P[i], H[i])]
            for i in range(0, len(P) - 1)]


def ignorePolarity():
    pass  # required for choiceVars