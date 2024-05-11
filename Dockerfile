FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    flake8 \
    mutmut \
    mypy \
    pandas-stubs \
    pylint \
    pytest \
    pytest-cov \
    types-requests
