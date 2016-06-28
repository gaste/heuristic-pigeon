def addedVarName(var, name):
    """
    Optional.
    This method is invoked while reading the name associated to a variable.
    :param var: the id of the variable
    :param name: the name associated to var
    """
    pass


def onStartingSolver(num_vars, num_clauses):
    """
    Optional.
    When the computation starts (after reading the input and performing the simplifications).
    :param num_vars: number of vars.
    :param num_clauses: number of clauses. The ids for variables start from 1.
    """
    # set-up interpretation as everything is unknown
    global interpretation, UNKNOWN
    interpretation = [UNKNOWN] * (num_vars + 1)


def choiceVars():
    """
    Required.
    This method is invoked when a choice is needed. It can return a choice, a list of choices and special
    values for performing special actions.
    Special values:
     - [1, 0] force the solver to perform a restart
     - [n, 2, 0] use the fallback heuristic for n steps (n<=0 use always fallback heuristic) -> require the presence of the method fallback() in the script
     - [v, 3, 0] unroll the truth value of the variable v
     - [4, 0] force the solver to stop the computation returning incoherent
    :return: A list of choices. Be careful, the first choice is the last element in the list.
    """
    pass


def ignorePolarity():
    """
    Required if onChoiceContradictory has not been set.
    This method tells the solver to use the suggested polarity if possible, otherwise the solver infers the polarity in order to have no conflicts. If this method is added than onChoiceContradictory must not be added.
    """
    pass
