# Little Lemon

### I use dir env python virtual env management

See more [here](https://stackabuse.com/managing-python-environments-with-direnv-and-pyenv/)

1. Install direnv
2. Place this in your bash rc: `eval "$(direnv hook zsh)"`
3. cd into the repo and write `direnv allow`

### Install dependencies:

```
pip install -r ./requirements/dev.txt
```

### Start server

```
python manage.py runserver
```
