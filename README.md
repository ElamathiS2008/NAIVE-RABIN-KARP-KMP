# Comparative Analysis of Naive, KMP, and Rabin-Karp Algorithms for String Matching

## Overview

This project implements and compares three popular string matching algorithms:

- Naive String Matching Algorithm
- Knuth-Morris-Pratt (KMP) Algorithm
- Rabin-Karp Algorithm

The program allows the user to enter a text string and a pattern string. It then searches for all occurrences of the pattern in the text using each algorithm and compares their performance based on the number of character comparisons.

---

## Objectives

- Implement the Naive, KMP, and Rabin-Karp algorithms.
- Find all occurrences of a pattern in a given text.
- Compare the efficiency of each algorithm.
- Understand the advantages and disadvantages of different string matching techniques.

---

## Features

- User-friendly input for text and pattern.
- Displays all matching positions.
- Counts the number of character comparisons.
- Compares the performance of all three algorithms.

---

## Algorithms Used

### 1. Naive String Matching

- Compares the pattern with every possible position in the text.
- Simple to implement.
- Time Complexity:
  - Best Case: O(n)
  - Worst Case: O(n × m)

### 2. Knuth-Morris-Pratt (KMP)

- Uses the Longest Prefix Suffix (LPS) array.
- Avoids unnecessary comparisons.
- Time Complexity:
  - Best Case: O(n + m)
  - Worst Case: O(n + m)

### 3. Rabin-Karp

- Uses hashing to compare the pattern with the text.
- Efficient for multiple pattern matching.
- Time Complexity:
  - Average Case: O(n + m)
  - Worst Case: O(n × m)

---

## Requirements

- Python 3.x
- Visual Studio Code (Recommended)

No external libraries are required.

---

## Project Structure

```
StringMatching/
│
├── task2.py
├── README.md
```

---

## How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python task2.py
```

or

```bash
py task2.py
```

4. Enter the text and pattern when prompted.

---

## Sample Input

```
Enter the Text    : AABAACAADAABAABA
Enter the Pattern : AABA
```

---

## Sample Output

```
Naive Algorithm
Match Positions : [0, 9, 12]
Comparisons     : 30

KMP Algorithm
Match Positions : [0, 9, 12]
Comparisons     : 18

Rabin-Karp Algorithm
Match Positions : [0, 9, 12]
Comparisons     : 12
```

---

## Comparison Table

| Algorithm | Time Complexity | Extra Space |
|-----------|-----------------|-------------|
| Naive | O(n × m) | O(1) |
| KMP | O(n + m) | O(m) |
| Rabin-Karp | O(n + m) Average | O(1) |

---

## Applications

- Text editors
- Search engines
- DNA sequence matching
- Plagiarism detection
- Spell checking
- Bioinformatics

---

## Advantages

### Naive
- Simple implementation
- No preprocessing required

### KMP
- Fast searching
- Eliminates redundant comparisons

### Rabin-Karp
- Efficient hashing technique
- Suitable for multiple pattern matching

---

## Conclusion

This project demonstrates the working of three string matching algorithms and compares their efficiency. The Naive algorithm is simple but slower for large inputs, KMP provides efficient linear-time searching using the LPS array, and Rabin-Karp uses hashing for faster average-case performance. This comparison helps understand the strengths and limitations of each algorithm in practical applications.

---

## Author

Name: ELAMATHI.S

Department: AI&DS

Course: Design and Analysis of Algorithms Laboratory
