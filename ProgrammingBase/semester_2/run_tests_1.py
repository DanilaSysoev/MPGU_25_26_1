import json

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BLUE = '\033[94m'

def check(condition, message):
    """Вспомогательная функция для генерации AssertionError с понятным текстом"""
    if not condition:
        raise AssertionError(message)

def run_test_case(test_name, test_func):
    """Выполняет один тест, перехватывает ошибки и выводит результат с подсказками."""
    try:
        test_func()
        print(f"  {GREEN}[+] {test_name} - ПРОЙДЕН{RESET}")
        return True
    except AssertionError as e:
        print(f"  {RED}[-] {test_name} - ОШИБКА{RESET}")
        print(f"      {YELLOW}Подсказка: {e}{RESET}")
        return False
    except Exception as e:
        print(f"  {RED}[-] {test_name} - ОШИБКА ВЫПОЛНЕНИЯ{RESET}")
        print(f"      {YELLOW}Код упал с ошибкой '{type(e).__name__}'. Проверьте логику функции.{RESET}")
        return False

def check_module(module_name, required_functions):
    try:
        module = __import__(module_name)
        missing_funcs = [func for func in required_functions if not hasattr(module, func)]
        if missing_funcs:
            print(f"{RED}КРИТИЧЕСКАЯ ОШИБКА в {module_name}.py:{RESET} Не найдены функции: {', '.join(missing_funcs)}.")
            return None
        return module
    except ImportError:
        print(f"{RED}КРИТИЧЕСКАЯ ОШИБКА:{RESET} Файл {module_name}.py не найден.")
        return None
    except Exception as e:
        print(f"{RED}КРИТИЧЕСКАЯ ОШИБКА:{RESET} Ошибка импорта {module_name}.py: {e}")
        return None

def test_junior():
    print(f"\n{BLUE}=== Запуск тестов БЛОК 1 (Junior) ==={RESET}")
    score = 0
    funcs = ['create_hashtags', 'filter_prices', 'cleanup_users', 'convert_grades', 'find_phone']
    module = check_module('junior', funcs)
    if not module:
        return 0

    print("\nТестирование create_hashtags:")
    r1 = run_test_case("Базовый и регистр", lambda: check(module.create_hashtags("PyThOn is GREAT") == ["#python", "#is", "#great"], "Теги должны быть в нижнем регистре с символом #."))
    r2 = run_test_case("Лишние пробелы и пустота", lambda: check(module.create_hashtags("  a   b  ") == ["#a", "#b"] and module.create_hashtags("") == [], "Функция ломается на пустой строке или нескольких пробелах."))
    if r1 and r2:
        score += 1

    print("\nТестирование filter_prices:")
    r3 = run_test_case("Успешная фильтрация", lambda: check(module.filter_prices([10, 50, 100], 50) == [10], "В список попадают цены >= лимита."))
    r4 = run_test_case("Отсутствие подходящих", lambda: check(module.filter_prices([100, 200], 50) == [], "Если подходящих цен нет, должен возвращаться пустой список."))
    if r3 and r4:
        score += 1

    print("\nТестирование cleanup_users:")
    r5 = run_test_case("Очистка и дубликаты", lambda: check(sorted(module.cleanup_users([" ivan ", "iVaN", "anna"])) == ["Anna", "Ivan"], "Не удаляются дубликаты (в разном регистре) или не очищаются пробелы."))
    if r5:
        score += 1

    print("\nТестирование convert_grades:")
    r6 = run_test_case("Полный набор оценок", lambda: check(module.convert_grades([5, 5, 4, 3, 2]) == {"Отлично": 2, "Хорошо": 1, "Удовл": 1, "Неуд": 1}, "Неверный подсчет словаря. Проверьте строковые ключи."))
    if r6:
        score += 1

    print("\nТестирование find_phone:")
    r7 = run_test_case("Поиск (успех/провал)", lambda: check(module.find_phone({"A":"1"}, "A") == "1" and module.find_phone({"A":"1"}, "B") == "Не найдено", "ОШИБКА: Функция не возвращает 'Не найдено' при отсутствии ключа."))
    if r7:
        score += 1

    return score

def test_middle():
    print(f"\n{BLUE}=== Запуск тестов БЛОК 2 (Middle) ==={RESET}")
    score = 0
    funcs = ['merge_stocks', 'analyze_text', 'get_top_students', 'check_password_strength', 'group_by_age']
    module = check_module('middle', funcs)
    if not module:
        return 0

    print("\nТестирование merge_stocks:")
    r1 = run_test_case("Слияние и суммирование", lambda: check(module.merge_stocks({"a":1}, {"a":2, "b":1}) == {"a":3, "b":1}, "Товары не суммируются или теряются уникальные ключи."))
    r2 = run_test_case("С пустым складом", lambda: check(module.merge_stocks({"a":1}, {}) == {"a":1}, "Ломается, если один из складов пуст."))
    if r1 and r2:
        score += 3

    print("\nТестирование analyze_text:")
    r3 = run_test_case("Пунктуация и регистр", lambda: check(module.analyze_text("Привет, мир! Привет...") == {"привет": 2, "мир": 1}, "Слова считаются некорректно. Забыли удалить '!' или ',' или перевести в нижний регистр."))
    if r3:
        score += 3

    print("\nТестирование get_top_students:")
    # Передаем 4 студентов. D - лучший(5), B - (4.5), A - (4), C - худший(3)
    log = [{'name': 'A', 'scores': [4]}, {'name': 'B', 'scores': [4, 5]}, {'name': 'C', 'scores': [3]}, {'name': 'D', 'scores': [5]}]
    r4 = run_test_case("Сортировка и обрезка Топ-3", lambda: check(module.get_top_students(log) == ["D", "B", "A"], "Неверная сортировка (нужно от лучшего к худшему) или возвращается больше 3 студентов."))
    if r4: 
        score += 3

    print("\nТестирование check_password_strength:")
    # Проверяем ВСЕ негативные сценарии
    r5 = run_test_case("Надежный пароль", lambda: check(module.check_password_strength("Str0ng!Pass") is True, "Хороший пароль отклонен."))
    r6 = run_test_case("Короткий пароль", lambda: check(module.check_password_strength("S1!hort") is False, "Пропущен пароль < 8 символов."))
    r7 = run_test_case("Без спецсимвола", lambda: check(module.check_password_strength("Str0ngPass") is False, "Пропущен пароль без спецсимвола."))
    r8 = run_test_case("Без цифры", lambda: check(module.check_password_strength("Strong!Pass") is False, "Пропущен пароль без цифры."))
    r9 = run_test_case("Без заглавной", lambda: check(module.check_password_strength("str0ng!pass") is False, "Пропущен пароль без заглавной буквы."))
    if all([r5, r6, r7, r8, r9]):
        score += 3

    print("\nТестирование group_by_age:")
    r10 = run_test_case("Группировка", lambda: check(module.group_by_age([("A", 20), ("B", 20), ("C", 30)]) == {20: ["A", "B"], 30: ["C"]}, "Люди с одинаковым возрастом не группируются в один список."))
    if r10:
        score += 3

    return score

def test_project():
    print(f"\n{BLUE}=== Запуск тестов БЛОК 3 (Senior) ==={RESET}")
    score = 0
    funcs = ['add_task', 'complete_task', 'filter_tasks', 'delete_task']
    module = check_module('project', funcs)
    if not module:
        return 0

    task_list = []
    
    print("\nТестирование add_task (4 балла):")
    def test_add():
        module.add_task(task_list, "Тест 1", "Высокий")
        module.add_task(task_list, "Тест 2", "Низкий")
        module.add_task(task_list, "Тест 3") # По умолчанию должен быть Средний
        
        check(len(task_list) == 3, "Задачи не добавляются в список.")
        check('id' in task_list[0], "В словаре задачи отсутствует ключ 'id'.")
        check(len({t['id'] for t in task_list}) == 3, "ID задач не уникальны (генерируются одинаковые).")
        check(task_list[2].get('priority') == "Средний", "Не работает приоритет по умолчанию ('Средний').")
        check(task_list[0].get('is_done') is False, "Новая задача должна иметь статус is_done = False.")
        
    if run_test_case("Добавление нескольких задач", test_add): 
        score += 4

    if len(task_list) == 3:
        id_1 = task_list[0]['id']
        id_2 = task_list[1]['id']
        id_3 = task_list[2]['id']
        
        print("\nТестирование complete_task (2 балла):")
        def test_complete():
            module.complete_task(task_list, id_1)
            check(task_list[0]['is_done'] is True, "Статус is_done не изменился на True.")
            # Граничный случай: вызов с несуществующим ID
            try:
                module.complete_task(task_list, 9999)
            except Exception:
                check(False, "Функция падает с ошибкой при передаче несуществующего ID. Ожидался корректный выход.")
                
        if run_test_case("Выполнение задачи и защита от падения", test_complete): 
            score += 2

        print("\nТестирование filter_tasks (2 балла):")
        def test_filter():
            # На текущий момент id_1 выполнена, id_2 и id_3 активны.
            all_t = module.filter_tasks(task_list, "all")
            check(len(all_t) == 3, "Фильтр 'all' не вернул все задачи.")
            
            # Проверяем выполненные (допускаем варианты нейминга)
            comp_t = module.filter_tasks(task_list, "completed")
            if len(comp_t) != 1:
                comp_t = module.filter_tasks(task_list, "выполненные")
            check(len(comp_t) == 1, "Фильтр не умеет возвращать только выполненные задачи (ожидался статус 'completed' или 'выполненные').")
            
            # Проверяем активные
            act_t = module.filter_tasks(task_list, "active")
            if len(act_t) != 2:
                act_t = module.filter_tasks(task_list, "активные")
            check(len(act_t) == 2, "Фильтр не умеет возвращать только активные задачи (ожидался статус 'active' или 'активные').")

        if run_test_case("Граничные случаи фильтрации", test_filter): 
            score += 2

        print("\nТестирование delete_task (2 балла):")
        def test_delete():
            module.delete_task(task_list, id_2)
            check(len(task_list) == 2, "Задача не удалилась из списка.")
            check(all(t['id'] != id_2 for t in task_list), "Удалена неверная задача (перепутали ID и индекс?).")
            
            # Граничный случай: вызов с несуществующим ID
            try:
                module.delete_task(task_list, 9999)
            except Exception:
                check(False, "Функция падает с ошибкой при попытке удалить несуществующий ID. Ожидалась защита.")
                
        if run_test_case("Удаление задачи и защита от падения", test_delete): 
            score += 2
    else:
        print(f"  {YELLOW}[!] Остальные тесты пропущены из-за ошибки в add_task.{RESET}")

    return score

if __name__ == "__main__":
    j_score = test_junior()
    m_score = test_middle()
    p_score = test_project()
    total = j_score + m_score + p_score
    
    print(f"\n{GREEN}=== Тестирование завершено ==={RESET}")
    print(f"__SCORES_JSON__={json.dumps({'junior': j_score, 'middle': m_score, 'project': p_score, 'total': total})}")