# DAA — Design and Analysis of Algorithms
### CSE2201 | B.Tech CSE | Semester IV | Manipal University Jaipur

**Faculty:** Abhay Bisht Sir  
**Student:** Aaryan Kalra | Terminator1pluss

---

## Repository Structure

```
DAA-CSE2201/
│
├── Assignment-1/               ← Theory + Analysis Assignment
│   ├── Section-A/              ← Short answer questions (Q1–Q22)
│   ├── Section-B/              ← Long analysis questions
│   └── Section-C/              ← Deep questions (BFS/DFS, MST, Sorting)
│
├── Assignment-2-Dijkstra/      ← Real-Life Implementation Project
│   ├── code/                   ← Python source code
│   ├── screenshots/            ← Output visualizations
│   └── README.md               ← Full assignment report
│
└── README.md                   ← This file
```

---

## Assignment 1 — Topics Covered

| Cluster | Topics | Questions |
|---------|--------|-----------|
| 1 | Algorithm basics, Big-O/Omega/Theta, Loop complexity | A1–A8, A18–A22 |
| 2 | Recurrences, Master Theorem, Divide & Conquer | A9–A13, B1–B4 |
| 3 | Merge Sort, Quick Sort, Randomized QS, Binary Search | A11–A12, B8–B11, C3–C4 |
| 4 | BFS, DFS, Graph representations | A14–A15, B12–B14, C1 |
| 5 | Greedy: Knapsack, Job Sequencing, Huffman, Merge Pattern | A16, B15–B18 |
| 6 | Prim's, Kruskal's, Union-Find, MST | A17, B19–B20, C2 |

---

## Assignment 2 — Dijkstra's GPS Route Planner

**Algorithm:** Dijkstra's Single Source Shortest Path  
**Real-Life Application:** GPS navigation between Jaipur landmarks  
**Language:** Python 3.12  
**Marks:** 10 + 1 Bonus (visualization)

**Shortest path found:** Amer Fort → Jal Mahal → Hawa Mahal → Albert Hall → Birla Temple = **15 km**

---

## How to Run Assignment 2

```bash
# Clone the repo
git clone https://github.com/Terminator1pluss/DAA-CSE2201.git
cd DAA-CSE2201/Assignment-2-Dijkstra/code

# Install dependencies
pip install matplotlib

# Run
python3 dijkstra_gps.py
```

Output: Console step-by-step execution + 4 PNG visualizations generated automatically.
