VERSION = 0.0.4

docker-test:
	docker build --target test-image -t telepot:$(VERSION)-test .
