# Tower of Hanoi Recursive Solver

A Python-based implementation of the classic Tower of Hanoi puzzle. This project demonstrates the power of recursive algorithms to solve complex, multi-step problems with minimal, clean code.

## 🚀 Key Features
- **Recursive Logic:** Breaks the $n$-disk problem into smaller sub-problems.
- **Move Tracking:** Captures the state of all three rods after every single move.
- **Scalability:** Solves for any number of disks, following the rule of $2^n - 1$ moves.

## 🛠️ Technical Stack
- **Language:** Python 3
- **Concepts:** Recursion, Algorithmic Complexity, State Management

## 🧩 The Recursive Approach
To move a tower of $N$ disks from the start rod to the target rod, the algorithm performs three logical steps:
1. Move $N-1$ disks to the helper rod.
2. Move the largest disk to the target rod.
3. Move the $N-1$ disks from the helper to the target rod.



```mermaid
graph TD
    A[Start: N Disks] --> B{Base Case: N=1?}
    B -- Yes --> C[Move Disk]
    B -- No --> D[Recurse: Move N-1 to Aux]
    D --> E[Move Largest to Target]
    E --> F[Recurse: Move N-1 to Target]
