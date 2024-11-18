## Getting Started

### Prerequisites

- **Python 3.6+**
- **Virtual Environment** (optional but recommended)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/jonathanpmelian/static-site-generator.git
   cd static-site-generator
   ```

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux
   ```

3. **Install the Package**:

   ```bash
   pip install -e .
   ```

   This will install the package in editable mode and make the `ssg` command available globally within the virtual environment.

4. **Verify the Installation**:

   ```bash
   ssg --help
   ```

   You should see a list of available commands.

## Configuration

### Dependencies

Dependencies are listed in `requirements.txt` and are installed automatically when the package is installed. You can also install them manually with:

```bash
pip install -r requirements.txt
```

## Development

### Running Tests

Tests are written with `pytest`. To run tests:

```bash
pytest
```

You're now ready to create your first project! See [Usage](docs/usage.md) for details.
