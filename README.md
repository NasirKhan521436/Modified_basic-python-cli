*Company*: CODTECH IT SOLUTIONS
*NAME*:  NASIR HUSSAIN KHAN
*INTERN ID*: CT12WE82
*DOMAIN*: Software Development
*Duration*: 12 weeks
*Mentor*: NEELA SANTOSH
## INTERNSHIP TASK 4:  CODE REFACTORING AND PERFORMANCE OPTIMIZATION
# Modified Basic Python CLI
A minimal Python Command Line Interface (CLI) tool to calculate the size of a given file in megabytes (MB), built without external CLI frameworks. Includes basic testing with `pytest`.

## 🛠 Features

- Pure Python CLI (no external CLI frameworks)
- Simple usage: Pass a file path as an argument
- Includes a help message for empty input
- Unit tested with `pytest`

## 📦 Requirements

- Python 3.6+
- [pytest](https://docs.pytest.org/) (for testing)

Install `pytest`:

```bash
pip install pytest
```

## 🚀 Usage

From the terminal:

```bash
python cli.py yourfile.txt
```

Example output:

```
3 MB
```

If no argument is passed:

```bash
python cli.py
```

Output:

```
This is a CLI tool that calculates file sizes
and it takes a single argument
```

## ✅ Running Tests

Run tests with `pytest`:

```bash
python -m pytest -v
```

Or (if pytest is in your PATH):

```bash
pytest -v
```

## 📺 Video Tutorial (Original Version)

[![Build a simple CLI in Python tutorial](https://img.youtube.com/vi/DrmdOb-EEMw/0.jpg)](https://youtu.be/DrmdOb-EEMw "Build a simple CLI in Python")

## 🔄 Next Steps

Now that you have a working CLI:
- Try extending it using `argparse` or `Click`
- Add more features (e.g., show size in KB or GB)
- Package it with `setuptools` for pip installation

Explore:
- [argparse CLI example](https://github.com/alfredodeza/argparse-python-cli)
- [Click framework CLI example](https://github.com/alfredodeza/click-python-cli)
