# python-project-template
Quick starting point for a respectable Python project.

## Roadmap
- [x] Package management
- [x] Directory structure
- [x] Code formatting
- [x] Code linting
- [ ] Commit hooks
- [x] Settings management
- [x] Testing
- [ ] Structured logging
- [x] Minimal asyncio entrypoint
- [ ] Usage guide

## Quick start

### Setup
1. Use [poetry] to install and activate the latest Python 3.10.
2. Install [poetry]: `pipx install poetry` (for other options consult the documentation).
3. In the repository root execute `poetry install`

### Run the app

```shell
./run.sh
```

### Run the tests
```shell
./test.sh
```

### Run the linters

```shell
./lint.sh
```


## What's inside?
- Package management using either [poetry] or [pipenv].
- Settings management using [dynaconf]. 
- Code formatting using [Black](https://black.readthedocs.io).
- Code linting using [Flake8](https://flake8.pycqa.org).
- Testing using [pytest](https://docs.pytest.org).

[pyenv]: https://github.com/pyenv/pyenv
[pipenv]: https://pipenv.pypa.io/en/latest/
[poetry]: https://python-poetry.org/
[dynaconf]: https://www.dynaconf.com/
