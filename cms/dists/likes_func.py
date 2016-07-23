## helper functions for visualizing component score prior likelihoods
## last updated: 07.21.16 vitti@broadinstitute.org

import matplotlib as mp 
mp.use('TkAgg') #set backend
import matplotlib.pyplot as plt
from random import choice
import os
#from likes_func import get_hists_bins #maybe?
"""def get_hist_bins(score,numBins):
	if score == "ihs":
		scorerange = [-4., 4.]
		ylims = [0, .25]
	elif score == "delihh":
		scorerange = [-2., 3.]
		ylims = [0, .25]
	elif score == "fst":
		scorerange = [-.05, 1.]#[-2., 4.5]
		ylims = [0, .25]
	elif score == "deldaf":
		scorerange = [-1., 1.]
		ylims = [0, .25]
	elif score == "xp":
		scorerange = [-3., 7.]
		ylims = [0, .25]
	binlen = (scorerange[1] - scorerange[0])/float(numBins-1)
	bins = [scorerange[0] + binlen * i for i in range(numBins)]
	return bins, scorerange, ylims"""

def read_likes_file(likesfilename):
	'''parses a file from e.g. write_hists_to_files'''
	starts, ends, vals = [], [], []
	openfile = open(likesfilename, 'r')
	for line in openfile:
		entries = line.split()
		start, end, val = [float(x) for x in entries]
		for item in ['start', 'end', 'val']:
			eval(item + "s").append(eval(item))
	openfile.close()
	return starts, ends, vals
def get_old_likes():
	likesloc = "/Users/vitti/Desktop/070916/likes/"
	scores = ['ihs', 'delihh', 'fst', 'xp', 'deldaf']
	pops = range(1,5)
	models = ['default_112115_825am', 'default_default_101715_12pm', 'gradient_101915_treebase_6_best', 'nulldefault', 'nulldefault_constantsize']
	dists = ['causal', 'linked', 'neut']
	likesdict = {}
	for model in models:
		for score in scores:
			for dist in dists:
				for pop in pops:
					likesfilename = likesloc + score + "_" + model + "_" + str(pop) + "_likes_" + dist + ".txt"
					assert os.path.isfile(likesfilename)
					#if not os.path.isfile(likesfilename):
					#	print("missing file: " + likesfilename)
					key = (model, score, dist, pop)
					starts, ends, vals = read_likes_file(likesfilename)
					likesdict[key] = [starts, ends, vals]
	return likesdict
def plot_likes(starts, ends, vals, ax):
	ax.scatter(starts, vals)
	plt.show()
	print("I did it!")
	return ax

def main(): #for debug
	old_likes = get_old_likes()
	starts, ends, vals = old_likes[('gradient_101915_treebase_6_best', 'delihh', 'causal', 1)]

	fig = plt.figure()
	ax = fig.add_subplot(111)
	plot_likes(starts, ends, vals, ax)
	fig.show()
main()