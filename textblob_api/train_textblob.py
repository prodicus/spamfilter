# -*- coding: utf-8 -*-
# @Authors: Nikhil Jindal, Tasdik Rahman
# @Date:   2016-04-10 21:09:25
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-10 22:29:57
# @GPLv3 License
# @https://github.com/prodicus/spamfilter

from textblob.classifiers import NaiveBayesClassifier
import dill

from data import training_data
from constants import TEXTBLOB_PICKLE_FILE


def main():

    # training the classifier on the training_dataset
    # takes crap load of time to run
    cl = NaiveBayesClassifier(train)

    # pickling it for later resuse using dill (as json module is incable of it)
    save_classifier = open(TEXTBLOB_PICKLE_FILE, "wb")
    dill.dump(cl, save_classifier)
    save_classifier.close()

if __name__ == "__main__":
    main()
