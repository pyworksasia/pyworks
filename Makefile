# Quick PyWorks CLI with Makefile
dir=${CURDIR}
app_dir="${CURDIR}/App"
db_dir="${CURDIR}/App/Database"
model_dir="${CURDIR}/App/Models"
env_path="${CURDIR}/App/.env"

# Export project to PYTHONPATH
export PYTHONPATH=$(dir)

# Read variables from .env file
include App/.env
VARS:=$(shell sed -ne 's/ *\#.*$$//; /./ s/=.*$$// p' $(app_dir)/.env )
$(foreach v,$(VARS),$(eval $(shell echo export $(v)="$($(v))")))

## Help
help:
	@cat makefile | grep "##." | sed '2d;s/##//;s/://'

cd:
	@cd $(app_dir)
## Database and Migration
model:
	@orator make:model $$name -p $(model_dir)

migrate:
	@orator migrate -p $(db_dir)/migrations -c $(db_dir)/db.py

migration:
	@orator make:migration -p $(db_dir)/migrations -c $(db_dir)/db.py

rollback:
	@orator migrate:rollback -p $(db_dir)/migrations  -c $(db_dir)/db.py

refresh:
	@orator migrate:refresh -p $(db_dir)/migrations --seed --seed-path $(db_dir)/seeds -c $(db_dir)/db.py

## Development
# venv: # Create venv if it doesn't exist
#     test -d venv-py3.7 || virtualenv -p python3.7 venv-py3.7

venv:
	@rm -rf ./venv-py3.7
	@virtualenv -p python3.7 venv-py3.7

install:
	@pip install -r requirements.in

require:
	@pip install $$name

start:
	@echo $(APP_NAME)
	@uvicorn App.main:app --reload --port $(APP_PORT)

# db-sync:		##Gets db from server and syncs it with local. Requires db_username, db_password, db_name
# 	@echo "Downloading development DB, trying to connect to server"
# 	@scp -P $(port) $(url):$(db_file) .
# 	@echo "Populating local DB, this may take a while"
# 	@mysql -u $(db_username) --password=$(db_password) $(db_name) < $(db_file)


# db-connect:	##Connects to local db
# 	@mysql -u $(db_username) -p$(db_password) $(db_name)

## Testing
test:
	pytest App/Tests
