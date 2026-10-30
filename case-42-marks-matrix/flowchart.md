# Flowchart — Student Marks Matrix Analysis

This flowchart follows the matrix input, row/column calculations, and top-performer search in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[Initialize students, subjects and empty marks matrix]
    B --> C[/Enter mark for each student and subject/]
    C --> D{Mark between 0 and 100?}
    D -- No --> E[Display invalid mark]
    E --> Z([End])
    D -- Yes --> F[Store mark in matrix]
    F --> G{More marks to enter?}
    G -- Yes --> C
    G -- No --> H[Calculate each student's total and average]
    H --> I[Calculate each subject's column average]
    I --> J[Find student with highest total]
    J --> K[Display totals, averages and top performer]
    K --> Z
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
