import os


class PhonebookEntry:
    """Инициализация объекта PhonebookEntry.
    last_name: Фамилия.
     first_name: Имя.
     middle_name: Отчество.
     organization: Название организации.
     work_phone: Рабочий телефон.
     :personal_phone: Личный телефон."""



def __init__(self, last_name, first_name, middle_name, organization, work_phone, personal_phone):
    self.last_name = last_name
    self.first_name = first_name
    self.middle_name = middle_name
    self.organization = organization
    self.work_phone = work_phone
    self.personal_phone = personal_phone


def __str__(self):
    """Преобразование объекта в строку для вывода.
    return: Строка с информацией о записи."""


    return f"{self.last_name} {self.first_name} {self.middle_name}, {self.organization}, Рабочий: {self.work_phone}, Личный: {self.personal_phone}"


class Phonebook:
    """Инициализация объекта Phonebook.
    data_file: Имя файла для хранения данных справочника."""


    def __init__(self, data_file):
        self.data_file = data_file
        self.entries = self.load_entries()

    def load_entries(self):
        """Загрузка записей из файла.
        return: Список объектов PhonebookEntry."""

        entries = []
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(";")
                    if len(parts) == 6:
                        entry = PhonebookEntry(*parts)
                        entries.append(entry)
        return entries

    def save_entries(self):
        """Сохранение записей в файл."""

        with open(self.data_file, "w") as f:
            for entry in self.entries:
                f.write(f"{entry.last_name};{entry.first_name};{entry.middle_name};"
                        f"{entry.organization};{entry.work_phone};{entry.personal_phone}\n")

    def display_entries(self, page_size, page_number):
        """Вывод записей на экран постранично.
        page_size: Количество записей на странице.
        page_number: Номер текущей страницы."""

        start_idx = (page_number - 1) * page_size
        end_idx = start_idx + page_size
        for idx, entry in enumerate(self.entries[start_idx:end_idx], start=start_idx + 1):
            print(f"{idx}. {entry}")

    def add_entry(self):
        """Добавление новой записи в справочник."""

        print("Добавление новой записи")
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        middle_name = input("Отчество: ")
        organization = input("Организация: ")
        work_phone = input("Телефон рабочий: ")
        personal_phone = input("Телефон личный: ")
        entry = PhonebookEntry(last_name, first_name, middle_name, organization, work_phone, personal_phone)
        self.entries.append(entry)
        self.save_entries()
        print("Запись успешно добавлена!")

    def edit_entry(self, entry_index):
        """Редактирование существующей записи в справочнике.
        entry_index: Индекс записи для редактирования."""

        if 0 <= entry_index < len(self.entries):
            entry = self.entries[entry_index]
            while True:
                print("Редактирование записи")
                print("Выберите поле для редактирования:")
                print("1. Фамилия")
                print("2. Имя")
                print("3. Отчество")
                print("4. Организация")
                print("5. Телефон рабочий")
                print("6. Телефон личный")
                print("7. Завершить редактирование")
                field_choice = input("Введите номер поля или '7' для завершения редактирования: ")

                if field_choice == "1":
                    entry.last_name = input(f"Фамилия ({entry.last_name}): ")
                elif field_choice == "2":
                    entry.first_name = input(f"Имя ({entry.first_name}): ")
                elif field_choice == "3":
                    entry.middle_name = input(f"Отчество ({entry.middle_name}): ")
                elif field_choice == "4":
                    entry.organization = input(f"Организация ({entry.organization}): ")
                elif field_choice == "5":
                    entry.work_phone = input(f"Телефон рабочий ({entry.work_phone}): ")
                elif field_choice == "6":
                    entry.personal_phone = input(f"Телефон личный ({entry.personal_phone}): ")
                elif field_choice == "7":
                    break
                else:
                    print("Некорректный выбор поля.")

                self.save_entries()
                print("Запись успешно отредактирована!")
        else:
            print("Некорректный индекс записи.")

    def search_entries(self):
        """Поиск записей по различным характеристикам."""

        print("Выберите тип поиска:")
        print("1. По фамилии")
        print("2. По имени")
        print("3. По организации")
        print("4. По рабочему телефону")
        print("5. По личному телефону")
        search_type = input("Введите номер типа поиска: ")

        search_term = input("Введите строку для поиска: ").lower()
        found_entries = []

        if search_type == "1":
            found_entries = [entry for entry in self.entries if search_term in entry.last_name.lower()]
        elif search_type == "2":
            found_entries = [entry for entry in self.entries if search_term in entry.first_name.lower()]
        elif search_type == "3":
            found_entries = [entry for entry in self.entries if search_term in entry.organization.lower()]
        elif search_type == "4":
            found_entries = [entry for entry in self.entries if search_term in entry.work_phone]
        elif search_type == "5":
            found_entries = [entry for entry in self.entries if search_term in entry.personal_phone]
        else:
            print("Некорректный тип поиска.")

        if found_entries:
            print("Найденные записи:")
            for idx, entry in enumerate(found_entries, start=1):
                print(f"{idx}. {entry}")
        else:
            print("Записи не найдены.")


def main():
    """Главная функция программы для управления телефонным справочником."""

    data_file = "phonebook.txt"
    phonebook = Phonebook(data_file)
    page_size = 5
    page_number = 1

    while True:
        print("\nТелефонный справочник")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            phonebook.display_entries(page_size, page_number)
            while True:
                command = input("Введите 'n' для следующей страницы, 'p' для предыдущей, или 'b' для возврата в меню: ")
                if command == "n":
                    page_number += 1
                    break
                elif command == "p" and page_number > 1:
                    page_number -= 1
                    break
                elif command == "b":
                    break
                else:
                    print("Некорректная команда!")

        elif choice == "2":
            phonebook.add_entry()

        elif choice == "3":
            entry_index = int(input("Введите индекс записи для редактирования: ")) - 1
            phonebook.edit_entry(entry_index)

        elif choice == "4":
            phonebook.search_entries()

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    main()
