DOCKER_IMAGE_NAME = gpt-proxy-sever
DOCKER_IMAGE_TAG = 0.0.1

build:
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) .

run:
	docker run -it --rm --env-file .env -p 8080:8080 $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)

deploy:
	docker ps -q --filter "name=$(DOCKER_IMAGE_NAME)" | xargs -r docker rm -f
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) .
	docker run -it --rm -d --env-file .env -p 8080:8080 --name $(DOCKER_IMAGE_NAME) $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
