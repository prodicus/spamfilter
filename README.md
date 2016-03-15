## spamfilter

Building a spam filter for our mini-project

### Initial plan of action

- [x] classify the dataset as spam or ham
  - [x] make a training set
  - [x] make a testing set (against which we will test our trained model)
- Machine learning models to be tested upon
  - [x] Naive Bayes
  - [ ] Logistic regression
  - [ ] Linear SVM
  - **more to come**
- Implement [`sklearn`'s machine learning algorithms](https://scikit-learn.org/stable/modules/naive_bayes.html) (Will have to read upon on what's feasible and what
  is not!)
- To add [`logging` module](https://docs.python.org/2/howto/logging.html) into `test.py`
  for logging error messages. 

## Far fetched Ideas!

- [ ] To make a voting system which will take the best out of all the
classifiers (increasing the accuracy is the aim)
- [x] ~To decide on whether to use `clint` or `termcolor`~ Using colorama as
  explained in commit [89da4cd](https://github.com/prodicus/spamfilter/commit/89da4cd534abef3adec7b6b22a4e64e0f2b33393)
- [ ] deploying it to [heroku](https://heroku.com)
- [ ] **More to come** 

### Regarding the dataset

The dataset used is the [Enron dataset](http://www.cs.cmu.edu/~enron/). The
total size of the whole file being close to **1.8GB**.

So we will be using the dataset used in the paper ["Spam Filtering with Naive Bayes - Which Naive Bayes?"](http://www.aueb.gr/users/ion/docs/ceas2006_paper.pdf). 

Namely -

- `corpus1`
- `corpus2`
- `corpus3`

#### Typical directory structure

```sh
tasdik at Acer in ~/Dropbox/projects/spamfilter on master [!]
$ tree -L 2 data
data
├── corpus1
│   ├── ham
│   └── spam
├── corpus2
│   ├── ham
│   └── spam
├── corpus3
│   ├── ham
│   ├── spam
│   └── Summary.txt
├── enron1
│   ├── ham
│   ├── spam
│   └── Summary.txt
├── enron2
│   ├── ham
│   ├── spam
│   └── Summary.txt
├── enron3
│   ├── ham
│   ├── spam
│   └── Summary.txt
├── enron4
│   ├── ham
│   ├── spam
│   └── Summary.txt
├── enron5
│   ├── ham
│   ├── spam
│   └── Summary.txt
└── enron6
    ├── ham
    ├── spam
    └── Summary.txt

27 directories, 7 files

```


##### Total files 

```sh
tasdik at Acer in ~/Dropbox/projects/spamfilter on master [!?]
$ find ~/Dropbox/projects/spamfilter/data -type f | wc -l
50070
```

Yeah, right. Close to **50k** emails

## To the contributers

- **Make an issue if you have any query**
- before developing a feature, please create a seperate branch from the master
as this will reduce merge conflicts, 

```sh
$ git checkout -b <username>/<feature_to_implement>
```

- Before making a Pull request, check whether that it passes `flake8` or 
conforms to [PEP0008](http://pep8.org/)

```sh
$ flake8 <file_you_are_working_on>.py
```
- Don't forget to flattening(`rebasing`) your commits to 1 before making PR.

## References

- ["Spam Filtering with Naive Bayes - Which Naive Bayes?". Proceedings of the 3rd Conference on Email and Anti-Spam (CEAS 2006), Mountain View, CA, USA, 2006](http://www.aueb.gr/users/ion/docs/ceas2006_paper.pdf)
