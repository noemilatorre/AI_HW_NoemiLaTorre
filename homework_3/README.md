Homework 3
==========================================

## 🎯 Exercise 1: Museum Emergency Exit System

### Problem Description
Implement an intelligent emergency evacuation system for a museum using the A* pathfinding algorithm. The system helps visitors find the shortest safe path to the nearest emergency exit during critical situations.

### Key Features
- 🗺️ Grid-based navigation system
- 🎯 A* pathfinding implementation
- 🚪 Multiple exit support
- 🚧 Obstacle avoidance
- 📊 Visual path representation

### Learning Objectives
- Understanding A* algorithm implementation
- Working with grid-based navigation
- Implementing heuristic functions
- Handling obstacle avoidance
- Data visualization techniques


### Hints:
- Start by implementing the Manhattan distance heuristic
- Use a simple priority queue (heapq) for selecting next nodes
- Break down the problem into small steps: first find valid moves, then implement 
  the core algorithm
- Consider edge cases like when no path exists

## 🎯 Exercise 2: City Power Grid Optimization

### Problem Description
Design an optimal power distribution network for a city using Prim's algorithm. The goal is to minimize installation costs while ensuring all neighborhoods have reliable power access.

### Key Features
- 🏙️ Real-world cost modeling
- 📊 Network optimization
- 💡 Connection cost analysis
- 🗺️ Network visualization
- 📈 Performance reporting

### Learning Objectives
- Understanding Prim's algorithm
- Working with weighted graphs
- Implementing priority queues
- Cost optimization strategies
- Network visualization skills

### Hints:
- Start by creating a clear graph representation of the neighborhoods
- Use a priority queue to efficiently select the next edge
- Consider creating helper methods for adding edges and updating the MST
- Think about how to handle disconnected components
- Consider factors like maintenance access when designing the network

## 📊 Visualization Examples

### Museum Layout
The visualization shows:
- 🟦 Free spaces (White)
- ⬛ Walls/Obstacles (Gray)
- 🟥 Emergency exits (Red)
- 🟨 Calculated path (Yellow)
- 🟦 Current position (Blue)

### Power Grid Network
The visualization displays:
- 🔴 Power stations (Red dots)
- ⚡ Possible connections (Gray lines)
- 🟢 Optimal connections (Green lines)
- 💰 Connection costs (Annotations)
- 

## 🗂️ Project Structure
-----------------
```
homework_3/
│
├── README.md
├── main.py
├── exercise_1/
│   ├── __init__.py
│   └── astar.py.py
│
└── exercise_2/
    ├── __init__.py
    └── prims.py
```