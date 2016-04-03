## contributing

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