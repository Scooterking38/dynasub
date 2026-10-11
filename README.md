# DynaSub

Inline `${var}` substitution via a custom codec.

## Architecture Overview

The `dynasub` repository is structured to provide an inline variable substitution mechanism using a custom Python codec. The core functionality is encapsulated within the `dynasub` package, which includes:

- **`init.py`**: Contains the implementation of the custom codec for `${var}` substitution.
- **`sitecustomize.py`**: Initializes the custom codec by importing the `dynasub` module.

The repository leverages Python's built-in `codecs` module to register and use the custom codec. The `pyproject.toml` file is used for project metadata and build configuration, ensuring compatibility with modern Python packaging standards.

## Tech Stack

- **Programming Language**: Python 3.8+
- **Build System**: setuptools
- **Codecs Module**: Python's built-in `codecs` module

## Getting Started / Setup Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/dynasub.git
   cd dynasub
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8 or higher installed. Then, install the project dependencies using pip:
   ```bash
   python -m pip install .
   ```

3. **Usage**:
   To use the custom codec in your Python scripts, ensure that `sitecustomize.py` is loaded during interpreter startup. This can be done by placing it in a directory listed in the `PYTHONSTARTUP` environment variable or by modifying the site-packages directory.

4. **Example**:
   Here's an example of how to use the custom codec in a Python script:

   ```python
   import codecs

   # Register the custom codec
   codecs.register(dynasub.search)

   # Open a file with the custom codec
   with open('example.txt', 'r', encoding='dynasub') as f:
       content = f.read()
       print(content)
   ```

   In `example.txt`, you can use `${var}` syntax for inline variable substitution.

5. **Testing**:
   To test the functionality, create a file named `test.txt` with the following content:

   ```plaintext
   #${var}
   var = "Hello, World!"
   print(var)
   ```

   Then, run the following Python script to see the output:

   ```python
   import codecs

   codecs.register(dynasub.search)

   with open('test.txt', 'r', encoding='dynasub') as f:
       content = f.read()
       exec(content)
   ```

   This should print `Hello, World!` to the console.

For more detailed information and advanced usage, refer to the inline comments in the source code.