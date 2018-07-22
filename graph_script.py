import sys
import os
from argparse import ArgumentParser

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

parser = ArgumentParser()
parser.add_argument("-f","--file",dest="filename", help="The input datafile", metavar="FILE")
parser.add_argument("-g","--group",dest="group", help="The groups that you would like to sort by. May be an array.")
parser.add_argument("-d","--dependent",dest="dep", help="The dependent variable you wish to graph.")
parser.add_argument("-t","--title",dest="title", help="The title of your figure.")
parser.add_argument("-o","--output",dest="output", help="The desired output filename. Please include the extension.")
args = parser.parse_args()


data1 = pd.read_csv(args.filename, sep="\t", lineterminator="\n")

#print(data1.head())

means = data1.groupby(args.group)[args.dep].mean()
#print(means)
data_std = data1.groupby(args.group)[args.dep].std()
#print(data_std)
groups = means.index

def plot_v1(data,error,title):
        def set_style():
                plt.style.use('seaborn-paper')
                matplotlib.rc("font",family="serif")
        set_style()

        #Create the figure and axis objects that I'll plot on.
        fig, ax = plt.subplots()

        #plot the bars
        ax.bar(np.arange(len(data)),data,yerr=error,align="center",alpha=0.5,ecolor='black',capsize=2)

        #setting a nice y-axis limit
        ax.set_ylim(0,25)

        #label the bars
        ax.set_xticks(np.arange(len(data)))
        ax.set_xticklabels(data.index)

        ax.set_xlabel(args.group)
        ax.set_ylabel(args.dep)
        ax.set_title(title)


        return fig,ax


p1=plot_v1(means,data_std,args.title)
p1[0].savefig(args.output)
