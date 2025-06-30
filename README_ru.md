# Sorting Algorithms in Python

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Repo Size](https://img.shields.io/github/repo-size/VioletSoul/SortMethods)
![Code Size](https://img.shields.io/github/languages/code-size/VioletSoul/SortMethods)
[![Stars](https://img.shields.io/github/stars/VioletSoul/SortMethods.svg?style=social)](https://github.com/VioletSoul/SortMethods)
[![Last Commit](https://img.shields.io/github/last-commit/VioletSoul/SortMethods.svg)](https://github.com/VioletSoul/SortMethods/commits/main)

---

## 📚 Описание

**Этот репозиторий содержит коллекцию классических и современных алгоритмов сортировки, реализованных на Python.**  
Каждый алгоритм снабжён кратким описанием и примером использования.  
Подойдёт для обучения, собеседований, а также для быстрой интеграции в проекты.

---

## 🚀 Список реализованных алгоритмов

- Пузырьковая сортировка (Bubble Sort)
- Сортировка выбором (Selection Sort)
- Сортировка вставками (Insertion Sort)
- Сортировка слиянием (Merge Sort)
- Быстрая сортировка (Quick Sort)
- Пирамидальная сортировка (Heap Sort)
- Шейкерная сортировка (Cocktail Sort)
- Сортировка расчёской (Comb Sort)
- Сортировка подсчётом (Counting Sort)
- Поразрядная сортировка (Radix Sort)
- Сортировка Шелла (Shell Sort)
- Сортировка вставками с двоичным поиском (Binary Insertion Sort)
- Timsort (встроенный в Python: `sorted()` и `list.sort()`)

---

## 📦 Как использовать

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/yourusername/sorting-algorithms.git
    ```
2. Импортируйте нужный алгоритм в свой проект или изучайте примеры в файлах.

---


---

## 🏷️ Описание алгоритмов

| Алгоритм                    | Сложность (средняя) | Стабильность | Описание                                      |
|-----------------------------|:------------------:|:------------:|-----------------------------------------------|
| Bubble Sort                 | O(n²)              | ✅           | Простой, обучающий, редко используется на практике |
| Selection Sort              | O(n²)              | ❌           | Минимум обменов, не стабилен                  |
| Insertion Sort              | O(n²)              | ✅           | Хорош для почти отсортированных массивов       |
| Merge Sort                  | O(n log n)         | ✅           | Делит и сливает, требует доп. память           |
| Quick Sort                  | O(n log n)         | ❌           | Быстрый, но не стабилен                        |
| Heap Sort                   | O(n log n)         | ❌           | На куче, не стабилен                           |
| Cocktail Sort               | O(n²)              | ✅           | Улучшенная пузырьковая, двунаправленная        |
| Comb Sort                   | O(n²)              | ❌           | Быстрее пузырьковой, уменьшает "черепах"       |
| Counting Sort               | O(n + k)           | ✅           | Для целых чисел ограниченного диапазона        |
| Radix Sort                  | O(nk)              | ✅           | Поразрядная, для чисел/строк                   |
| Shell Sort                  | O(n log n)         | ❌           | Улучшение вставками, зависит от шага           |
| Binary Insertion Sort       | O(n²)              | ✅           | Вставки с двоичным поиском                     |
| Timsort                     | O(n log n)         | ✅           | Встроенный в Python, гибридный                 |

---

## 💡 Примечания

- Для большинства задач рекомендуется использовать встроенные методы Python: `sorted()` и `list.sort()`, реализующие Timsort.
- Реализации написаны для образовательных целей и могут быть не оптимальны для больших данных.
- Все примеры протестированы на Python 3.7+.

---

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).

---

## ⭐️ Поддержите проект

Если репозиторий был полезен — поставьте ⭐️ и сделайте fork!

---

## 🤝 Контакты

- GitHub: [VioletSoul](https://github.com/VioletSoul)
- GitHub Issues: [Оставить вопрос](https://github.com/VioletSoul/SortMethods/issues)

---

