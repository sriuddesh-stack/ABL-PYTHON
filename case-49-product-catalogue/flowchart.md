# Flowchart — Tuple-Based Product Catalogue Audit

This flowchart follows the tuple validation, inventory valuation, and low-stock check in `main.py`.

```mermaid
flowchart TD
    A([Start]) --> B[Load product tuples]
    B --> C[Set inventory total to zero]
    C --> D[Unpack next product tuple]
    D --> E{Price or stock negative?}
    E -- Yes --> F[Display invalid record]
    E -- No --> G[Calculate price multiplied by stock]
    G --> H[Add item value to inventory total]
    H --> I{Stock below 5?}
    I -- Yes --> J[Display replenishment warning]
    I -- No --> K{More products?}
    J --> K
    F --> K
    K -- Yes --> D
    K -- No --> L[Display valid inventory total]
    L --> Z([End])
```

**Key:** Oval = Start/End · Parallelogram = Input/Output · Diamond = Decision · Rectangle = Process
