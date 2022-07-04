install:
    poetry install

brain-games:
    poetry run brain-games

brain-even:
    poetry run brain-even

brain-calc:
    poetry run brain-calc

build:
    poetry build

publish:
    poetry publish --dry-run

package-install:
    python3 -m pip install --user dist/hexlet_code-0.2.0-py3-none-any.whl

lint:
    poetry run flake8 brain_games

inst: # added from github.com/A-V-tor/python-project-lvl1/blob/main/Makefile
    python3 -m pip install --upgrade --force-reinstall dist/hexlet_code-0.2.0-py3-none-any.whl

