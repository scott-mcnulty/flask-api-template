SHELL := /bin/bash

.PHONY: help
help:
	@echo "    clean"
	@echo "         Cleans local files/dirs made when running code/testing/etc."
	@echo "    test"
	@echo "         Tests the app locally using tox."
	@echo "    directory-tree"
	@echo "         Creates a new tree representation of the myapi directory."



.PHONY: clean
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf htmlcov || true;
	rm -f coverage.xml || true;
	rm -f .coverage || true;
	rm -f pytest-results.xml || true;


.PHONY: test
test: clean
	tox


.PNONY: directory-tree
directory-tree: clean
	cd myapi;\
	tree --prune;