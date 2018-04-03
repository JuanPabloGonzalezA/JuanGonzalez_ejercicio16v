grafica.png : grafica.py datos.txt
	python grafica.py
datos.txt : album
	./album > datos.txt
album : album.cpp
	c++ album.cpp -o 'album'

