# Flowchart — Attendance Recovery Computation

This flowchart follows the input checks and consecutive-attendance loop in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[/Enter attended, conducted and target percentage/]
    B --> C{Inputs valid?}
    C -- No --> D[Display invalid input]
    D --> Z([End])
    C -- Yes --> E{Conducted classes equal zero?}
    E -- Yes --> F[Display no classes conducted]
    F --> Z
    E -- No --> G[Calculate current attendance percentage]
    G --> H{Current percentage meets target?}
    H -- Yes --> I[Display requirement already met]
    H -- No --> J[Set extra classes to zero]
    J --> K{Projected percentage meets target?}
    K -- No --> L[Increase extra classes by one]
    L --> K
    K -- Yes --> M[Display minimum extra classes]
    I --> Z
    M --> Z
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
