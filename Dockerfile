FROM python:3.9-slim AS base-stage

COPY pyproject.toml poetry.lock yaml-searcher/

WORKDIR /yaml-searcher

RUN python -m pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

FROM python:3.9-slim
COPY --from=base-stage /yaml-searcher/ /yaml-searcher/

WORKDIR /yaml-searcher

ENV PATH="/yaml-searcher/.venv/bin:$PATH"

CMD ["echo", "hello"]