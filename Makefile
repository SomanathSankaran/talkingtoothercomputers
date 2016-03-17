all: slides post
slides: talkingtoothercomputers.slides.html
post: talkingtoothercomputers.slides.html
talkingtoothercomputers.slides.html: talkingtoothercomputers.ipynb
	jupyter nbconvert talkingtoothercomputers --to slides
talkingtoothercomputers.html: talkingtoothercomputers.ipynb
	jupyter nbconvert --to html talkingtoothercomputers.ipynb
present: talkingtoothercomputers.slides.html
	python -c 'import webbrowser; webbrowser.open("http://localhost:8000/talkingtoothercomputers.slides.html#/")' & python -m SimpleHTTPServer
