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

DOCGEN 		   = python3 -msphinx
DOCFLAGS 	   = -b
DOC_FORMAT     = html
SOURCE_DOC_DIR = doc-source
OUTPUT_DOC_DIR = ../doc

TEST_FILE 	   = test_mathlib
INSTALLER_DIR  = ../installer
INSTALLER_DEB  = calcchamp.deb
DEV_PACKAGES   = devscripts debhelper python3-all python3-setuptools dh-python

.phony: all run test doc profile pack clean help installer install uninstall


all: reqs

run:
	@$(python) -m main

test:
	@$(python) -m unittest $(TEST_FILE)

# build documentation, install sphinx dependencies if build fails
doc:
	@make builddoc || { make reqs; make builddoc; }
builddoc:
	$(DOCGEN) $(DOCFLAGS) $(DOC_FORMAT) $(SOURCE_DOC_DIR) $(OUTPUT_DOC_DIR)

profile:
	# TODO: profiling

reqs:
	pip3 install -r requirements.txt

# remove all the .pyc, .pyo files and pycache dir from curr dir
# remove doc folder and all other nonessential folders
clean: cleaninstallsource
	@rm -rf $(INSTALLER_DIR)/!(source)
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@rm -rf __pycache__ $(OUTPUT_DOC_DIR) $(ZIP_FILE)
	@echo Deleted all nonessential files.

cleaninstallsource:
	@rm -rf $(INSTALLER_DIR)/!(source|$(INSTALLER_DEB))
	@rm -rf $(INSTALLER_DIR)/source/!(debian|data|setup.py)
	@rm -rf $(INSTALLER_DIR)/source/debian/\
	!(control|rules|compat|changelog|postinst)

# creates the installer and cleans everything except .deb file
# if debuild fails, fetches the appropriate dev packages
installer: debinstall cleaninstallsource
	@echo Created $(INSTALLER_DEB) in installer folder.
# moves scripts from /src into installer folder
movescripts: main.py __init__.py mathlib.py calculator.py ui_calculator.py img
	mkdir -p $(INSTALLER_DIR)/source/calcchamp
	cp -r $^ $(INSTALLER_DIR)/source/calcchamp
# creates the installer
debinstall: movescripts
	rm -rf $(INSTALLER_DIR)/!(source)
	make dodebuild || { make devpackages; make dodebuild; }
	mv $(INSTALLER_DIR)/*.deb $(INSTALLER_DIR)/$(INSTALLER_DEB)
# install the dev packages if debuild fails
dodebuild:
	cd $(INSTALLER_DIR)/source && debuild -d
devpackages:
	@sudo apt install $(DEV_PACKAGES)

# installs the package, creates the package if package is not created
install: uninstall
	@make installdeb || { make installer; make installdeb; }
installdeb:
	@sudo apt -y install $(INSTALLER_DIR)/$(INSTALLER_DEB) 2>/dev/null

uninstall:
	@sudo apt -y purge calcchamp 2>/dev/null || echo "calcchamp not installed."

pack: clean $(ZIP_FILE)
	@rm -rf ../repo ../$(LOGINS)
$(ZIP_FILE): packrepo doc installer
	cp -r ../repo/. ../$(LOGINS)/repo
	cp -r $(INSTALLER_DIR)/$(INSTALLER_DEB) ../$(LOGINS)/install
	cp -r $(OUTPUT_DOC_DIR)/. ../$(LOGINS)/doc
	zip -ur $@ ../$(LOGINS)
packrepo: clean
	@rm -rf ../repo ../$(LOGINS)
	cd .. && mkdir -p repo && cp -r !(repo) repo
	mkdir -p ../$(LOGINS)/repo ../$(LOGINS)/install ../$(LOGINS)/doc

help:
	@echo "make"
	@echo "	   Executes 'make all' command."
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
	@echo "    Install the debian package. If no package found build it."
	@echo "make uninstall"
	@echo "    Uninstall the debian package calcchamp."
	@echo "make pack"
	@echo "    Pack the project with essential files only."
	@echo "make clean"
	@echo "    Delete files that are not essential."
	@echo "make help"
	@echo "    Print out this help."
