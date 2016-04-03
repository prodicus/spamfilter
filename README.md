## spamfilter

[spamfilter](https://github.com/prodicus/spamfilter) is our Machine Learning project, where we build a __custom Naive Bayes
classifier__ to classify email into __ham__ or __spam__.

**Trained on the feature sets of close to 33,000 training emails**

- CAPSLOCK
- attachments
- numbers
- Links
- Words in text

**You can use the pickled classifier objects to classify mail into __spam__ or __ham__. (Refer the [DEMO and API usage](#api-usage) guide for details)**

## Index

- [Development](#development)
  - [Installing the dependencies](#installing-the-dependencies)
  - [Downloading the NLTK corpora](#downloading-the-nltk-corpora)
  - [Check whether you have everything set up](#check-whether-you-have-everything-set-up)
- [Running the classifier](#running-the-classifier)
  - [Loading the saved classifier](#loading-the-saved-classifier)
  - [Manually running and training the classifier](#manually-running-and-training-the-classifier)
- [API usage](#api-usage)
  - [Custom NB classifier API](#custom-nb-classifier-api)
  - [Textblob API](#textblob-api)
- [Training classifier on your own dataset](#training-classifier-on-your-own-dataset)
- [FAQ](#faq)
  - [Accuracy of the classifier](#accuracy-of-the-classifier)
  - [Regarding the dataset](#regarding-the-dataset)
- [To the contributers](#to-the-contributers)
  - [Ideas](#ideas)
- [Legal stuff](#legal-stuff)

## Development
[:arrow_up: Back to top](#spamfilter)

#### Installing the dependencies

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
[:arrow_up: Back to top](#spamfilter)

After [installing the dependencies](https://github.com/prodicus/spamfilter#installing-the-dependencies) make sure that you have [`make`](https://www.gnu.org/software/make/) installed on your system

#### Loading the saved classifier

A trained classifier object, trained on the `full_corpus` dataset (close to 33,000 emails) can be loaded and used for classifying.

```sh
$ make pickle_run
```

Watch and lay back!

#### Manually running and training the classifier

```sh
$ make run
```

What this does is it will ask you which dataset to train the classifier upon.

And after it is trained, which dataset to test the classifier upon.

**NOTE**: For those not having `make` installed. You will have to do a 

- `$ python test.py` for `$ make run`
- `$ python test_classifier_pickle.py` for `$ make pickle_run`

## API usage
[:arrow_up: Back to top](#spamfilter)

### Custom NB classifier API

**Refer [API usage for the custom classifier (wiki)](https://github.com/prodicus/spamfilter/wiki/API-usage-for-the-custom-classifier) for implementation details**

### Textblob API

**Refer [API usage for the textblob classifier (wiki)](https://github.com/prodicus/spamfilter/wiki/API-usage-for-the-textblob-classifier) for implementation details**

##Training classifier on your own dataset

You can train the classifier on your own dataset! 

#### Step 1

Put your dataset folder (eg: `data_foo`) inside the `data` folder

```bash
$ tree data/corpus2/ -L 1
data/data_foo/
├── ham
└── spam

```

#### Step 2

- specify the folder name of your newly added dataset and the name of the pickle file to be created here [here in file `create_pickle.py`](https://github.com/prodicus/spamfilter/blob/f9dc8e9dabc7b9916c964fcdeb4329fabfaf3822/create_pickle.py#L33-L37)

- Choose the number of files to train the classifier againt [here in file `create_pickle.py`](https://github.com/prodicus/spamfilter/blob/f9dc8e9dabc7b9916c964fcdeb4329fabfaf3822/create_pickle.py#L54)

#### Step 3

```bash
$ make pickle
```

![boom](http://media.tumblr.com/tumblr_ltuzjvbQ6L1qzgpx9.gif)

## FAQ
[:arrow_up: Back to top](#spamfilter)

#### Accuracy of the classifier

I ran it one too many times apparantly and the accuracy is generally between 

|          | Accuracy  |
|:--------:|:---:|
| **Spam** | _80 to 94%_|
| **Ham**  | _70 to 80%_ |

**Watch the classifier [in action here](http://pastebin.com/cwSQxaEX)**

#### Regarding the dataset

The dataset used is the [Enron dataset](http://www.cs.cmu.edu/~enron/). 

We Trained our [`spam_classifier.pickle`](https://github.com/prodicus/spamfilter/blob/master/saved_classifiers/spam_classifier.pickle) classifier object against the [full_corpus](https://github.com/prodicus/spamfilter/tree/master/data/full_corpus) dataset and then cross validated the pickled classifier with any of the datasets present in the [data](https://github.com/prodicus/spamfilter/tree/master/data/) directory

Read more about the [directory structure here](https://github.com/prodicus/spamfilter/blob/pickling/data/README.md)

## To the contributers
[:arrow_up: Back to top](#spamfilter)

Refer [CONTRIBUTING.md](https://github.com/prodicus/spamfilter/tree/master/CONTRIBUTING.md) for more details

#### Ideas
[:arrow_up: Back to top](#spamfilter)

- [ ] **Deploying a full blown app to heroku**
- [ ] ~~To make a voting system which will take the best out of all the classifiers (increasing the accuracy is the aim)~~
- [x] Try out [`textblob`](https://textblob.readthedocs.org/en/dev/) and see how it performs with our classifier
- [x] ~~To decide on whether to use `clint` or `termcolor`~~ Using colorama as
  explained in commit [89da4cd](https://github.com/prodicus/spamfilter/commit/89da4cd534abef3adec7b6b22a4e64e0f2b33393)

## Legal Stuff
[:arrow_up: Back to top](#spamfilter)

Open sourced under [GPLv3](http://www.gnu.org/licenses/gpl-3.0.en.html)

    spamfilter
    Copyright (C) 2016  Tasdik Rahman(prodicus@outlook.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

You can a copy of the [LICENSE](https://github.com/prodicus/spamfilter/tree/master/LICENSE) file HERE