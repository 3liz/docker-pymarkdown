all: build push

build:
	@docker build -t 3liz/pymarkdown:latest .

push:
	@docker push 3liz/pymarkdown:latest
