IMG ?= citacloud/monitor-citacloud-exporter

VERSION=$(shell git describe --tags --match 'v*' --always --dirty)
GIT_COMMIT?=$(shell git rev-parse --short HEAD)

.PHONY: image-latest
image-latest:
	# Build image with latest stable
	docker buildx build -t $(IMG):latest --build-arg version=$(GIT_COMMIT) \
    		--platform linux/amd64,linux/arm64 . --push

.PHONY: image-version
image-version:
	[ -z `git status --porcelain` ] || (git --no-pager diff && exit 255)
	docker buildx build -t $(IMG):$(VERSION) --build-arg version=$(GIT_COMMIT) \
		--platform linux/amd64,linux/arm64 . --push