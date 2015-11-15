# python_example_package

A minimal Python package containing a single function and a minimal set of `nose` tests.
It is intended to serve as a template for building other packages.

TODO: Add MkDocs

## Using this as a package skeleton

Adapted from: http://learnpythonthehardway.org/book/ex46.html

Whenever you want to start a new project, do this:

1. Make a copy of the `python_example_package` directory. Name it after your new project.
2. Rename `python_example_package` to your project name throughout the skeleton files. 
3. Edit your `setup.py` to have all the information for your project.
4. Double check it's all working by using `nosetests` again.
       - from the main package directory run `nosetests`
5. Remove the sample function from the package `__init__.py` and the corresponding tests from `tests/`.
6. Start coding.


## More on naming from StackOverflow

source: `http://stackoverflow.com/questions/17457782/how-to-structure-python-packages-without-repeating-top-level-name-for-import/17530651#17530651`

... most people, tools and docs assume you have a package ...
So the minimum would be:

```
bagoftricks
├── bagoftricks
│   └── __init__.py
├── README.md
└── setup.py
```

With __init__.py containing the functions you want to import. You then use these functions like this:

from bagoftricks import levenshtein, anotherfunction
Once that __init__.py becomes too big, you want to split it up in several modules, giving you something like this:

```
bagoftricks
├── bagoftricks
│   ├── __init__.py
│   ├── anothermodule.py
│   └── levenshtein.py
├── README.md
└── setup.py
```

Your __init__.py should then import the functions from the various modules:

```
from bagoftricks.levenshtein import levenshtein
from bagoftricks.anothermodule import anotherfunction
```

And then you can still use them like like you did before.

shareimprove this answer
answered Jul 8 '13 at 15:39

Lennart Regebro
64k13105183