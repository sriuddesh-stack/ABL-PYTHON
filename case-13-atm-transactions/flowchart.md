# Flowchart — ATM Transaction Sequence Simulation

This flowchart follows the deposit, withdrawal, and rejection logic in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[/Enter opening balance/]
    B --> C{Opening balance negative?}
    C -- Yes --> D[Display error]
    D --> Z([End])
    C -- No --> E[/Enter transaction sequence/]
    E --> F{Number of tokens even?}
    F -- No --> G[Display invalid sequence]
    G --> Z
    F -- Yes --> H[Read next transaction type and amount]
    H --> I{Amount numeric and positive?}
    I -- No --> J[Reject transaction]
    I -- Yes --> K{Type is deposit D?}
    K -- Yes --> L[Add amount to balance]
    K -- No --> M{Type is withdrawal W?}
    M -- No --> J
    M -- Yes --> N{Amount within balance and Rs. 10000 limit?}
    N -- Yes --> O[Subtract amount from balance]
    N -- No --> J
    L --> P{More transactions?}
    O --> P
    J --> P
    P -- Yes --> H
    P -- No --> Q[Display balance and accepted/rejected counts]
    Q --> Z
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
