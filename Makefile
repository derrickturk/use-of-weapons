CHAPTERS := $(patsubst %.smd,%.md,$(wildcard ch*.smd))

all: chapters

chapters: $(CHAPTERS)

%.md: %.smd
	python shorthand.py $< >$@

%.html: %.md
	pandoc --from markdown_github --to html $< --output $@
