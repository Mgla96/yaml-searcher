PROJECT_NAME := yaml-searcher

CONTAINER_REGISTRY := localhost:8080
IMAGE_NAME := yaml-searcher
IMAGE_TAG := 0.1.0

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
	shiv . -e yaml-searcher/yaml_searcher:main -o yamlsearcher