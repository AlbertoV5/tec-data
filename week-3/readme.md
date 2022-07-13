|                      |                                 |                                 |                                     |
|--------------------- |-------------------------------- |-------------------------------- |------------------------------------ |
| [<<Home](../index.md) | [Lesson-1](./lesson-1/readme.md) | [Lesson-2](./lesson-2/readme.md) | [Challenge>>](./challenge/readme.md) |


# Introduction

Python is one of the most popular languages in the world, used in many industries to accomplish different goals. It&rsquo;s very easy to use, as you can focus on the problem and not the intricacies of the language.

Here is a YouTube playlist of keynotes that I&rsquo;ve collected over the past month while practicing and studying Python:

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLdswL3Tb01gznKrZf0_XeOc6ftUO3yZhn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---


# Terminal and bash


## Useful commands


### Print working directory

```shell
pwd
```

    /Users/albertovaldez/tec-data/week-3


### List directory

```shell
ls
```

    lesson-1
    lesson-2
    readme.html
    readme.org


### Change directory

```shell
cd $path
```


## Navigating with the Terminal Example

First let&rsquo;s call `ls` to see the contents of the current directory. Then let&rsquo;s move into the lesson-1 folder and check if we are actually in that directory with `cd lesson-1 && pwd`. The `&&` operator will help us run commands sequentially.

```shell
ls
cd lesson-1 && pwd
```

    lesson-1
    lesson-2
    readme.html
    readme.org
    /Users/albertovaldez/tec-data/week-3/lesson-1

Use `cd ..` to navigate to the top directory. Use `cd ../week-1` to navigate to a directory named &ldquo;week-1&rdquo; in the top directory.


# Git

Version control tool that will allow us to interact with GitHub from the Terminal.


## Installing homebrew

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`


## Installing git

`brew install git`

`brew install git-lfs`


## Checking versions

```shell
git --version
```

    git version 2.24.3 (Apple Git-128)

```shell
git-lfs --version
```

    git-lfs/3.2.0 (GitHub; darwin amd64; go 1.18.2)


# Python

We will be using `Python 3.7.6`. In my case I&rsquo;ll install it using pyenv with `pyenv install` `3.7.6`.

I&rsquo;ll activate the environment with `pyenv local` `3.7.6` which will tell python to use `Python 3.7.6` whenever I execute it in this directory: `/Users/albertovaldez/tec-data/week-3`.

We can check the version with:

```shell
python --version
```

    Python 3.7.6

We can run Python from the terminal with:

```shell
python
```

Let&rsquo;s try to use the current environment.

```python
print("Hello World!")
```

    Hello World!


## Python versions - End of life

[End of life](https://endoflife.date/python) is a website that shows the dates of when a Python version is not longer receiving security updates. For example:

| Version | Released    | End of life |
|------- |----------- |----------- |
| 3.7     | 26 Jun 2018 | 27 Jun 2023 |
| 2.7     | 03 Jul 2020 | 01 Jan 2020 |

The Python version is best chosen depending on the libraries you are planning on using, and most of the time the better supported versions are the ones released 2+ years ago.


# VS Code and GitHub

I use VS Code for working on development but for journaling/studying purposes I am using Emacs with org-mode as it let&rsquo;s me publish to HTML and Markdown while I interact with code blocks in a document wide session.

This is my GitHub account: `https://github.com/albertov5/`.


# Working with Python files

I&rsquo;m making sure my working directory is `/Users/albertovaldez/tec-data/week-3` and then I&rsquo;ll open VS Code with `code .`. All new python files for this week will live in this directory.
