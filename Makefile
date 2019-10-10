SLEEP:=1

read:
	@chmod 777 read.sh
	@./read.sh

main: chmod_mode
	for text in $$(ls *txt); do ./determinitzacio.py < $$text; done

automat3: determinitzacio.py chmod_mode
	./determinitzacio.py < automat3.txt

automat2: determinitzacio.py chmod_mode
	./determinitzacio.py < automat2.txt

automat1: determinitzacio.py chmod_mode
	./determinitzacio.py < automat1.txt

chmod_mode: determinitzacio.py
	@chmod 777 determinitzacio.py
