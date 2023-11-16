init:
	if ! virtualenv --version; then pip install virtualenv; fi
	if [ ! -d venv ]; then virtualenv venv; fi

install:
	. venv/bin/activate; pip install -r requirements.txt

lint:
	./venv/bin/pylint app
