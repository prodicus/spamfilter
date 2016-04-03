## Textblob API

Textblob was used just for experimentation purposes when we started out. Our custom classifier performs better than this!

> [Textblob](https://textblob.readthedocs.org/en/dev/) has an option to [manually train](https://textblob.readthedocs.org/en/dev/classifiers.html) the dataset and then cross validate the accuracy of the trained data.

#### Directory structure

```bash
tasdik at Acer in ~/Dropbox/projects/spamfilter/textblob_api on master [!?]
$ tree -L 2
.
├── constants.py
├── data.py
├── __init__.py
├── README.md
└── train_textblob.py

```

#### Pickled API usage

```python
>>> from data import testing_data
>>>
>>> import dill
>>> 
>>> # assuming that 'textblob_api.pickle' file is in the current directory
>>> f = open('textblob_api.pickle', 'rb')
>>> cl = dill.load(f)
>>>
>>> spam_text = \
...  "My Dear Friend, How are you and your family? I hope you all "\
...  "are fine. My dear I know that this mail will come to you as a"\
...  "surprise, but it's for my urgent need for a foreign partner that"\
...  "made me to contact you for your sincere genuine assistance My"\
...  "name is Mr.Herman Hirdiramani, I am a banker by profession "\
...  "currently holding the post of Director Auditing Department "\
...  "in the Islamic Development Bank(IsDB)here in Ouagadougou, "\
...  "Burkina Faso. I got your email information through the "\
...  "Burkina's Chamber of Commerce and industry on foreign business"\
...  "relations here in Ouagadougou Burkina Faso I haven'disclose "\
...  "this deal to any body I hope that you will not expose or betray"\
...  "this trust and confident that I am about to repose on you for"\
...  "the mutual benefit of our both families. I need your urgent"\
...  "assistance in transferring the sum of Eight Million,Four "\
...  "Hundred and Fifty Thousand United States Dollars ($8,450,000:00)"\
...  "into your account within 14 working banking days This money has "\
...  "been dormant for years in our bank without claim due to the owner"\
...  "of this fund died along with his entire family and his supposed"\
...  "next of kin in an underground train crash since years ago."\
...  "For your further informations please visit "\
...  "http://news.bbc.co.uk/2/hi/5141542.stm)"
>>>
>>> cl.classify(spam_text)
'spam'
>>>
>>> cl.accuracy(testing_data)
0.9090909090909091
>>>
>>> cl.show_informative_features(15)
Most Informative Features
         contains(money) = True             spam : ham    =     19.7 : 1.0
         contains(click) = True             spam : ham    =     19.0 : 1.0
      contains(attached) = True              ham : spam   =     16.3 : 1.0
       contains(meeting) = True              ham : spam   =     15.7 : 1.0
          contains(2000) = True              ham : spam   =     15.0 : 1.0
           contains(www) = True             spam : ham    =     12.3 : 1.0
     contains(marketing) = True             spam : ham    =     11.7 : 1.0
        contains(review) = True              ham : spam   =     11.0 : 1.0
     contains(regarding) = True              ham : spam   =     10.3 : 1.0
          contains(team) = True              ham : spam   =      9.0 : 1.0
           contains(com) = True             spam : ham    =      9.0 : 1.0
       contains(subject) = True             spam : ham    =      8.3 : 1.0
  contains(professional) = True             spam : ham    =      8.3 : 1.0
       contains(product) = True             spam : ham    =      7.7 : 1.0
    contains(operations) = True              ham : spam   =      7.7 : 1.0
>>> 
```

