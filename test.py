# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-14
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-15
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

from __future__ import division
import os
from datetime import datetime
import bs4

from termcolor import colored
from train import Trainer

__title__ = 'SpamFilter'
__version__ = '0.0.1'
__author__ = 'Tasdik Rahman'
__email__ = 'prodicus@outlook.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Tasdik Rahman'

# current directory where test.py is situated
MODULE_DIR = os.path.abspath(os.path.join('.'))
CORPUS_DIR = os.path.join(MODULE_DIR, 'data')

"""running above snippet
>>> MODULE_DIR
'/home/tasdik/Dropbox/projects/spamfilter'
>>>
"""


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
    corpus = os.path.join(CORPUS_DIR, corpus)
    label_dir = raw_input(colored("Enter {0} directory: ".format(label), 'cyan'))
    label_dir = os.path.join(corpus, label)
    try:
        limit = int(raw_input(colored("Enter number of files to be scanned [defaults to 1000 files]: ", 'cyan')))
    except ValueError:
        print 'Invalid Integer input!. Taking the default value now (1000)'
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

        precision = correct / total
    print colored('Files classified correctly : {0} out of {1}'.format(correct, 
        total))
    print colored('Precision : {0}'.format(precision), 'blue')


def main():
    kwargs = {}  # building up the arguments for the test() function

    directory = raw_input(colored("Enter Corpus Directory['eg: corpus2'] : ",
     'blue'))
    spam = raw_input(colored("Enter Spam Sub Directory[eg : 'spam']: ",
        'blue'))
    ham = raw_input(colored("Enter Clean Emails Sub Directory[eg :'ham']: ",
        'blue'))
    limit = raw_input(colored("Enter Limit of files per class(spam/ham)[eg: 1000]: ",
        'blue'))

    directory = os.path.join(CORPUS_DIR, directory)
    spam = os.path.join(directory, spam)
    ham = os.path.join(directory, ham)

    # TO-DO: Raise custom exceptions in test.py:main()
    # ================================================
    # raising custom exceptions: http://stackoverflow.com/a/9157277/3834059
    # try:
    #     try:
    #         directory_exists = map(
    #             lambda x: os.path.exists, [directory, spam, ham])
    #         # one of the entered directory or subdirectory doesn't exists
    #         if False in directory_exists:
    #             raise OSError('Directory does not exist!')
            # kwargs['directory'] = directory
            # kwargs['spam'] = spam
            # kwargs['ham'] = ham
    #     except OSError as e:
    #         print e

    #     try:
    #         kwargs['limit'] = int(limit)
    #     except TypeError as err:
    #         raise TypeError('Enter valid input for "limit": {0}'.format(err))
    # except TypeError as e:
    #     print colored(e, 'red')
    #     # exiting
    #     raise SystemExit  # refer http://stackoverflow.com/a/19747562/3834059
    # except OSError as e:
    #     print colored(e, 'red')
    #     raise SystemExit

    try:
        kwargs['directory'] = directory
        kwargs['spam'] = spam
        kwargs['ham'] = ham
    except ValueError:
        print colored("Switching back to the default test values:")
        kwargs['directory'] = 'corpus3'
        kwargs['spam'] = 'spam'
        kwargs['ham'] = 'ham'

    try:
        kwargs['limit'] = int(limit)
    except TypeError as e:
        print "Taking default value of limit (1000)"
        kwargs['limit'] = 500

    trainer = Trainer(**kwargs)

    starting_time = datetime.now()
    classifier_object = trainer.train(verbose=1)
    end_time = datetime.now()

    elapsed = end_time - starting_time
    # ref: http://stackoverflow.com/a/1345852/3834059
    minutes_elapsed, seconds_elapsed = divmod(
        elapsed.total_seconds(), 60)[0], divmod(elapsed.total_seconds(), 60)[1]
    print colored("Training took {min} minutes : {sec} seconds".format(
        min=minutes_elapsed,
        sec=seconds_elapsed
        ),'green')

    # Testing the accuracy
    test(trainer, classifier_object, 'spam')
    test(trainer, classifier_object, 'ham')

if __name__ == "__main__":
    main()
