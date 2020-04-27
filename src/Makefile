# File: Makefile
# Author: OkayChamps, Marek Filip (xfilip46), FIT BUT
# Date: 2020-Apr-22
# Brief: IVS-project2-calculator
# Details: Makefile for the calculator. Tries to use general makefile rules.
#		   I encourage all contributors to adjust the makefile to their liking.

SHELL:=/bin/bash -O extglob  # need extglob for copying into subdirectory
.DEFAULT_GOAL := all  # set default goal to all
LOGINS = xfilip46_xknesl02_xnorek01_xsalab00
ZIP_FILE = $(LOGINS).zip
python = python3
TEST_FILES = test_mathlib
DOCGEN = pydoc
DOCFLAGS = -w
INSTALLER_DIR  = ../installer
SOURCE_DOC_DIR = doc-source
OUTPUT_DOC_DIR = ../doc
DOC_FORMAT     = html

.phony: all run test doc profile pack clean help

all:
	# TODO: profiling

run:
	@$(python) -m main

test:
	@$(python) -m unittest $(TEST_FILES)

doc:
	@sphinx-build -b $(DOC_FORMAT) $(SOURCE_DOC_DIR) $(OUTPUT_DOC_DIR)

profile:
	# TODO: profiling

pack: $(ZIP_FILE)
$(ZIP_FILE):
	make clean && make doc && cd .. && rm -rf repo
	cd .. && mkdir repo && cp -r !(repo) repo
	cd .. && zip -ur $@ doc/ install/ repo/ && rm -rf repo
	echo $(CURDIR)

# remove all the .pyc, .pyo files and pycache dir from curr dir
# remove doc folder
clean:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@rm -rf __pycache__ $(OUTPUT_DOC_DIR)
	@rm -rf $(INSTALLER_DIR)/!(source)
	@rm -rf $(INSTALLER_DIR)/source/.pybuild
	@rm -rf $(INSTALLER_DIR)/source/!(debian|setup.py)
	@rm -rf $(INSTALLER_DIR)/source/debian/!(control|rules|compat|changelog)
	@echo Deleted all nonessential files.

help:
	@echo "make all"
	@echo "    Translate the project including the profiling program."
	@echo "make run"
	@echo "    Run the program."
	@echo "make test"
	@echo "    Run the mathematical library tests."
	@echo "make doc"
	@echo "    Generate the documentation."
	@echo "make profile"
	@echo "    Run translation of program to compute the standard deviation \
	for profiling."
	@echo "make pack"
	@echo "    Pack the project with essential files only."
	@echo "make clean"
	@echo "    Delete files that are not essential."
	@echo "make help"
	@echo "    Print out this help."

movescripts:
	@cd $(INSTALLER_DIR)/source && mkdir -p calcchamp
	@cp -r main.py __init__.py mathlib.py calculator.py ui_calculator.py \
		img/ $(INSTALLER_DIR)/source/calcchamp

# TODO: remove
zipinstaller: movescripts
	@zip -r ../installer.zip ../installer

installer: movescripts
	@cd $(INSTALLER_DIR)/source && debuild -d
