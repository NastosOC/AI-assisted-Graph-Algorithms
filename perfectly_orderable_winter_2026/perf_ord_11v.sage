import os
import time
from datetime import timedelta, datetime
from itertools import combinations, permutations, product

# ---------- Core Pruned Search Algorithm and Helpers ----------

def induced_P4s(G):
    """Return all induced paths a‑b‑c‑d."""
    P4=[]
    for S in combinations(list(G.vertices()),4):
        H=G.subgraph(S)
        if H.size()!=3: continue
        if sorted(H.degree(v) for v in S)!=[1,1,2,2]: continue
        for a,b,c,d in permutations(list(S),int(4)):
            if all(H.has_edge(x,y) for x,y in [(a,b),(b,c),(c,d)]) and \
               not any(H.has_edge(x,y) for x,y in [(a,c),(a,d),(b,d)]):
                P4.append((a,b,c,d)); break
    return P4

def is_perfectly_orderable_pruned(G):
    """Uses a corrected pruned backtracking search to find a perfect orientation."""
    edges_to_orient = list(G.edges(labels=False))
    if not edges_to_orient: return True
    
    all_p4s = induced_P4s(G)

    def has_obstruction_in_partial_orientation(D):
        for a,b,c,d in all_p4s:
            if D.has_edge(a,b) and D.has_edge(d,c): return True
        return False

    def search(D, remaining_edges):
        if not remaining_edges: return True
        edge, rest, (u, v) = remaining_edges[0], remaining_edges[1:], remaining_edges[0]

        D.add_edge(u, v)
        if D.distance(v, u) == Infinity and not has_obstruction_in_partial_orientation(D):
            if search(D, rest): return True
        D.delete_edge(u, v)

        D.add_edge(v, u)
        if D.distance(u, v) == Infinity and not has_obstruction_in_partial_orientation(D):
            if search(D, rest): return True
        D.delete_edge(v, u)
        
        return False

    # --- THIS IS THE CORRECTED PART ---
    initial_D = DiGraph()
    initial_D.add_vertices(G.vertices())
    return search(initial_D, edges_to_orient)

# ---------- Property and Subgraph Filters ----------

P5_target = graphs.PathGraph(5)

def is_P5_free(G):
    """Checks for an induced P5."""
    for S in combinations(list(G.vertices()), 5):
        if G.subgraph(S).is_isomorphic(P5_target):
            return False
    return True

# Define the complete list of known minimal forbidden induced subgraphs
forbidden_subgraphs = {
    5: [graphs.CycleGraph(5)],
    6: [graphs.CycleGraph(6).complement()],
    7: [graphs.CycleGraph(7), graphs.CycleGraph(7).complement()],
    8: [Graph("GCpdao"), Graph("GCpbQs"), graphs.CycleGraph(8).complement()],
    9: [graphs.CycleGraph(9), graphs.CycleGraph(9).complement(),
        Graph("H?`af@X"), Graph("H?qadbB"), Graph("H?qacha"),
        Graph("H?ovDdj"), Graph("H?otTbb"), Graph("HCpburY")]
}

def has_known_forbidden_subgraph(G):
    """Checks for known forbidden subgraphs."""
    for n in sorted(forbidden_subgraphs.keys()):
        if G.order() < n: continue
        for target in forbidden_subgraphs[n]:
            k = target.order()
            for S in combinations(list(G.vertices()), k):
                if G.subgraph(S).is_isomorphic(target):
                    return True
    return False

# ---------- Main Enumeration for 10 Vertices ----------

# =========================================================================
# === SET YOUR STARTING POINT HERE ===

start_index = 0
# =========================================================================

# --- Output Configuration ---
OUTPUT_DIR = "non_perfectly_orderable_graphs_11"
G6_LOGFILE = "non_perfectly_orderable_g6_11.txt"
MAPFILE = "image_g6_map_11.tsv"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Scanning 10‑vertex graphs with PRUNED SEARCH.")
print("Filters: connected, prime, non-chordal, P5-free AND long-antihole-free, and free of known smaller obstructions.\n")

geng_iterator = graphs.nauty_geng("11 -c")
#g6_list = ["I_GOGPbcw", "I`@?X?X`w", "I_D@?ekBw", "IBAH?SFqW", "I`?KQScDG"]
#geng_iterator = (Graph(s) for s in g6_list)

total_graphs = 1006700565

count_candidates = 0
count_bad = 0
last_processed_index = -1

# --- Progress timing ---
chunk_size = 10000
start_time = time.time()
last_chunk_time = start_time
chunks_completed = 0

for i, G in enumerate(geng_iterator):
    last_processed_index = i
    if i < start_index:
        continue
    
    if (i+1) % 10000 == 0:
        #print(f"  ...processed {i+1}/{total_graphs}")
        now = time.time()

        chunk_elapsed = now - last_chunk_time
        total_elapsed = now - start_time

        chunks_completed += 1
        avg_chunk_time = total_elapsed / chunks_completed

        remaining_chunks = (total_graphs - (i + 1)) / chunk_size
        est_remaining = remaining_chunks * avg_chunk_time

        eta = datetime.now() + timedelta(seconds=est_remaining)

        print(
            f"  ...processed {i + 1}/{total_graphs}\n"
            f"     chunk time: {timedelta(seconds=chunk_elapsed)}\n"
            f"     avg / 10k:  {timedelta(seconds=avg_chunk_time)}\n"
            f"     elapsed:   {timedelta(seconds=total_elapsed)}\n"
            f"     ETA:       {eta.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        last_chunk_time = now

    G.relabel()
    # Apply filters
    if G.is_chordal():                    continue
    if not G.is_prime():                  continue
    if is_P5_free(G) and G.is_long_antihole_free(): continue
    #if has_known_forbidden_subgraph(G):   continue
    
    count_candidates += 1
    
    # Run the expensive pruned check
    if not is_perfectly_orderable_pruned(G):
        count_bad += 1
        Gc = G.complement()
        
        print(f"\n-- Found Non-Perfectly-Orderable Graph -- (i = {i})")
        print(f"  Graph (G) G6 string: {G.graph6_string()}")
        print(f"  Edges ({G.size()}): {G.edges(labels=False)}")
        #G.show()
        
        print(f"\n  Complement (Gc) G6 string: {Gc.graph6_string()}")
        print(f"  Edges ({Gc.size()}): {Gc.edges(labels=False)}")
        #Gc.show()

        # --- Save PNG + Log Mapping ---
        # The with statement ensures automatic closing
        g6 = G.graph6_string()

        image_name = f"i{i:08d}.png"
        png_path = os.path.join(OUTPUT_DIR, image_name)
        G.plot(vertex_size=300, vertex_labels=False).save(png_path)

        with open(G6_LOGFILE, "a") as f:
            f.write(g6 + "\n")
        with open(MAPFILE, "a") as f:
            f.write(f"{image_name}\t{g6}\n")

print(f"\n\n--- Search Complete (or timed out) ---")
print(f"Last index processed: {last_processed_index}")
print(f"Candidate graphs checked in this run: {count_candidates}")
print(f"New non-perfectly-orderable graphs found: {count_bad}")
