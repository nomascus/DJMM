#!bin/#!/usr/bin/env python3

#filename: pca_plot.py
#owner: Stella Paffenholz
#output: Generate a PCA plot from a dictionary containing counts of amino acids and DNA bases from a dna string generated from a song of a specific genre


#Generate a dataframe from the dictionary containing the amino acid, nucleotide composition and genre
import pandas as pd
import numpy as np

dict = {'song1':{'Met':1, 'Thr':3, 'Arg':2, 'A':30,'C':15, 'T':20, 'G':10, 'genre':'rock'}, 'song2':{'Met':1, 'Thr':2, 'Arg':3, 'A':15,'C':20, 'T':8, 'G':32, 'genre':'classical'}, 'song3':{'Met':1, 'Thr':5, 'Arg':2, 'A':7,'C':21, 'T':18, 'G':32, 'genre':'dance'}}

seq_df = pd.DataFrame.from_dict(dict)
seq_df = seq_df.transpose()
print(seq_df)


#Standardize the data onto unit scale (mean = 0 and variance = 1)
from sklearn.preprocessing import StandardScaler

#seperating out the counts of amino acid and DNA bases (= column headers, without genre)
features = list(seq_df)
features.remove('genre')

x = seq_df.loc[:, features].values
print(x)

#separating out the genres
y = seq_df.loc[:,['genre']].values
print(y)

#standardizing the features
x2 = StandardScaler().fit_transform(x)
print(x2)


# calculate principal components and create dataframe of genre with PC1 and PC2 values
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_components = pca.fit_transform(x2)
print(pca_components)


principal_df = pd.DataFrame(data = pca_components
             , columns = ['PC1', 'PC2'], index = seq_df.index)
print(principal_df)

final_df = pd.concat([principal_df, seq_df[['genre']]], axis = 'columns')
print(final_df)

#PCA plotting
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('PC1', fontsize = 15)
ax.set_ylabel('PC2', fontsize = 15)
ax.set_title('PCA', fontsize = 20)

targets = ['rock', 'classical', 'dance']
colors = ['r', 'g', 'b']

for genre, color in zip(targets,colors):
    indicesToKeep = final_df['genre'] == genre
    ax.scatter(final_df.loc[indicesToKeep, 'PC1']
               , final_df.loc[indicesToKeep, 'PC2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
