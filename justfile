# check formatting (ruff)
formatcheck:
    uv run ruff format --check

# check types (mypy)
typecheck:
    uv run mypy --strict .

# run linter (ruff)
lint:
    uv run ruff check .
