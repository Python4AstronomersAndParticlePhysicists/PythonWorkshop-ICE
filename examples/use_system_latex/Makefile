texopts = --lualatex \
	  --output-directory=build \
	  --halt-on-error \
	  --interaction=nonstopmode


all: build/proceeding.pdf


build/proceeding.pdf: FORCE build/plot.pdf
	latexmk $(texopts) proceeding.tex

build/plot.pdf: matplotlibrc matplotlib_header.tex settings.tex plot.py | build
	# matplotlib runs latex in /tmp, so we need to add the 
	# current working directory to the TEXINPUTS, so LaTeX can find 
	# our header file
	TEXINPUTS=$(shell pwd): python plot.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: clean all FORCE
