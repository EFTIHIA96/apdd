from read_problem import read_problem
from read_solution import read_solution, evaluate
from save_solution import save_solution, color_dsatur


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
    graph = 0

    while True:
        print("Επιλέξτε 1-4")
        print("0. Εξοδος")
        print("1. Φόρτωση προβλήματος")
        print("2. Φόρτωση λύσης")
        print("3. Επίλυση προβλήματος ")
        print("4. Μαζική επίλυση προβλημάτων")

        # user IO keyboard
        user_input = input("Επιλέξτε")
        user_input_integer = int(user_input)

        if user_input_integer == 0:
            break

        # Ανάγνωση προβλήματος σε γραφο
        if user_input_integer == 1:
            for index, path in enumerate(paths):
                print(index, path)
            i = input("Δώστε νούμερο προβλήματος:")
            selection = int(i)
            graph = read_problem(paths[selection])

        # Άνάγνωση λύσης
        elif user_input_integer == 2:
            if graph == 0:
                print("NO problem selected")
                print()
                continue

            solution_path = input("Enter solution name:")
            solution = read_solution(solution_path)  # Ανάγνωση λύσης
            periods, feasible = evaluate(graph, solution)  #  Βαθμολόγηση λύσης
            if feasible == True:
                print("Solution is feasible")
                print(f"solution uses {periods} periods")
                print()
            else:
                print("not feasible")
                print()

        elif user_input_integer == 3:
            if graph == 0:
                print("NO problem selected")
                print()
                continue
            solution = color_dsatur(graph)
            periods, feasible = evaluate(graph, solution)
            if feasible == True:
                save_solution(problem, solution, periods)
                print(f"solution uses {periods} periods")
            else:
                print("not feasible")

        elif user_input_integer == 4:
            for problem in paths:
                graph = read_problem(problem)

                solution = color_dsatur(graph)
                periods, feasible = evaluate(graph, solution)
                if feasible == True:
                    save_solution(problem, solution, periods)
                    print(f"solution uses {periods} periods")

                else:
                    print("not feasible")
    print("Goodbye")
