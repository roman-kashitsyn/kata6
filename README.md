# Algorithm Katas

A collection of algorithms and data structures short enough to fit on an A6 index card (105×148mm).

## Building the cards

Render every algorithm in `src/*` into `cards.pdf` (one A6 landscape page each):

```
uv run build-cards
```

The script uses [typst](https://github.com/typst/typst) to render the PDF.
On the first run, it fetches the pinned binary and caches it in `.bin/`.

The default font is the Typst-embedded **DejaVu Sans Mono**.
You can override it with the `--font` option.

```
uv run build-cards --font "JetBrains Mono"
```

## Implemented algorithms

- [ ] Topological sort
- [x] [Dijkstra’s shortest path](src/dijkstra.py)
- [x] [Bellman-Ford shortest path](src/bellmanford.py)
- [x] [Floyd-Warshall all-pairs shortest path](src/floydwarshall.py)
- [x] [Union-Find disjoint set](src/unionfind.py)
- [x] [Prim's spanning tree](src/prim.py)
- [x] [Kruskal's spanning tree](src/kruskal.py)
- [ ] Tarjan's strongly-connected components
- [ ] Kuhn's bipartite matching
- [ ] Edmonds-Karp max flow
- [ ] Fenwick tree
- [ ] Knuth-Morris-Pratt search
- [ ] Rabin-Karp search
- [ ] Edit distance
- [ ] Meyers diff
- [ ] Burrows-Wheeler transform
- [ ] Suffix array construction
- [ ] Graham's convex hull
- [ ] Point in polygon (ray casting)
- [ ] Miller-Rabin primality test
- [ ] Reservoir sampling
- [ ] Quick select
- [ ] Huffman code
- [x] [Fast exponentiation](src/fastexp.py)
- [ ] Boyer-Moore majority vote
- [ ] Floyd's cycle finding
- [ ] Cooley–Tukey FFT

## Layout

- `src/` --- algorithm implementations
- `tests/` --- unit tests (`pytest`)

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).
Run the test suite with `uv run pytest`.

## Formatting and linting

Format the code with `uv run ruff format`.
Check style with `uv run ruff check` (add `--fix` to auto-fix).

## Naming conventions

Variable names are terse for brevity.
Function signatures are untyped, but the code follows common conventions:
- `u` and `v` are vertices of `type Vertex = int`.
   Edges always go from `u` to `v`.
- `s` is a source vertex of type `int`.
- `e` is an edge of type `tuple[Vertex, Vertex, Weight]`.
- `w` is a weight of some numeric type (`int` or `float`).
- `g` is an adjacency list representation of a graph, of type `list[list[tuple[Vertex, Weight]]]`.
- `d` is a distance array or matrix (depending on the algorithm), of type `list[Weight]` or `list[list[Weight]]`.
- `p` is a predecessor array or matrix (depending on the algorithm), of type `list[Vertex]` or `list[list[Vertex]]`.
