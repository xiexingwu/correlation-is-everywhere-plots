main:
	python 1_measure.py
	python 2_stocks.py
	python 3_wally.py #--compute # uncommet "--compute" to run the computation
	python 4_fft.py

# Crop Wally's head from the Where's Wally image
wally:
	convert data/wally.png -crop 20x20+1630+870 data/wally_ref.png
