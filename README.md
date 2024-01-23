# Решение домашнего задания по теме «Import. Module. Package»

1. **Структура** программы «Бухгалтерия» состоит из файлов:
- `./main.py`;  
- `./application/salary.py`;  
- `./application/db/people.py`.

Main.py — основной модуль для запуска программы. При вызове функций модуля main.py выводится текущая дата.  
В модуле salary.py хранится функция calculate_salary.  
В модуле people.py - функция get_employees.  

2. В файле `./requirements.txt` указан пакет [beautiful-console](https://pypi.org/project/beautiful-console/) в актуальной версии. 

3. Рядом с файлом main.py создан модуль `./dirty_main.py`, в который импортированы все функции модуля main.py.