# Flowchart — Examination Result and Grace-Mark Validation

This flowchart follows the validation, grace-mark limit, and result logic in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[Set subjects, pass mark 35 and grace limit 5]
    B --> C[/Enter marks for each subject/]
    C --> D{Any mark outside 0–100?}
    D -- Yes --> E[Display invalid mark]
    E --> Z([End])
    D -- No --> F[Set grace used to zero]
    F --> G[Check each subject mark]
    G --> H{Below pass mark by 5 or less and grace limit available?}
    H -- Yes --> I[Add required grace marks]
    H -- No --> J[Keep original mark]
    I --> K{More subjects?}
    J --> K
    K -- Yes --> G
    K -- No --> L{All final marks at least 35?}
    L -- Yes --> M[Display PASS]
    L -- No --> N[Display FAIL]
    M --> O[Display final marks and grace used]
    N --> O
    O --> Z
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
