FROM python:3.9-slim AS base-stage

COPY pyproject.toml poetry.lock yamlsearcher/

WORKDIR /yamlsearcher

RUN python -m pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

FROM python:3.9-slim
COPY --from=base-stage /yamlsearcher/ /yamlsearcher/
COPY . /yamlsearcher

WORKDIR /yamlsearcher

ENV PATH="/yamlsearcher/.venv/bin:$PATH"

CMD ["echo", "hello"]