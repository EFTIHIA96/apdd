from itertools import combinations
from networkx import Graph
from networkx.classes.function import density

# pip install networkx
def read_problem(path):
    # Create an empty Graph
    graph = Graph()

    # initialize students
    students = 0
    enrollments = 0
    # open file with read rights
    file = open(path, "r")

    # a_list = ["4","1	5","1	2	3",...]
    # split file into lines
    lines = file.readlines()

    # For every line
    for line in lines:
        # Remove emptyspace
        line = line.strip()

        # corner case where the line is empty
        if line == "":
            continue

        students += 1

        # Split line
        exams = line.split()

        enrollments += len(exams)

        # corner case were a student has only one exam
        if len(exams) == 1:
            exam_int = int(exams[0])
            graph.add_node(exam_int)
            # goto next line
            continue

        # Create all possible combinations of exams
        # Για την [1,2,3]: [(1,2),(1,3),(2,3)]
        exam_combinations = combinations(exams, 2)

        for exam_a, exam_b in exam_combinations:
            # Cast to integers
            exam_a_int = int(exam_a)
            exam_b_int = int(exam_b)

            # Add edge to the graph
            graph.add_edge(exam_a_int, exam_b_int)

    # print density
    density_of_graph = density(graph)

    # round density to two decimal points
    density_rounded = round(density_of_graph, 2)

    # report
    print(f"Conflict density for {path} is {density_rounded}")
    print(f"Number of students: {students}")
    print(f"Number of enrollments: {enrollments}")
    print(f"Number of exams: {graph.number_of_nodes()}")

    return graph


if __name__ == "__main__":
    paths = [
        "car-f-92.stu",
        "car-s-91.stu",
        "ear-f-83.stu",
        "hec-s-92.stu",
        "kfu-s-93.stu",
        "lse-f-91.stu",
        "pur-s-93.stu",
        "rye-s-93.stu",
        "sta-f-83.stu",
        "tre-s-92.stu",
        "uta-s-92.stu",
        "ute-s-92.stu",
        "yor-f-83.stu",
    ]

    for path in paths:
        graph = read_problem(path)
        print()
    # graph = read_problem("toy.stu")
