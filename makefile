
run:
	python3 main.py

#https://stackoverflow.com/questions/24736146/how-to-use-virtualenv-in-makefile
#https://gist.github.com/jakubroztocil/7892597
clean:
	find . \
    	-name '__pycache__' -delete -print \
    	-o \
    	-name '*.pyc' -delete -print