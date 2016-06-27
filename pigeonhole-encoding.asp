% guess an assignment
inHole(P, H) :- not outHole(P, H), pigeon(P), hole(H).
outHole(P,H) :- not inHole(P, H), pigeon(P), hole(H).

% derive whether a pigeon is in some hole
inSomeHole(P) :- inHole(P, _).

# a hole contains at most one pigeon
:- inHole(P1, H), inHole(P2, H), P1 != P2.

# a pigeon is in at most one hole
:- inHole(P, H1), inHole(P, H2), H1 != H2.

# a pigeon must be in some hole
:- pigeon(P), not inSomeHole(P).
