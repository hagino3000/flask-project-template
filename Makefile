setup:
	virtualenv .
	./bin/pip install flask

run:
	./bin/python app/app.py
