# Algorithm Katas

A collection of algorithms and data structures short enough to fit on an A6 index card (105×148mm).

## Implemented algorithms

- [x] [Dijkjstra’s shortest path](src/dijkstra.py)
- [x] [Bellman-Ford shortest path](src/bellmanford.py)
- [x] [Floyd-Warshall all-pairs shortest path](src/floydwarshall.py)
- [x] [Union-Find disjoint set](src/unionfind.py)

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
Function signatures are untyped,
but the code follows common conventions:
- `u` and `v` are vertices of `type Vertex = int`.
   Edges always go from `u` to `v`.
- `s` is a source vertex of type `int`.
- `e` is an edge of type `tuple[Vertex, Vertex, Weight]`.
- `w` is a weight of some numeric type (`int` or `float`).
- `g` is an adjacency list representation of a graph, of type `list[list[tuple[Vertex, Weight]]]`.
- `d` is a distance array or matrix (depending on the algorithm), of type `list[Weight]` or `list[list[Weight]]`.
- `p` is a predecessor array or matrix (depending on the algorithm), of type `list[Vertex]` or `list[list[Vertex]]`.
