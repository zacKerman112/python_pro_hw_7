import csv


def process_students_data(file_path: str) -> None:
    students: list[dict[str, str]] = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)

        if students:
            total_score = sum(int(s['mark']) for s in students)
            average_scr = total_score / len(students)
            print(f"Average mark: {average_scr:.2f}")

        new_student = ['Lina', 22, 96]

        with open(file_path, mode="a", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_student)

        print(f"The student: {new_student} has been added to the file successfully")

    except FileNotFoundError as file_not_err:
        print(f"We cannot find the file {file_not_err}")

    except Exception as e:
        print(f"Some error: {e}")


if __name__ == "__main__":
    process_students_data('students.csv')