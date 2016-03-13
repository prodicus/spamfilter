## spamfilter

Building a spam filter for our mini-project

### Initial plan of action

- [x] classify the dataset as spam or ham
  - [x] make a training set
  - [x] make a testing set (against which we will test our trained model)
- Machine learning models to be tested upon
  - [ ] Naive Bayes
  - [ ] Logistic regression
  - [ ] Linear SVM
  - **more to come**
- To make a voting system which will take the best out of all the
classifiers (increasing the accuracy is the aim)

- To decide on whether to use `clint` or `termcolor`
- [ ] deploying it to [heroku](https://heroku.com)

**More to come** 

### Regarding the dataset

The dataset used is the [Enron dataset](http://www.cs.cmu.edu/~enron/). The
total size of the whole file being close to **1.8GB**.

So we will be using the dataset used in the paper ["Spam Filtering with Naive Bayes - Which Naive Bayes?"](http://www.aueb.gr/users/ion/docs/ceas2006_paper.pdf). 

Namely

- `enron1`
- `enron2`
- `enron3`
- `enron4`
- `enron5`
- `enron6`

#### Typical directory structure

```sh
tasdik at Acer in ~/Dropbox/projects/spamfilter on master [!?]
$ tree data/ -I "corpus|corpus2|corpus3" | head -n 10
data/
├── enron1
│   ├── ham
│   │   ├── 0001.1999-12-10.farmer.ham.txt
│   │   ├── 0002.1999-12-13.farmer.ham.txt
│   │   ├── 0003.1999-12-14.farmer.ham.txt
│   │   ├── 0004.1999-12-14.farmer.ham.txt
│   │   ├── 0005.1999-12-14.farmer.ham.txt
│   │   ├── 0007.1999-12-14.farmer.ham.txt
│   │   ├── 0009.1999-12-14.farmer.ham.txt

tasdik at Acer in ~/Dropbox/projects/spamfilter on master [!?]
$ #### FOR SPAM FOLDER

tasdik at Acer in ~/Dropbox/projects/spamfilter on master [!?]
$ tree data/ -I "corpus|corpus2|corpus3|ham" | head -n 10
data/
├── enron1
│   ├── spam
│   │   ├── 0006.2003-12-18.GP.spam.txt
│   │   ├── 0008.2003-12-18.GP.spam.txt
│   │   ├── 0017.2003-12-18.GP.spam.txt
│   │   ├── 0018.2003-12-18.GP.spam.txt
│   │   ├── 0026.2003-12-18.GP.spam.txt
│   │   ├── 0032.2003-12-19.GP.spam.txt
│   │   ├── 0040.2003-12-19.GP.spam.txt

tasdik at Acer in ~/Dropbox/projects/spamfilter on master [!?]
$ 
```

**note**: The number at the beginning of each filename is the "order of arrival".

##### Total files 

Spam | Ham
--- | ---
17171 | 16545

## To the team members

- **Make an issue if you have any query**
- before developing a feature, please create a seperate branch from the master
as this will reduce merge conflicts, 
- Before making a Pull request, check whether that it passes `flake8` or 
conforms to [PEP0008](http://pep8.org/)

```sh
$ git checkout -b <username>/<feature_to_implement>
```

## References

- ["Spam Filtering with Naive Bayes - Which Naive Bayes?". Proceedings of the 3rd Conference on Email and Anti-Spam (CEAS 2006), Mountain View, CA, USA, 2006](http://www.aueb.gr/users/ion/docs/ceas2006_paper.pdf)
