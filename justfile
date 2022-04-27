@_default:
    just --list

@build:
    python -m build

@check:
    twine check dist/*

@fmt:
    just --fmt --unstable

@lint:
    # black .
    # blacken-docs ./README.rst
    just pre-commit

@pip-compile:
    pip-compile -r ./requirements.in

@pre-commit:
    git ls-files -- . | xargs pre-commit run --config=.pre-commit-config.yaml --files

@test:
    pytest

@upload:
    twine upload dist/*
