# Flowchart — Student Performance Trend Analysis

This flowchart follows the previous/current marks comparison in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[Set subject names and empty marks lists]
    B --> C[/Enter previous marks for all subjects/]
    C --> D[/Enter current marks for all subjects/]
    D --> E[Select next subject]
    E --> F[Calculate current mark minus previous mark]
    F --> G{Change greater than zero?}
    G -- Yes --> H[Label Improved]
    G -- No --> I{Change less than zero?}
    I -- Yes --> J[Label Declined]
    I -- No --> K[Label No change]
    H --> L{More subjects?}
    J --> L
    K --> L
    L -- Yes --> E
    L -- No --> M[Find current marks below 40]
    M --> N[Display trends and subjects needing attention]
    N --> Z([End])
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
