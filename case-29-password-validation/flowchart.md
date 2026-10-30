# Flowchart — Password Policy Validation Engine

Use a made-up sample password for this classroom exercise, not a personal password.

```mermaid
flowchart TD
    A([Start]) --> B[/Enter sample password/]
    B --> C[Initialize validation flags and error list]
    C --> D[Scan each character]
    D --> E[Update lowercase, uppercase, digit or special flag]
    E --> F{More characters?}
    F -- Yes --> D
    F -- No --> G[Check minimum length]
    G --> H[Check all character-category flags]
    H --> I[Check prohibited word rule]
    I --> J{Any validation errors?}
    J -- Yes --> K[Display each failed rule]
    J -- No --> L[Display policy passed]
    K --> Z([End])
    L --> Z
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
