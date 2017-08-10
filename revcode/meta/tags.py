from enum import Enum


class Dependency_Tags(Enum):
    nsubj = 1
    dobj = 2
    xcomp = 3
    amod = 4
    compound = 5
    advmod = 6
    root = 7
    pobj = 8
    aux = 9
    acl = 10
    nsubjpass = 11
    auxpass = 12
    case = 13
    poss = 14
    csubj = 15
    csubjpass = 16
    dative = 17
    attr = 18
