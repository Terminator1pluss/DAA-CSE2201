# Assignment 1 — Section A: Short Answer Questions

**Course:** CSE2201 Design and Analysis of Algorithms  
**Faculty:** Abhay Bisht Sir | **Sem:** IV Summer 2026

---

## Q1. Define an algorithm. Write any two characteristics of a good algorithm.

An **algorithm** is a finite set of well-defined instructions to solve a problem in a limited amount of time and space.

Two characteristics of a good algorithm:
- **Finiteness:** Must terminate after a finite number of steps.
- **Definiteness:** Each step must be precisely and unambiguously defined.

---

## Q2. Differentiate between iterative and recursive algorithms.

| Feature | Iterative | Recursive |
|---|---|---|
| Definition | Uses loops to repeat steps | Function calls itself |
| Memory | Constant stack memory | Uses call stack |
| Termination | Loop condition | Base case |
| Example | `for` loop for factorial | `fact(n) = n × fact(n−1)` |

---

## Q3. Explain priori analysis and posteriori analysis.

- **Priori Analysis:** Theoretical analysis done *before* execution. Counts operations as a function of input size n. Machine-independent.
- **Posteriori Analysis:** Practical analysis done *after* execution. Measures actual time and memory on a specific machine. Machine-dependent.

---

## Q4. Define Big-O notation with one suitable example.

**Big-O notation** defines the **upper bound** on the growth rate of an algorithm's time complexity.

**Formally:** f(n) = O(g(n)) if ∃ constants c > 0 and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀.

**Example:** Linear search = O(n) — worst case checks all n elements.

---

## Q5. Differentiate between Big-O and Big-Ω notations.

| Feature | Big-O | Big-Ω |
|---|---|---|
| Bound type | Upper bound | Lower bound |
| Represents | Worst case | Best case |
| Definition | f(n) ≤ c·g(n) | f(n) ≥ c·g(n) |
| Example | Linear search = O(n) | Linear search = Ω(1) |

---

## Q6. What is asymptotic analysis? Why is it important?

**Asymptotic analysis** evaluates algorithm efficiency as input size n → ∞, using O, Ω, Θ notations.

**Importance:**
- Machine-independent comparison of algorithms
- Ignores hardware-specific constants, focuses on growth rate
- Identifies scalability before implementation

---

## Q7. Define time complexity and space complexity.

- **Time Complexity:** Number of basic operations as a function of n. Example: Bubble Sort = O(n²).
- **Space Complexity:** Total memory used including input and auxiliary space. Example: Merge Sort = O(n) auxiliary.

---

## Q8. Find complexity: `for(i=1; i<=n; i=i*2) print(i)`

**Working:** i takes values 1, 2, 4, 8, ..., 2^k until 2^k ≤ n → k = log₂n

**Executions = ⌊log₂n⌋ + 1**  
**Time Complexity = O(log n)**

---

## Q9. What is a recurrence relation? Give one example.

A **recurrence relation** expresses the time complexity of a recursive algorithm in terms of smaller subproblems.

**Example:** Merge Sort → T(n) = 2T(n/2) + n, T(1) = 1 → solves to O(n log n).

---

## Q10. State the Master Theorem.

For T(n) = aT(n/b) + f(n), where a ≥ 1, b > 1:

| Case | Condition | Result |
|---|---|---|
| Case 1 | f(n) = O(n^(log_b a − ε)) | T(n) = Θ(n^log_b a) |
| Case 2 | f(n) = Θ(n^log_b a) | T(n) = Θ(n^log_b a · log n) |
| Case 3 | f(n) = Ω(n^(log_b a + ε)) | T(n) = Θ(f(n)) |

---

## Q11. Why is Merge Sort stable?

During the merge step, when two elements are equal, the element from the **left subarray is always placed first**, preserving original relative order → stable.

---

## Q12. Why is Randomized Quick Sort preferred over normal Quick Sort?

Normal Quick Sort with fixed pivot degrades to O(n²) on sorted/reverse-sorted arrays. Randomized Quick Sort picks pivot randomly, making worst-case probability negligible → expected O(n log n) for all inputs.

---

## Q13. Define Divide and Conquer with one example.

**Divide and Conquer** has three phases:
1. **Divide:** Split into smaller subproblems
2. **Conquer:** Solve recursively
3. **Combine:** Merge solutions

**Example:** Merge Sort → T(n) = 2T(n/2) + n = O(n log n)

---

## Q14. What is graph representation? Name two methods.

**Graph representation** is how G(V,E) is stored in memory.

1. **Adjacency Matrix:** 2D array, cell [i][j]=1 if edge exists
2. **Adjacency List:** Array of lists, each storing neighbours

---

## Q15. Differentiate BFS and DFS.

| Feature | BFS | DFS |
|---|---|---|
| Data structure | Queue | Stack/Recursion |
| Order | Level by level | Deep path first |
| Time complexity | O(V+E) | O(V+E) |
| Application | Shortest path (unweighted) | Topological sort |

---

## Q16. What is the greedy strategy? Give one real-life example.

**Greedy strategy** always makes the locally optimal choice at each step.

**Example:** Activity Selection — always pick the activity finishing earliest to maximize non-overlapping activities.

---

## Q17. Purpose of Union-Find in Kruskal's algorithm?

**Union-Find** tracks connected components. Before adding edge (u,v):
- **Find(u) = Find(v)** → same component → cycle → skip
- **Find(u) ≠ Find(v)** → **Union(u,v)** → add to MST

---

## Q18. `for(i=1;i<=n;i++) for(j=1;j<=n;j++) print(i,j)`

Outer: n times. Inner: n times for every i.  
**Total = n × n = n²**  
**Time Complexity = O(n²)**

---

## Q19. `for(i=1;i<=n;i++) for(j=1;j<=i;j++) print(i,j)`

When i=1: 1 time. i=2: 2 times. ... i=n: n times.  
**Total = 1+2+3+...+n = n(n+1)/2**  
**Time Complexity = O(n²)**

---

## Q20. `for(i=1;i<=n;i=i*2) for(j=1;j<=n;j++) print(i,j)`

Outer: log n times (i doubles). Inner: n times for every i.  
**Total = n × log n**  
**Time Complexity = O(n log n)**

---

## Q21. `for(i=n;i>=1;i=i/2) for(j=1;j<=i;j++) print(i,j)`

Outer: log n times (i halves). Inner: i times (shrinks with outer).  
Total = n + n/2 + n/4 + ... + 1 = **2n** (geometric series, sum = 2a)  
**Time Complexity = O(n)**

---

## Q22. `for(i=1;i<=n;i++) for(j=1;j<=n;j=j*2) print(i,j)`

Outer: n times. Inner: log n times (j doubles).  
**Total = n × log n**  
**Time Complexity = O(n log n)**
