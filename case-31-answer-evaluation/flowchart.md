# Flowchart — String-Based Examination Answer Evaluation

This flowchart follows the answer comparison and negative-marking logic in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[/Enter answer key and student answers/]
    B --> C[Remove spaces and convert to uppercase]
    C --> D{Same non-zero length?}
    D -- No --> E[Display input error]
    E --> Z([End])
    D -- Yes --> F[Initialize counts and score]
    F --> G[Compare next answer position]
    G --> H{Answer is blank marker?}
    H -- Yes --> I[Increase unanswered count]
    H -- No --> J{Answer matches key?}
    J -- Yes --> K[Increase correct count and add 1]
    J -- No --> L[Increase incorrect count and subtract 0.25]
    I --> M{More positions?}
    K --> M
    L --> M
    M -- Yes --> G
    M -- No --> N[Display counts and final score]
    N --> Z
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
