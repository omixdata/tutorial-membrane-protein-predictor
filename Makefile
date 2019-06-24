info:
	more README.md

install:
	apt install python3-pip
	pip3 install -r requirements.txt

download:
	bash scripts/download.sh

preprocess:
	python3 scripts/preprocess.py

train:
	python3 scripts/train.py

server:
	python3 scripts/server.py
