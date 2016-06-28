variables = {1: 'false', 'false': 1}
holes = []
pigeons = []


def addedVarName(var, name):
    global variables, holes, pigeons
    variables.update({var: name, name: var})
    if name.startswith("pigeon"):
        pigeons.append(name[7:-1])
    if name.startswith("hole"):
        holes.append(name[5:-1])


def onFinishedParsing():
    # do not remove any variable during simplification
    return [v for v in variables.keys() if isinstance(v, int)]


def choiceVars():
    global variables, holes, pigeons
    if len(pigeons) > len(holes):
        return [4, 0]  # force incoherence
    # assign pigeon i to hole i
    return [variables["inHole(%s,%s)" % (pigeons[i], holes[i])]
            for i in range(0, len(pigeons) - 1)]


def ignorePolarity():
    pass  # required for choiceVars
