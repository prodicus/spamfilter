# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-24 01:24:13
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-24 11:39:55

"""Saves a the classifier_object and trainer object as a pickle object for
later reuse. A demo of that is done in test_classifier_pickle.py


References
==========

[1]:
  - http://stackoverflow.com/q/16626429/3834059
  - http://stackoverflow.com/a/21239587/3834059
[2]: http://trac.mystic.cacr.caltech.edu/project/pathos/wiki/dill
[3]: http://stackoverflow.com/a/1345852/3834059
"""

from __future__ import division
import os
from datetime import datetime
import logging
# import pickle   ## importing dill instead


import dill     # refer: [1], for further documentation refer: [2]
from train import Trainer
from termcolor import colored

# current directory where create_pickle.py is situated
MODULE_DIR = os.path.abspath(os.path.join('.'))
CORPUS_DIR = os.path.join(MODULE_DIR, 'data', 'full_corpus')
CLASSIFIER_DIR = os.path.join(MODULE_DIR, 'saved_classifiers')
CLASSIFIER_FILE = os.path.join(CLASSIFIER_DIR, 'spam_classifier.pickle')
TRAINER_FILE = os.path.join(CLASSIFIER_DIR, 'trainer.pickle')

logging.basicConfig(
    filename='logfiles/logfile.txt',
    level = logging.DEBUG,
    filemode = 'w',
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def save_pickle():
    directory = CORPUS_DIR
    spam = os.path.join(directory, 'spam')
    ham = os.path.join(directory, 'ham')
    kwargs = {
        "directory": directory,
        "spam": spam,
        "ham": ham,
        "limit": 16545
    }

    logging.info("Testing the classifier on dataset : {0}".format(directory))

    # limit is given 16545 as 
    """
    $ ls data/full_corpus/ham | wc -l
    16545
    tasdik at Acer in ~/Dropbox/projects/spamfilter on pickling [!?]
    $ ls data/full_corpus/spam | wc -l
    17157
    (spamfilter)
    """

    trainer = Trainer(**kwargs)

    ## saving the trainer object
    trainer_file = open(TRAINER_FILE, "wb")
    dill.dump(trainer, trainer_file)
    trainer_file.close()

    ## training it
    starting_time = datetime.now()
    classifier_object = trainer.train(verbose=1)
    end_time = datetime.now()

    ## saving the classifier
    save_classifier = open(CLASSIFIER_FILE, "wb")
    dill.dump(classifier_object, save_classifier)
    save_classifier.close()

    elapsed = end_time - starting_time  # refer: [3]
    minutes_elapsed, seconds_elapsed = divmod(
        elapsed.total_seconds(), 60)[0], divmod(elapsed.total_seconds(), 60)[1]
    print colored("Training took {min} minutes : {sec} seconds".format(
        min=minutes_elapsed,
        sec=seconds_elapsed
        ),'green')
    logging.info("Training took {min} minutes : {sec} seconds".format(
        min=minutes_elapsed,
        sec=seconds_elapsed
        ))

def main():
    save_pickle()

if __name__ == "__main__":
    main()