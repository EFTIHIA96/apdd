from networkx import Graph


def read_solution(path):
    # Create an empty dictionary
    solution = dict()

    # open file with read rights
    file = open(path, "r")

    # split file into lines
    lines = file.readlines()

    # For every line in lines
    for line in lines:
        # Remove emptyspace
        line = line.strip()
        if line == "":
            continue
        # split line
        line_contains = line.split()

        exam = int(line_contains[0])
        period = int(line_contains[1])
        solution[exam] = period

    return solution


def evaluate(graph: Graph, solution):
    used_periods = dict()
    # Check that all exams are present and on valid periods
    for exam in graph:
        if exam not in solution.keys():
            return 0, False
        assigned_period = solution[exam]
        if assigned_period < 0:
            return 0, False
        used_periods[assigned_period] = True

    # Check that no hard constraint is violated and evaluate
    for exam_a, exam_b in graph.edges():
        if solution[exam_a] == solution[exam_b]:
            return 0, False

    return len(used_periods), True
