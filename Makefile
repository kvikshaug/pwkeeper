.PHONY: publish
publish:
	python setup.py sdist bdist_egg upload --sign

.PHONY: clean
clean:
	python setup.py clean -a
