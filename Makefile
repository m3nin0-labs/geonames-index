
.PHONY: files-* os-* help

files-download:  ## Download Geonames file
	./utilities/download-files.sh

os-start:  ## Start Opensearch using Docker
	docker compose up -d

os-down:  ## Remove Opensearch container
	docker compose down


os-logs:  ## View Opensearch logs
	docker compose logs -f --tail 10


os-mappings:  ## Create Geonames index
	cd mappings && \
		./geonames.sh

os-index:  ## Index Geonames index
	python \
		workflow/index-geonames.py

#
# Documentation function (thanks for https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html)
#
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
