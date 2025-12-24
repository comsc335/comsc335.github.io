.PHONY: build
build:
	jb build .

.PHONY: clean
clean:
	jb clean .

.PHONY: publish
publish:
	make build
	ghp-import -n -p -f _build/html

.PHONY: pdf
pdf:
	jb build . --builder pdfhtml