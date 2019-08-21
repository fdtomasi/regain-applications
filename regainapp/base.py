"""Utility to load datasets."""
import pandas as pd
import os


def load_webkb():
    txt_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'text')

    train_filename = os.path.join(txt_path, 'webkb-train-stemmed.txt')
    train = pd.read_csv(train_filename, header=None, sep='\t',
                        index_col=0).dropna()
    train.columns = ['words']

    test_filename = os.path.join(txt_path, 'webkb-train-stemmed.txt')
    test = pd.read_csv(test_filename, header=None, sep='\t',
                       index_col=0).dropna()
    test.columns = ['words']

    return train, test
