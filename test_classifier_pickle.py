# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-14
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-24 15:35:02
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

"""
Loads the pickled classifier which was trained against the "full_corpus"
dataset in "saved_classifiers" directory and tests against

"""

from __future__ import division
import os
from datetime import datetime
import logging

import bs4
from termcolor import colored
import dill

from train import Trainer

logging.basicConfig(
    filename='logfiles/logfile.txt',
    level = logging.DEBUG,
    filemode = 'w',
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

# current directory where test.py is situated
MODULE_DIR = os.path.abspath(os.path.join('.'))
CORPUS_DIR = os.path.join(MODULE_DIR, 'data')

def test(trainer, classifier_object, label):
    """
    :param trainer: Obejct of class Trainer
    :param classifier_object: Classifier object
    :param label: label to be tested. Will be taken from the testing dataset
    """
    print "\n"
    print colored("#"*40, "yellow")
    print "Testing the classifier on Test Dataset\n"

    corpus = raw_input(colored("Enter corpus directory: [eg: corpus3] ", 'cyan'))
    logging.info("Testing the classifier on dataset "+corpus)
    corpus = os.path.join(CORPUS_DIR, corpus)
    label_dir = raw_input(colored("Enter {0} directory: ".format(label), 'cyan'))
    label_dir = os.path.join(corpus, label)
    try:
        limit = int(raw_input(colored("Enter number of files to be scanned [defaults to 1000 files]: ", 'cyan')))
    except ValueError:
        print 'Invalid Integer input!. Taking the default value now (1000)'
        logging.debug('Invalid Integer input!. Taking the default value now (1000)')
        limit = 1000

    os.chdir(label_dir)

    correct = 0
    total = 0

    print colored("Testing {label} files".format(label=label), 'green')

    for email in os.listdir(label_dir)[:limit]:
        email_file = open(email, 'r')
        email_text = email_file.read()
        email_file.close()
        try:
            email_text = bs4.UnicodeDammit.detwingle(email_text).decode(
                'utf-8'
            )
        except:
            print colored("Skipping file: '{file}'' due to bad encoding!".format(
                file=email), 'red')
            logging.error("Skipping file: '{file}'' due to bad encoding!".format(
                file=email))
            continue
        email_text = email_text.encode('ascii', 'ignore')
        hamorspam = classifier_object.classify(trainer.extract_features(
            email_text)
        )

        total += 1
        if hamorspam == label:
            correct += 1
        else:
            print colored('Classified {mail} incorrectly'.format(
                mail=email), 'yellow'
            )
            logging.warning('Classified {mail} incorrectly'.format(
                mail=email))

        precision = correct / total
    print colored('Files classified correctly : {0} out of {1}'.format(correct, 
        total))
    logging.info('Files classified correctly : {0} out of {1}'.format(correct, 
        total))
    print colored('Precision : {0}'.format(precision), 'blue')
    logging.info('Precision : {0}'.format(precision))


def main():

    classifier_file = open('saved_classifiers/spam_classifier.pickle', 'rb')
    classifier_object = dill.load(classifier_file)
    classifier_file.close()

    trainer_file = open('saved_classifiers/trainer.pickle', 'rb')
    trainer_object = dill.load(trainer_file)
    trainer_file.close()

    # Testing the accuracy
    test(trainer_object, classifier_object, 'spam')
    test(trainer_object, classifier_object, 'ham')

if __name__ == "__main__":
    main()
