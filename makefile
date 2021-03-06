# https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run
ifeq (run,$(firstword $(MAKECMDGOALS)))
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(RUN_ARGS):;@:)
endif

run:
	python3 main.py $(RUN_ARGS)

#https://stackoverflow.com/questions/24736146/how-to-use-virtualenv-in-makefile
#https://gist.github.com/jakubroztocil/7892597
clean:
	find . \
    	-name '__pycache__' -delete -print \
    	-o \
    	-name '*.pyc' -delete -print