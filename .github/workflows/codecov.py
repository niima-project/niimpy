name: Docs
on: [push, pull_request]
jobs:
  test:
    name: codecov
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version:
          - 3.8
    steps:
      - uses: actions/checkout@v2
      - name: Run tests and collect coverage
        run: |
          coverage run -m pytest
          coverage xml
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v2
