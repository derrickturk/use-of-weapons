%.html: %.md
	pandoc --from markdown_github --to html $< --output $@

%.md: %.smd
	python shorthand.py $< >$@
