# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -aE 
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Servmon
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# DO NOT RUN THIS COMMAND UNLESS ABSOLUTELY NECESSARY, IT WILL ERASE ALL CHANGES
# OF RST FILES
rst:
	# Remove old common.rst
	rm -f common.rst
	# Build API docs for common module
	sphinx-apidoc -o . ../servmon/common
	# Build the entire document

html:
	# Build the document only
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
