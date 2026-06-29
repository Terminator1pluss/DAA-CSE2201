"""
DAA Assignment-2: Dijkstra's Algorithm — GPS Route Planner
Real-Life Scenario: Shortest path between landmarks in Jaipur, Rajasthan
Author: [Your Name] | Course: CSE2201 | Sem: IV
"""

import heapq
import matplotlib
matplotlib.use('Agg')  # non-interactive backend for screenshot generation
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np

# ─────────────────────────────────────────
# GRAPH: Jaipur landmarks with road distances (km)
# ─────────────────────────────────────────
GRAPH = {
    'Amer Fort':      [('Jal Mahal', 4), ('City Palace', 12), ('Nahargarh', 8)],
    'Jal Mahal':      [('Amer Fort', 4), ('City Palace', 6), ('Hawa Mahal', 5)],
    'City Palace':    [('Jal Mahal', 6), ('Amer Fort', 12), ('Hawa Mahal', 2),
                       ('Jantar Mantar', 1), ('Albert Hall', 4)],
    'Hawa Mahal':     [('Jal Mahal', 5), ('City Palace', 2), ('Jantar Mantar', 1),
                       ('Albert Hall', 3)],
    'Jantar Mantar':  [('City Palace', 1), ('Hawa Mahal', 1), ('Albert Hall', 3)],
    'Albert Hall':    [('City Palace', 4), ('Hawa Mahal', 3), ('Jantar Mantar', 3),
                       ('Nahargarh', 7), ('Birla Temple', 3)],
    'Nahargarh':      [('Amer Fort', 8), ('Albert Hall', 7), ('Birla Temple', 9)],
    'Birla Temple':   [('Albert Hall', 3), ('Nahargarh', 9)],
}

# Node positions for drawing (x, y) — approximate map layout
POSITIONS = {
    'Amer Fort':     (1.5, 8.5),
    'Jal Mahal':     (2.5, 7.0),
    'Nahargarh':     (1.0, 6.0),
    'City Palace':   (4.0, 6.5),
    'Hawa Mahal':    (5.0, 6.0),
    'Jantar Mantar': (4.5, 5.0),
    'Albert Hall':   (3.5, 4.0),
    'Birla Temple':  (2.0, 3.0),
}

# ─────────────────────────────────────────
# DIJKSTRA'S ALGORITHM
# ─────────────────────────────────────────
def dijkstra(graph, source):
    """
    Dijkstra's Single Source Shortest Path
    Input : graph (adjacency list), source node
    Output: dist dict (shortest distances), prev dict (predecessor for path reconstruction)
    Time  : O((V + E) log V) using min-heap
    """
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0

    # Min-heap: (distance, node)
    heap = [(0, source)]
    visited = set()
    steps = []  # for step-by-step logging

    while heap:
        d, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)
        steps.append({'node': u, 'dist': d, 'dist_table': dict(dist)})

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, prev, steps


def reconstruct_path(prev, source, target):
    """Trace back from target to source using predecessor map."""
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    if path[0] != source:
        return []  # no path exists
    return path


# ─────────────────────────────────────────
# VISUALIZATION — Screenshot 1: Full graph
# ─────────────────────────────────────────
def draw_graph(highlight_path=None, dist=None, title="Jaipur GPS Route Planner",
               filename="screenshot_1_graph.png"):

    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#16213e')
    ax.set_xlim(0, 7)
    ax.set_ylim(1.5, 10)
    ax.axis('off')

    path_edges = set()
    if highlight_path:
        for i in range(len(highlight_path) - 1):
            path_edges.add((highlight_path[i], highlight_path[i+1]))
            path_edges.add((highlight_path[i+1], highlight_path[i]))

    drawn_edges = set()
    for u, neighbors in GRAPH.items():
        for v, w in neighbors:
            edge = tuple(sorted([u, v]))
            if edge in drawn_edges:
                continue
            drawn_edges.add(edge)

            x1, y1 = POSITIONS[u]
            x2, y2 = POSITIONS[v]

            is_path = (u, v) in path_edges or (v, u) in path_edges
            color = '#00ff88' if is_path else '#4a4a6a'
            lw = 3.5 if is_path else 1.2
            zorder = 5 if is_path else 2

            ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw,
                    zorder=zorder, solid_capstyle='round')

            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx, my, str(w)+'km', fontsize=8, color='#aaaacc',
                    ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#1a1a2e',
                              edgecolor='none', alpha=0.8),
                    zorder=6)

    for node, (x, y) in POSITIONS.items():
        is_path_node = highlight_path and node in highlight_path

        if highlight_path:
            if node == highlight_path[0]:
                color, ec, size = '#00cc44', '#ffffff', 420
                label_color = '#00ff88'
            elif node == highlight_path[-1]:
                color, ec, size = '#ff4444', '#ffffff', 420
                label_color = '#ff6666'
            elif is_path_node:
                color, ec, size = '#ffaa00', '#ffffff', 350
                label_color = '#ffcc44'
            else:
                color, ec, size = '#2a2a4a', '#6666aa', 280
                label_color = '#8888bb'
        else:
            color, ec, size = '#0f3460', '#e94560', 320
            label_color = '#ffffff'

        ax.scatter(x, y, s=size, c=color, edgecolors=ec,
                   linewidths=2, zorder=10)

        dist_text = ''
        if dist and node in dist and dist[node] != float('inf'):
            dist_text = f'\n({dist[node]} km)'

        ax.text(x, y + 0.45, node + dist_text,
                fontsize=9, color=label_color, ha='center', va='bottom',
                fontweight='bold', zorder=11,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0d0d1f',
                          edgecolor='none', alpha=0.7))

    if highlight_path:
        path_str = ' → '.join(highlight_path)
        ax.set_title(f'{title}\nShortest path: {path_str}',
                     color='#00ff88', fontsize=13, pad=15, fontweight='bold')
    else:
        ax.set_title(title, color='#e94560', fontsize=14,
                     pad=15, fontweight='bold')

    legend_elements = []
    if highlight_path:
        legend_elements = [
            mpatches.Patch(color='#00cc44', label=f'Source: {highlight_path[0]}'),
            mpatches.Patch(color='#ff4444', label=f'Destination: {highlight_path[-1]}'),
            mpatches.Patch(color='#ffaa00', label='Intermediate stops'),
            mpatches.Patch(color='#00ff88', label='Shortest path'),
        ]
    else:
        legend_elements = [
            mpatches.Patch(color='#e94560', label='Landmark node'),
            mpatches.Patch(color='#4a4a6a', label='Road connection'),
        ]

    ax.legend(handles=legend_elements, loc='lower right',
              facecolor='#1a1a2e', edgecolor='#444466',
              labelcolor='white', fontsize=9)

    plt.tight_layout()
    plt.savefig(f'/home/claude/{filename}', dpi=150,
                bbox_inches='tight', facecolor='#1a1a2e')
    plt.close()
    print(f"Saved: {filename}")


# ─────────────────────────────────────────
# VISUALIZATION — Screenshot 2: Step table
# ─────────────────────────────────────────
def draw_step_table(steps, source, target, filename="screenshot_2_steps.png"):
    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    ax.axis('off')

    nodes = list(GRAPH.keys())
    col_labels = ['Step', 'Node Visited'] + nodes
    table_data = []

    for i, step in enumerate(steps):
        row = [str(i+1), step['node']]
        for n in nodes:
            v = step['dist_table'].get(n, float('inf'))
            row.append('∞' if v == float('inf') else str(v))
        table_data.append(row)

    table = ax.table(cellText=table_data,
                     colLabels=col_labels,
                     cellLoc='center', loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.2)

    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor('#333355')
        if r == 0:
            cell.set_facecolor('#e94560')
            cell.set_text_props(color='white', fontweight='bold')
        elif c == 1 and r > 0:
            cell.set_facecolor('#0f3460')
            cell.set_text_props(color='#00ff88', fontweight='bold')
        else:
            cell.set_facecolor('#16213e' if r % 2 == 0 else '#1a1a2e')
            cell.set_text_props(color='#ccccee')

    ax.set_title(f"Dijkstra Step-by-Step Distance Table\nSource: {source}  |  Target: {target}",
                 color='#e94560', fontsize=13, pad=20, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'/home/claude/{filename}', dpi=150,
                bbox_inches='tight', facecolor='#1a1a2e')
    plt.close()
    print(f"Saved: {filename}")


# ─────────────────────────────────────────
# VISUALIZATION — Screenshot 3: All distances bar chart
# ─────────────────────────────────────────
def draw_distance_chart(dist, source, filename="screenshot_3_distances.png"):
    nodes = [n for n in dist if n != source and dist[n] != float('inf')]
    distances = [dist[n] for n in nodes]

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#16213e')

    colors = ['#e94560' if d == max(distances) else
              '#00cc44' if d == min(distances) else
              '#0f3460' for d in distances]

    bars = ax.barh(nodes, distances, color=colors, edgecolor='#333355',
                   linewidth=0.8, height=0.6)

    for bar, dist_val in zip(bars, distances):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{dist_val} km', va='center', color='#ffffff',
                fontsize=10, fontweight='bold')

    ax.set_xlabel('Distance from Source (km)', color='#aaaacc', fontsize=11)
    ax.set_title(f'Shortest Distances from {source}\n(Dijkstra\'s Algorithm)',
                 color='#e94560', fontsize=13, fontweight='bold', pad=15)
    ax.tick_params(colors='#aaaacc')
    ax.spines['bottom'].set_color('#333355')
    ax.spines['left'].set_color('#333355')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_facecolor('#16213e')

    legend_elements = [
        mpatches.Patch(color='#00cc44', label='Nearest destination'),
        mpatches.Patch(color='#0f3460', label='Reachable nodes'),
        mpatches.Patch(color='#e94560', label='Farthest destination'),
    ]
    ax.legend(handles=legend_elements, facecolor='#1a1a2e',
              edgecolor='#444466', labelcolor='white', fontsize=9)

    plt.tight_layout()
    plt.savefig(f'/home/claude/{filename}', dpi=150,
                bbox_inches='tight', facecolor='#1a1a2e')
    plt.close()
    print(f"Saved: {filename}")


# ─────────────────────────────────────────
# TEXT OUTPUT — Console demonstration
# ─────────────────────────────────────────
def run_demo(source, target):
    print("=" * 62)
    print("   DAA Assignment-2: Dijkstra GPS Route Planner")
    print("   Real-Life Scenario: Jaipur Landmark Navigation")
    print("=" * 62)

    dist, prev, steps = dijkstra(GRAPH, source)
    path = reconstruct_path(prev, source, target)

    print(f"\n  Source      : {source}")
    print(f"  Destination : {target}")
    print(f"  Shortest distance: {dist[target]} km")
    print(f"  Optimal route    : {' → '.join(path)}")

    print("\n  Step-by-step execution:")
    print(f"  {'Step':<5} {'Node Visited':<20} {'Distance Assigned'}")
    print("  " + "-"*50)
    for i, step in enumerate(steps):
        print(f"  {i+1:<5} {step['node']:<20} {step['dist']} km")

    print("\n  All shortest distances from", source + ":")
    print(f"  {'Destination':<22} {'Distance'}")
    print("  " + "-"*35)
    for node, d in sorted(dist.items(), key=lambda x: x[1]):
        if node != source:
            marker = " ← OPTIMAL" if node == target else ""
            print(f"  {node:<22} {d} km{marker}")

    print("\n  Generating visualizations...")
    draw_graph(title="Jaipur GPS Route Planner — Full Graph",
               filename="screenshot_1_graph.png")
    draw_graph(highlight_path=path, dist=dist,
               title="Jaipur GPS Route Planner — Shortest Path Found",
               filename="screenshot_2_path.png")
    draw_step_table(steps, source, target,
                    filename="screenshot_3_steps.png")
    draw_distance_chart(dist, source,
                        filename="screenshot_4_distances.png")
    print("  All screenshots saved.")
    print("=" * 62)

    return dist, prev, path, steps


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
if __name__ == "__main__":
    SOURCE = "Amer Fort"
    TARGET = "Birla Temple"
    run_demo(SOURCE, TARGET)
