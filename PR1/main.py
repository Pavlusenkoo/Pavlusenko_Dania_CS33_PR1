import time

def read_students_file(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            st_lastname, st_firstname, grade, classroom, bus, t_lastname, t_firstname = line.strip().split(',')
            students.append({
                'st_lastname': st_lastname,
                'st_firstname': st_firstname,
                'grade': int(grade),
                'classroom': int(classroom),
                'bus': int(bus),
                't_lastname': t_lastname,
                't_firstname': t_firstname
            })
    return students

# Поиск по фамилии студента
def search_student_by_lastname(students, lastname):
    results = [s for s in students if s['st_lastname'].lower() == lastname.lower()]
    for student in results:
        print(f"{student['st_firstname']} {student['st_lastname']}, Класс: {student['classroom']}, Учитель: {student['t_firstname']} {student['t_lastname']}")
    return results

# Поиск автобуса по фамилии студента
def search_student_bus_by_lastname(students, lastname):
    results = [s for s in students if s['st_lastname'].lower() == lastname.lower()]
    for student in results:
        print(f"{student['st_firstname']} {student['st_lastname']}, Автобус: {student['bus']}")
    return results

# Поиск студентов по фамилии учителя
def search_students_by_teacher_lastname(students, lastname):
    results = [s for s in students if s['t_lastname'].lower() == lastname.lower()]
    for student in results:
        print(f"{student['st_firstname']} {student['st_lastname']}")
    return results

# Поиск студентов по номеру класса
def search_students_by_classroom(students, classroom):
    results = [s for s in students if s['classroom'] == classroom]
    for student in results:
        print(f"{student['st_firstname']} {student['st_lastname']}")
    return results

# Поиск студентов по автобусному маршруту
def search_students_by_bus(students, bus_number):
    results = [s for s in students if s['bus'] == bus_number]
    for student in results:
        print(f"{student['st_firstname']} {student['st_lastname']}, Класс: {student['classroom']}")
    return results

# Основной цикл программы
def main():
    students = read_students_file('students.txt')
    while True:
        command = input("Введите команду (S[tudent], T[eacher], C[lassroom], B[us], Q[uit]): ").strip()
        if command.lower().startswith('s'):
            lastname = command.split(':')[1].strip()
            if 'b' in command.lower():
                start_time = time.time()
                search_student_bus_by_lastname(students, lastname)
                print(f"Время поиска: {time.time() - start_time:.6f} секунд")
            else:
                start_time = time.time()
                search_student_by_lastname(students, lastname)
                print(f"Время поиска: {time.time() - start_time:.6f} секунд")
        elif command.lower().startswith('t'):
            lastname = command.split(':')[1].strip()
            start_time = time.time()
            search_students_by_teacher_lastname(students, lastname)
            print(f"Время поиска: {time.time() - start_time:.6f} секунд")
        elif command.lower().startswith('c'):
            classroom = int(command.split(':')[1].strip())
            start_time = time.time()
            search_students_by_classroom(students, classroom)
            print(f"Время поиска: {time.time() - start_time:.6f} секунд")
        elif command.lower().startswith('b'):
            bus_number = int(command.split(':')[1].strip())
            start_time = time.time()
            search_students_by_bus(students, bus_number)
            print(f"Время поиска: {time.time() - start_time:.6f} секунд")
        elif command.lower() == 'q':
            print("Выход из программы.")
            break
        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
