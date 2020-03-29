# @file Makefile
# @author Okaychamps, Marek Filip (xfilip46), FIT BUT
# @date 29/Mar/2020
# @brief IVS-project2-calculator
# @details Makefile for the calculator. Tries to use general makefile rules.
#		   I encourage all contributors to adjust the makefile to their liking.

SHELL:=/bin/bash -O extglob  # need extglob for copying into subdirectory
.DEFAULT_GOAL := all  # set default goal to all
LOGINS = xfilip46_xknesl02_xnorek01_xsalab00
ZIP_FILE = $(LOGINS).zip
DOCGEN = pydoc
DOCFLAGS = -w
DOC_DIR = doc

.phony: all run test doc profile pack clean help

all:
	# TODO: profiling

run:
	@python -m main

test:
	@python -m 

doc:
	@$(DOCGEN) $(DOCFLAGS) ../src
	@mv *.html ../doc/
	@echo 'Documentation building finished. HTML files are in "doc/".'

profile:
	# TODO: profiling

pack: $(ZIP_FILE)
$(ZIP_FILE):
	make clean && make doc && cd .. && rm -rf repo
	cd .. && mkdir repo && cp -r !(repo) repo
	cd .. && zip -ur $@ doc/ install/ repo/ && rm -rf repo
	echo $(CURDIR)

# remove all the .pyc, .pyo files and pycache dir from curr dir
clean: 
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@rm -rf __pycache__

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
