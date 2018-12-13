.DEFAULT_GOAL := help
help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

local-up:  ## runs a local instance
	docker-compose -f docker-compose-LocalExecutor.yml up --build

local-build:  ## builds a local instance
	docker-compose -f docker-compose-LocalExecutor.yml build

local-down: ## turns off a local instance
	docker-compose -f docker-compose-LocalExecutor.yml down

local-sh: ## executes bash on a local instance
	docker-compose -f docker-compose-LocalExecutor.yml run webserver sh

celery-up: ## runs a local instance using celerybuilds django docker image
	docker-compose -f docker-compose-CeleryExecutor.yml up

