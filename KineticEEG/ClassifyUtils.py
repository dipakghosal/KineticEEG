"""This file contains many nessecary utilities for the classification alogrithm"""
import math

def euclideandistance(inst1, inst2, leng):
    d=0
    for i in range(leng):
        d+=pow((inst1[i]-inst2[i]),2)

    return math.sqrt(d)
