FROM python:3.9-slim AS base-stage

COPY pyproject.toml poetry.lock python-project-skeleton/

WORKDIR /python-project-skeleton

RUN python -m pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

FROM python:3.9-slim
COPY --from=base-stage /python-project-skeleton/ /python-project-skeleton/

WORKDIR /python-project-skeleton

ENV PATH="/python-project-skeleton/.venv/bin:$PATH"

CMD ["echo", "hello"]