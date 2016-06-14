env:
	virtualenv --prompt="[newspipeline] " env

	
install: env
	source ./env/bin/activate; \
	pip install -r requirements.txt; \


start:
	source ./env/bin/activate; \
	npm start; \        


build:
	source ./env/bin/activate; \
	npm build; \        

    
all: clean_all install
	source ./env/bin/activate; \
	npm start; \        

serve:
	source ./env/bin/activate; \
	python serve.py

clean_dist: 
	rm -rf dist

clean_all:
	rm -rf env
	rm -rf dist
	find . -name \*.pyc -delete
