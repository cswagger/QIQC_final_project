# Solving CLIQUE using Quantum Computing

## QAOA Setup and Execution Guide

### Step 1: Navigate to the `QAOA/` Folder
Open a terminal and move to the `QAOA/` directory where the project files are located:
```bash
cd QAOA/
```

### Step 2: Create a Virtual Environment
Ensure you have `python3.9` installed. Create an isolated Python environment to manage dependencies:
```bash
python3.9 -m venv .venv
```

### Step 3: Activate the Virtual Environment
Activate the environment to ensure all installations and executions are contained within it. For example, in **Linux/macOS**:

```bash
source .venv/bin/activate
```

### Step 4: Install Required Packages
Use `pip` to install all necessary dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 5: Run Test Cases and Validate Results
Use the `clique_QAOA.py` script to run test cases. Replace the placeholders `[inputfile]`, `[answerfile]`, and `[reps]` with your input data:

- **[inputfile]**: The path to the file containing the graph data.
- **[answerfile]**: The file where the computed results will be validated against.
- **[reps]**: Number of repetitions (layers \( p \)) for QAOA.

### Step 6: Conducting Experiments

A script `run.sh` is provided to conduct experiments.

Make sure that you have granted execution permission before executing
```bash
chmod +x run.sh
```

You could run it with
```bash
./run.sh
```

### Step 7: Deactivating the Virtual Environment
Once finished, deactivate the virtual environment to return to your default Python environment:
```bash
deactivate
```

---

## Testcases

### Input Format
The first line contains two integers, $V$ and $E$. $V$ represents the number of vertices in the graph, and $E$ represents the number of edges in the graph. The vertices are numbered from $0$ to $V - 1$.

The next $E$ lines each contain two integers, $v_1$ and $v_2$, indicating that there is an edge between $v_1$ and $v_2$.

### Output Format
The first line contains one integer $k$, indicating the number of cliques for the given input. The next $k$ lines each represent a clique, with each line listing all the vertices in the set of a clique. The vertices within a line are ordered in lexicographic order, and the lines themselves are also ordered in lexicographic order.

### Sample Input/Output
**Input**
```
6 7
0 1
1 2
0 2
3 4
4 5
3 5
1 4
```
This describes a graph with six vertices and seven edges. Vertices $0$, $1$, and $2$ form a fully connected subgraph. Similarly, vertices $3$, $4$, and $5$ form another fully connected subgraph. Additionally, there is an edge between vertices $1$ and $4$.

**Output**
```
3
0 1 2
1 4
3 4 5
```
This indicates that there are three maximal cliques: [0, 1, 2], \[1, 4], and [3, 4, 5].

### Testcase Directories
- **custom_testcases**: Contains small test cases for debugging.

- **normal_testcases**: Contains test cases with $V$ ranging from $4$ to $35$.

- **all_connected_testcases**: Contains test cases with $V$ ranging from $4$ to $35$, where all vertices are adjacent to each others.

