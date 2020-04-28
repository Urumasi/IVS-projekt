# File: Makefile
# Author: OkayChamps, Marek Filip (xfilip46), FIT BUT
# Date: 2020-Apr-22
# Brief: IVS-project2-calculator
# Details: Makefile for the calculator. Uses general makefile rules.
#		   I encourage all contributors to adjust the makefile to their liking.

 # need extglob and dotglob for copying and removing
SHELL := /bin/bash -O extglob -O dotglob
python = python3

LOGINS   = xfilip46_xknesl02_xnorek01_xsalab00
ZIP_FILE = ../$(LOGINS).zip

DOCGEN 		   = sphinx-build
DOCFLAGS 	   = -b
DOC_FORMAT     = html
SOURCE_DOC_DIR = doc-source
OUTPUT_DOC_DIR = ../doc

TEST_FILE 	   = test_mathlib
INSTALLER_DIR  = ../installer
INSTALLER_DEB  = calcchamp.deb

.phony: all run test doc profile pack clean help installer install


all: reqs

run:
	@$(python) -m main

test:
	@$(python) -m unittest $(TEST_FILE)

doc: reqs
	$(DOCGEN) $(DOCFLAGS) $(DOC_FORMAT) $(SOURCE_DOC_DIR) $(OUTPUT_DOC_DIR)

profile:
	# TODO: profiling

reqs:
	pip3 install -r requirements.txt

# remove all the .pyc, .pyo files and pycache dir from curr dir
# remove doc folder and other nonessential folders
clean: cleaninstallsource
	@rm -rf $(INSTALLER_DIR)/!(source|$(INSTALLER_DEB))
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@rm -rf __pycache__ $(OUTPUT_DOC_DIR) $(ZIP_FILE)
	@echo Deleted all nonessential files.

cleaninstallsource:
	@rm -rf $(INSTALLER_DIR)/!(source)
	@rm -rf $(INSTALLER_DIR)/source/!(debian|data|setup.py)
	@rm -rf $(INSTALLER_DIR)/source/debian/!(control|rules|compat|changelog)

# creates the installer and cleans everything except .deb file
installer: debinstall cleaninstallsource
	@mv $(INSTALLER_DIR)/*.deb $(INSTALLER_DIR)/$(INSTALLER_DEB)
	@rm -rf $(INSTALLER_DIR)/!(source|$(INSTALLER_DEB))
	@echo Created $(INSTALLER_DEB) in installer folder.
# moves scripts from /src into installer folder
movescripts: main.py __init__.py mathlib.py calculator.py ui_calculator.py img
	@mkdir -p $(INSTALLER_DIR)/source/calcchamp
	@cp -r $^ $(INSTALLER_DIR)/source/calcchamp
# creates the installer
debinstall: movescripts
	@rm -rf $(INSTALLER_DIR)/!(source)
	cd $(INSTALLER_DIR)/source && debuild -d

# installs the package
install: installer
	sudo apt purge calcchamp
	sudo apt install $(INSTALLER_DIR)/$(INSTALLER_DEB)

pack: clean $(ZIP_FILE)
	@rm -rf ../repo ../$(LOGINS)
$(ZIP_FILE): packrepo doc installer
	cp -r ../repo/. ../$(LOGINS)/repo
	cp -r $(INSTALLER_DIR)/$(INSTALLER_DEB) ../$(LOGINS)/install
	cp -r $(OUTPUT_DOC_DIR)/. ../$(LOGINS)/doc
	zip -ur $@ ../$(LOGINS)
packrepo: clean
	rm -rf ../repo ../$(LOGINS)
	cd .. && mkdir -p repo && cp -r !(repo) repo
	mkdir -p ../$(LOGINS)/repo ../$(LOGINS)/install ../$(LOGINS)/doc

help:
	@echo "make all"
	@echo "    Installs the requirements packages from pip."
	@echo "make run"
	@echo "    Run the program."
	@echo "make test"
	@echo "    Run the mathematical library tests."
	@echo "make doc"
	@echo "    Generate the documentation."
	@echo "make profile"
	@echo "    Run program to compute the standard deviation for profiling."
	@echo "make installer"
	@echo "    Create a debian package in installer folder."
	@echo "make install"
	@echo "    Install the debian package with 'sudo apt install'."
	@echo "make pack"
	@echo "    Pack the project with essential files only."
	@echo "make clean"
	@echo "    Delete files that are not essential."
	@echo "make help"
	@echo "    Print out this help."
