# Sorting Algorithms in Python

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Repo Size](https://img.shields.io/github/repo-size/VioletSoul/SortMethods)
![Code Size](https://img.shields.io/github/languages/code-size/VioletSoul/SortMethods)
[![Stars](https://img.shields.io/github/stars/VioletSoul/SortMethods.svg?style=social)](https://github.com/VioletSoul/SortMethods)
[![Last Commit](https://img.shields.io/github/last-commit/VioletSoul/SortMethods.svg)](https://github.com/VioletSoul/SortMethods/commits/main)

---

## 📚 Description

**This repository contains a collection of classical and modern sorting algorithms implemented in Python.**  
Each algorithm comes with a brief description and usage example.  
Suitable for learning, interviews, and quick integration into your projects.

---

## 🚀 Implemented Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Cocktail Sort
- Comb Sort
- Counting Sort
- Radix Sort
- Shell Sort
- Binary Insertion Sort
- Timsort (built-in in Python: `sorted()` and `list.sort()`)

---

## 📦 How to Use

1. Clone the repository:
    ```
    git clone https://github.com/VioletSoul/SortMethods.git
    ```
2. Import the required algorithm into your project or explore the examples in the files.

---

## 🏷️ Algorithms Overview

| Algorithm             | Avg. Complexity | Stable | Description                                             |
|-----------------------|:---------------:|:------:|--------------------------------------------------------|
| Bubble Sort           | O(n²)           | ✅     | Simple, educational, rarely used in practice           |
| Selection Sort        | O(n²)           | ❌     | Minimum swaps, not stable                              |
| Insertion Sort        | O(n²)           | ✅     | Good for nearly sorted arrays                          |
| Merge Sort            | O(n log n)      | ✅     | Divide and merge, requires extra memory                |
| Quick Sort            | O(n log n)      | ❌     | Fast, but not stable                                   |
| Heap Sort             | O(n log n)      | ❌     | Heap-based, not stable                                 |
| Cocktail Sort         | O(n²)           | ✅     | Improved bubble sort, bidirectional                    |
| Comb Sort             | O(n²)           | ❌     | Faster than bubble, reduces "turtles"                  |
| Counting Sort         | O(n + k)        | ✅     | For integers in a limited range                        |
| Radix Sort            | O(nk)           | ✅     | Digit by digit, for numbers/strings                    |
| Shell Sort            | O(n log n)      | ❌     | Improved insertion, depends on gap sequence            |
| Binary Insertion Sort | O(n²)           | ✅     | Insertion with binary search                           |
| Timsort               | O(n log n)      | ✅     | Python built-in, hybrid algorithm                      |

---

## 💡 Notes

- For most tasks, it is recommended to use Python's built-in methods: `sorted()` and `list.sort()`, which implement Timsort.
- The implementations are for educational purposes and may not be optimal for large datasets.
- All examples are tested on Python 3.7+.

---

## 📄 License

This project is distributed under the MIT License.

---

## ⭐️ Support

If you found this repository useful — please star ⭐️ and fork it!

---

## 🤝 Contacts

- GitHub: [VioletSoul](https://github.com/VioletSoul)
- GitHub Issues: [Ask a question](https://github.com/VioletSoul/SortMethods/issues)

---
