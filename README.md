# Python CLI + PyTest Scaffold

A modern, production-ready template for building Python CLI applications with Click and PyTest.

## Features

-   **Click**: Robust framework for creating command-line interfaces.
-   **PyTest**: Feature-rich testing framework.
-   **Structure**: Best practices folder structure (`src`, `tests`).
-   **Setup**: Ready-to-go `setup.py` for pip installation.

## Getting Started

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/anunzio-international/python-cli-scaffold.git
    cd python-cli-scaffold
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -e .
    pip install -r requirements.txt
    ```

4.  **Run the CLI**:
    ```bash
    mycli --help
    ```

## Running Tests

```bash
pytest
```

## Project Structure

```
├── src/
│   └── mypackage/      # Source code
│       ├── __init__.py
│       └── cli.py      # Entry point
├── tests/              # Tests
│   ├── __init__.py
│   └── test_cli.py
├── setup.py            # Package setup
└── requirements.txt    # Dev dependencies
```

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
