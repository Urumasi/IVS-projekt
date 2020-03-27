# @file Makefile
# @author Marek Filip (xfilip46), FIT BUT
# @date 27/Mar/2020
# @brief IVS-project2-calculator
# @details Makefile for the calculator. Tries to use general makefile rules.

.phony: all pack clean test doc run profile

LOGINS=xfilip46_xknesl02_xnorek01_xsalab00
ZIP_FILE = $(LOGINS).zip

.DEFAULT_GOAL := all

all:

test:
	@python -m 

pack: $(ZIP_FILE)
$(ZIP_FILE): plan src dokumentace.pdf skutecnost.txt hodnoceni.txt
	zip -r $@ $^

clean:
	@rm -r __pycache__
	

doc:
	pydoc -w ../src

run:
	@python -m main

profile:

help:
	@echo "make all"
	@echo "    Translate the project including the profiling program."
	@echo "make pack"
	@echo "    Pack the project with essential files only."
	@echo "make clean"
	@echo "    Clean the files are not essential."
	@echo "make test"
	@echo "    Run the mathematical library tests."
	@echo "make doc"
	@echo "    Generate the documentation."
	@echo "make run"
	@echo "    Run the program."
	@echo "make profile"
	@echo "    Run translation of program to compute the standard deviation \
	for profiling."
	@echo "make help"
	@echo "    Print out this help."
	@echo $(PYTHON)
