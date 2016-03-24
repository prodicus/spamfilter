## spamfilter

Building a spam filter for our mini-project. 

### Index

- [Initial plan of action](https://github.com/prodicus/spamfilter/tree/pickling#initial-plan-of-action)
- [Installing the dependencies](https://github.com/prodicus/spamfilter/tree/pickling#installing-the-dependencies)
  - [Downloading the NLTK corpora](https://github.com/prodicus/spamfilter/tree/pickling#downloading-the-nltk-corpora)
  - [Check whether you have everything set up](https://github.com/prodicus/spamfilter/tree/pickling#check-whether-you-have-everything-set-up)
- [Running the classifier](https://github.com/prodicus/spamfilter/tree/pickling#running-the-classifier)
  - [Manually running and training the classifier](https://github.com/prodicus/spamfilter/tree/pickling#manually-running-and-training-the-classifier)
  - [Loading the saved classifier](https://github.com/prodicus/spamfilter/tree/pickling#loading-the-saved-classifier)
- [Accuracy of the classifier](https://github.com/prodicus/spamfilter/tree/pickling#accuracy-of-the-classifier)
- [Regarding the dataset](https://github.com/prodicus/spamfilter/tree/pickling#regarding-the-dataset)
  - [Total files](https://github.com/prodicus/spamfilter/tree/pickling#total-files)
- [To the contributers](https://github.com/prodicus/spamfilter/tree/pickling#to-the-contributers)
  - [Ideas](https://github.com/prodicus/spamfilter/tree/pickling#ideas)
- [References](https://github.com/prodicus/spamfilter/tree/pickling#references)

### Initial plan of action

[:arrow_up: Back to top](https://github.com/prodicus/spamfilter/tree/pickling#spamfilter)

- [x] classify the dataset as spam or ham
  - [x] make a training set
  - [x] make a testing set (against which we will test our trained model)
- Machine learning models to be tested upon
  - [x] Naive Bayes
  - [ ] Logistic regression
  - [ ] Linear SVM
  - **more to come**
- [x] Pickling of the classifier trained on `full_corpus`
- [x] To add [`logging` module](https://docs.python.org/2/howto/logging.html) into `test.py`
  for logging error messages. 
- [ ] deploying it to [heroku](https://heroku.com)
- [ ] Implement [`sklearn`'s machine learning algorithms](https://scikit-learn.org/stable/modules/naive_bayes.html) (Will have to read upon on what's feasible and what
  is not!)

## Installing the dependencies
[:arrow_up: Back to top](https://github.com/prodicus/spamfilter/tree/pickling#spamfilter)

I prefer to use [`virtualenv`'s](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for keeping the global `python` interpreter clutter free. But you are free to do a system wide install for the dependencies.


```sh
$ git clone https://github.com/prodicus/spamfilter/ && cd spamfilter
$ pip install -r requirements.txt
```

#### Downloading the NLTK corpora

```python
>>> import nltk
>>> nltk.download('stopwords')
```

#### Check whether you have everything set up

```python
>>> from termcolor import colored
>>> import bs4
>>> from nltk.corpus import stopwords
>>> from nltk import stem
>>>
```

If the above imports work without giving you an error, you are good to go!

## Running the classifier
[:arrow_up: Back to top](https://github.com/prodicus/spamfilter/tree/pickling#spamfilter)

See that you have [`make`](https://www.gnu.org/software/make/) installed on your system

#### Manually running and training the classifier

```sh
$ make run
```

What this does is it will ask you which dataset to train the classifier upon after it is trained, which dataset to test it upon.

#### Loading the saved classifier

A trained classifier object, trained on the `full_corpus` dataset (close to 33,000 emails) can be loaded and used for classifying.

```sh
$ make pickle_run
```

Watch and lay back!

## Accuracy of the classifier
[:arrow_up: Back to top](https://github.com/prodicus/spamfilter/tree/pickling#spamfilter)

I ran it one too many times apparantly and the accuracy is generally between 

|          | Accuracy  |
|:--------:|:---:|
| **Spam** | _80 to 94%_|
| **Ham**  | _60 to 80%_ |

**Watch the classifier [in action here](http://pastebin.com/cwSQxaEX)**

## Regarding the dataset
[:arrow_up: Back to top](https://github.com/prodicus/spamfilter/tree/pickling#spamfilter)

The dataset used is the [Enron dataset](http://www.cs.cmu.edu/~enron/). The
total size of the whole file being close to **1.8GB**.

So we will be using the dataset used in the paper ["Spam Filtering with Naive Bayes - Which Naive Bayes?"](http://www.aueb.gr/users/ion/docs/ceas2006_paper.pdf) which has already classified the dataset into **spam** and **ham**. 

***

Training it against the **full_corpus** dataset and then cross validating the pickled classifier with any of the datasets

Read more about the [directory structure here](https://github.com/prodicus/spamfilter/blob/pickling/data/README.md)

#### Total files 

Training against a total of **33,702** emails!

## To the contributers
[:arrow_up: Back to top](https://github.com/prodicus/spamfilter/tree/pickling#spamfilter)

- **Make an issue if you have any query**
- before developing a feature, create a seperate branch from the master on you fork
as this will reduce merge conflicts, 

```sh
$ git checkout -b <username>/<feature_to_implement>
```

- Before making a Pull request, check whether that it passes `flake8`. Refer to [PEP0008](http://pep8.org/) for details

```sh
$ flake8 <file_you_are_working_on>.py
```
- Don't forget to flatten (`rebasing`) your commits to one before making a PR.

#### Ideas

- [ ] **Deploying to heroku**
- [ ] To make a voting system which will take the best out of all the
classifiers (increasing the accuracy is the aim)
- [x] ~~To decide on whether to use `clint` or `termcolor`~~ Using colorama as
  explained in commit [89da4cd](https://github.com/prodicus/spamfilter/commit/89da4cd534abef3adec7b6b22a4e64e0f2b33393)
- [ ] **More to come** 

## References
[:arrow_up: Back to top](https://github.com/prodicus/spamfilter/tree/pickling#spamfilter)

- ["Spam Filtering with Naive Bayes - Which Naive Bayes?". Proceedings of the 3rd Conference on Email and Anti-Spam (CEAS 2006), Mountain View, CA, USA, 2006](http://www.aueb.gr/users/ion/docs/ceas2006_paper.pdf)
