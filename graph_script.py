#!/usr/bin/env python3
import sys
import os
from argparse import ArgumentParser

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

parser = ArgumentParser()
parser.add_argument(dest="filename", help="The input datafile", metavar="FILE")
parser.add_argument(dest="plottype",help="The type of plot")
parser.add_argument(dest="group", help="The groups that you would like to sort by.")
parser.add_argument(dest="dep", help="The dependent variable you wish to graph.")
parser.add_argument("-t","--title",dest="title", help="The title of your figure.")
parser.add_argument(dest="output", help="The desired output filename. Please include the extension.")
args = parser.parse_args()


data1 = pd.read_csv(args.filename, sep="\t", lineterminator="\n")

#print(data1.head())

def plot_v1(data,error,title):
	def set_style():
		plt.style.use('seaborn-paper')
		matplotlib.rc("font",family="serif")
	set_style()

	#Create the figure and axis objects that I'll plot on.
	fig, ax = plt.subplots()
	
	#plot the bars
	ax.bar(np.arange(len(data)),data,yerr=error,align="center",alpha=0.5,ecolor='black',capsize=2)
	
	#math to determine ylimit
	maxmean = max(data)
	maxstd = max(error)
	ylimval = (maxmean+maxstd)*1.1
	print(ylimval)
	#setting a nice y-axis limit
	ax.set_ylim(0,ylimval)

	#label the bars
	ax.set_xticks(np.arange(len(data)))
	ax.set_xticklabels(data.index)
	
	ax.set_xlabel(args.group)
	ax.set_ylabel(args.dep)
	ax.set_title(title)


	return fig,ax

def plot_v2(data):
	def set_style():
		plt.style.use('seaborn-paper')
		matplotlib.rc("font",family="serif")
	set_style()
	matrix1 = data[data.columns[0]].values
	list1 = matrix1.tolist()
	matrix2 = data[data.columns[1]].values
	list2 = matrix2.tolist()
	fig = plt.figure() 
	plt.plot(list1,list2)
	plt.title(args.title)
	plt.xlabel(args.group)
	plt.ylabel(args.dep)

	return fig

if args.plottype == "bar":
	means = data1.groupby(args.group)[args.dep].mean()
	#print(means)
	data_std = data1.groupby(args.group)[args.dep].std()
	#print(data_std)
	groups = means.index

	p1=plot_v1(means,data_std,args.title)
	p1[0].savefig(args.output)
elif args.plottype == "line":
	p1 = plot_v2(data1)
	p1.savefig(args.output)
else:
	print("Invalid argument: plot type. Acceptable plot types: bar, line.")

