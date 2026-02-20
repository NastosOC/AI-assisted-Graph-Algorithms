from collections import defaultdict, deque
from itertools import permutations

def all_P4s(G):
    adj = {v: set(G.neighbors(v)) for v in G.vertices()}
    def has_edge(u,v): return v in adj[u]
    r = int(4)
    return [(a,b,c,d) for a,b,c,d in permutations(G.vertices(), r)
            if has_edge(a,b) and has_edge(b,c) and has_edge(c,d)
            and not has_edge(a,c) and not has_edge(a,d) and not has_edge(b,d)]

def prove_non_PO(G):
    P4s = all_P4s(G)

    def refute(orient, trail):
        succ = defaultdict(set)
        for (u,v) in orient.values():
            succ[u].add(v)

        def has_path(u,v):
            seen, Q = {u}, deque([u])
            while Q:
                x = Q.popleft()
                for w in succ[x]:
                    if w == v: return True
                    if w not in seen:
                        seen.add(w); Q.append(w)
            return False

        def do_orient(u,v,reason):
            F = frozenset({u,v})
            if F in orient:
                return orient[F] == (u,v)
            if has_path(v,u):
                trail.append(f"{u}->{v} would close a cycle – CONTRADICTION")
                return False
            orient[F] = (u,v)
            succ[u].add(v)
            trail.append(f"{u}->{v}  ({reason})")
            return True

        changed = True
        while changed:
            changed = False
            for a,b,c,d in P4s:
                Fab, Fcd = frozenset({a,b}), frozenset({c,d})
                d1, d2 = orient.get(Fab), orient.get(Fcd)
                if d1 == (b,a) and d2 == (c,d):
                    trail.append(f"P4 {a}-{b}-{c}-{d}: have {b}->{a} & {c}->{d} – CONTRADICTION")
                    return True
                if d1 == (b,a) and d2 is None:
                    if not do_orient(d,c,f"P4 {a}-{b}-{c}-{d} forbids {c}->{d}"):
                        return True
                    changed = True
                elif d2 == (c,d) and d1 is None:
                    if not do_orient(a,b,f"P4 {a}-{b}-{c}-{d} forbids {b}->{a}"):
                        return True
                    changed = True
            for u in G.vertices():
                for v in G.neighbors(u):
                    F = frozenset({u,v})
                    if F not in orient:
                        if has_path(u,v):
                            if not do_orient(u,v,"acyclicity"): return True
                            changed = True
                        elif has_path(v,u):
                            if not do_orient(v,u,"acyclicity"): return True
                            changed = True

        for u in G.vertices():
            for v in G.neighbors(u):
                if frozenset({u,v}) not in orient:
                    branch_trails = []
                    for s,t in [(u,v),(v,u)]:
                        o2 = dict(orient)
                        t2 = [f"Assume {s}->{t}"]
                        o2[frozenset({s,t})] = (s,t)
                        if not refute(o2, t2):
                            return False
                        branch_trails.append(t2)
                    for bt in branch_trails:
                        trail.extend(bt)
                    trail.append(f"{{{u},{v}}} impossible either way – CONTRADICTION")
                    return True
        return False

    trail = []
    refute({}, trail)
    for i,l in enumerate(trail,1):
        print(f"{i}. {l}")


# for each g6 string in the list, do the following
G = Graph("I?`@d`pJW")
G = Cycle_Graph(6).complement()
G.show()
prove_non_PO(G)
