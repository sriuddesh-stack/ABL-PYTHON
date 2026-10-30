# Flowchart — Weekly Electricity Consumption Matrix

This flowchart follows the appliance/day matrix input and row/column totals in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[Initialize appliance names, days and empty usage matrix]
    B --> C[/Enter daily units for next appliance/]
    C --> D{Reading negative?}
    D -- Yes --> E[Display invalid usage]
    E --> Z([End])
    D -- No --> F[Store reading]
    F --> G{More days for this appliance?}
    G -- Yes --> C
    G -- No --> H{More appliances?}
    H -- Yes --> C
    H -- No --> I[Calculate weekly total for each appliance]
    I --> J[Calculate total usage for each day]
    J --> K[Display weekly and daily totals]
    K --> Z
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
