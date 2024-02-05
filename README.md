# Assignment MZ370P19 Introduction to Programming

This is a repository for assignment for course
[Introduction to Programming][1] on Faculty of Science, Charles University
Prague.

The histogram generator code requires additional libraries that need
installing. Due to [PEP 405][2] it is recommended to install these
additional libraries in an virtual environment. Here is a short How To:

## Requirements

### Clone the repository and create virtual environment

```python
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries inside the virtual environment

```python
python3 -m pip install -r requirements.txt
```

To exit the virtual environment use this

```
deactivate
```

[1]: <http://web.natur.cuni.cz/~bayertom/index.php/teaching/uvod-do-programovani>
[2]: <https://peps.python.org/pep-0405/>
