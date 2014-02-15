MANAGE_PY = python manage.py
ROOT_DIR = fkzauth

MANAGE_OPTIONS = --noinput --traceback
RUN_OPTIONS = --traceback

# Please, keep the help message up to date concerning new commands

define helpmsg
Makefile command help

The following commands are available

- Running:
	run:			Start a development server on http://127.0.0.1:8000
	shell:			Start a development python shell on the current database

- Preparation & compilation
	makemsg: 		Update all .po files (to be manually updated)
	compilemsg:		Rebuild .mo files
	static:			Collect static files
	prepare:		Perform all required preparation steps

- Database:
	resetdb:		Reinitialize the database
	migratedb:		Migrates the database (using South)

- Misc:
	clean:			Cleanup all temporary files (*.pyc, ...)
	help:			Display this helpmessage
endef

default: help

all: prepare

help:
	@echo -n "" #Don't display extra lines
	$(info $(helpmsg))

.PHONY: all default help

# Running
# =======

run: static compilemsg
	$(MANAGE_PY) runserver $(RUN_OPTIONS) 8000

shell:
	$(MANAGE_PY) shell

.PHONY: run shell

# Preparation & compilation
# =========================

static:
	$(MANAGE_PY) collectstatic $(MANAGE_OPTIONS) --verbosity=0

makemsg:
	cd $(ROOT_DIR) && django-admin.py makemessages --all --no-wrap

PO_FILES = $(shell find $(ROOT_DIR) -name '*.po')
MO_FILES = $(PO_FILES:.po=.mo)

compilemsg: $(MO_FILES)

%.mo: %.po
	msgfmt --check-format -o $@ $<

prepare: compilemsg static

.PHONY: compilemsg makemsg prepare static

# Database
# ========

resetdb:
	rm -f db.sqlite3
	$(MANAGE_PY) syncdb $(MANAGE_OPTIONS) --migrate

migratedb:
	$(MANAGE_PY) migrate $(MANAGE_OPTIONS) --merge

.PHONY: resetdb migratedb

# Misc
# ====

clean:
	find . "(" -name "*.pyc" -or -name "*.pyo" -or -name "*.mo" ")" -delete

.PHONY: clean
