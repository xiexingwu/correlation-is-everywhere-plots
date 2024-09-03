all: plot show

plot:
	# python 1_measure.py
	python 2_stocks.py

show:
	### Section 1
	# ls plots/1_*.png | xargs -n 1 wezterm imgcat
	# cat plots/1_4b.txt

	### Section 2
	ls plots/2_*.png | xargs -n 1 wezterm imgcat

walley:
	convert data/walley.png -crop 20x20+1630+870 data/walley_ref.png
