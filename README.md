# python-project-template
Quick starting point for a respectable Python project.

## Roadmap
- [x] Package management
- [x] Directory structure
- [x] Code formatting
- [x] Code linting
- [ ] Commit hooks
- [ ] Configuration
- [ ] Testing
- [ ] Structured logging
- [x] Minimal asyncio entrypoint
- [ ] GitHub Actions
- [ ] Usage guide

## Quick start

### Setup
1. Use [pyenv] to install and activate the latest Python 3.10.
2. Install [pipenv]: `pip install --user pipenv`
3. In the repository root execute `pipenv install`

### Run the app

```shell
./run.sh
```

### Run the tests

### Run the linters

```shell
./lint.sh
```


## What's inside?
- Package management using [pipenv].
- Code formatting using [Black](https://black.readthedocs.io).
- Code linting using [Flake8](https://flake8.pycqa.org).

[pyenv]: https://github.com/pyenv/pyenv
[pipenv]: https://pipenv.pypa.io/en/latest/