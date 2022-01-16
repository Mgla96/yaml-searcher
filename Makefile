PROJECT_NAME := yamlsearcher

CONTAINER_REGISTRY := localhost:8080
IMAGE_NAME := yaml-searcher
IMAGE_TAG := 0.1.4

.PHONY: install
install:
	poetry install

.PHONY: black
black:
	poetry run python -m black ${PROJECT_NAME}/ tests/

.PHONY: lint
lint:
	poetry run python -m flake8 ${PROJECT_NAME}/

.PHONY: pylint
pylint:
	poetry run pylint ${PROJECT_NAME}

.PHONY: typecheck
typecheck:
	poetry run mypy ${PROJECT_NAME}

.PHONY: unittest
unittest:
	poetry run pytest

.PHONY: build
build:
	docker build -t ${CONTAINER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} .

.PHONY: push
push:
	docker push ${CONTAINER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}

.PHONY: shiv
shiv:
	shiv . -e yamlsearcher.yaml_searcher:main -o yaml-searcher
