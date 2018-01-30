#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Add random data to dummy speakers.csv data"""
from random import random
import lorem
import pandas as pd

# institutions

def get_random_institution(row):
    insts = [['KCL', 0.3], ['UCL', 0.5], ['Imperial', 0.6], ['Oxford', 0.7],
             ['Cambridge', 0.8], ['Manchester', 0.9]]
    rand = random()
    i = 0
    floor = 0
    while True:
        try:
            ceil = insts[i][1]
        except IndexError:
            return ''
        if (rand >= floor) & (rand < ceil):
            return insts[i][0]
        else:
            floor = ceil
            i += 1

def get_random_plenary(row):
    if row.role == 'speaker':
        plens = [['Plenary 1', 0.4], ['Plenary 2', 0.6], ['Plenary 3', 1.0]]
        rand = random()
        i = 0
        floor = 0
        while True:
            try:
                ceil = plens[i][1]
            except IndexError:
                return ''
            if (rand >= floor) & (rand < ceil):
                return plens[i][0]
            else:
                floor = ceil
                i += 1
    else:
        return ''

# homepages
def make_homepage(row):
    maxval = 1500
    url = 'xkcd.com/'+str(int(maxval*random()))
    # assume 30% have homepages
    if random() < 0.33:
        return url
    else:
        return ''

# twitter handles
def make_twitter(row):
    if random() < 0.16:
    # assume one in siz gives a twitter handle
        return '@'+row['surname']+str(int(random()*1000))
    else:
        return ''

# Talk titles
def get_random_title(row):
    if row.role == 'speaker':
        return lorem.sentence()
    else:
        return ''

df = pd.read_csv('../data-src/speakers.csv')
try:
    df.drop('num', inplace=True, axis=1)
    df.drop('institution', inplace=True, axis=1)
except ValueError:
    # num column not in dataframe
    pass

#print(df.apply(get_random_institution, axis=1))
df['university'] = df.apply(get_random_institution, axis=1)
df['homepage'] = df.apply(make_homepage, axis=1)
df['twitter'] = df.apply(make_twitter, axis=1)
df['talk_title'] = df.apply(get_random_title, axis=1)
df['plenary'] = df.apply(get_random_plenary, axis=1)

print('Writing dummy data to csv...')
df.to_csv('../data-src/participant_data.csv')
print('Success!\n')
print(df.head())
#print(get_random_plenary())
