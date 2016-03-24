## Data

Stores the corpus on which we train and cross validate the classifier

The `classifier_object` was trained on the `full_corpus` which has

| Spam | Ham | 
|:--:|:--:|
| 17157| 16545|

So trained on a total of **33,702** emails!

### typical directory structure

```sh
$ tree -L 2
.
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
├── enron6
│   ├── ham
│   ├── spam
│   └── Summary.txt
├── full_corpus
│   ├── ham
│   └── spam
└── README.md
```
