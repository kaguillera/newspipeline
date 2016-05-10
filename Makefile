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

    
all: clean install
	source ./env/bin/activate; \
	npm start; \        

serve:
	python serve.py

clean:
	rm -rf env
	rm -rf dist
	find . -name \*.pyc -delete
