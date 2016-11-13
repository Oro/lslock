<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orge10bff5">1. lslock</a>
<ul>
<li><a href="#org3027c06">1.1. Installation</a></li>
<li><a href="#orgd3c7014">1.2. Development</a>
<ul>
<li><a href="#orgf213cd9">1.2.1. Prerequisites</a></li>
<li><a href="#org95805cd">1.2.2. Running tests</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="orge10bff5"></a>

# lslock

    lslock /tmp

    File /tmp/locks/my.lock is locked by PID 5421

`lslock` comes with two executables, `lslock` and `lslock-test`.

-   `lslock` checks a given directory (and subdirectories) for any locked files and outputs them.
-   `lslock-test` locks a given number of files in a given directory and is used to check the validity of `lslock`.

See `lslock --help` or `lslock-test --help` for parameters.

`lslock` was tested on Ubuntu 12.04, but should work on Linux with Python >= 2.7.
For a leaner method of testing for locks on specific files, check out [lsof](https://linux.die.net/man/8/lsof).


<a id="org3027c06"></a>

## Installation

Make sure you have python and pip installed. If you are on a debian/ubuntu based system, you can install them via

    sudo apt-get update
    sudo apt-get install -y python-pip python-dev build-essential
    sudo pip install --upgrade pip virtualenv

Then run the following to be able to run `lslock` and `lslock-test`. If you are not using a virtualenv, you might need to run this as sudo as well.

    cd <path-to-repo>
    virtualenv venv
    . venv/bin/activate
    pip install -e .


<a id="orgd3c7014"></a>

## Development


<a id="orgf213cd9"></a>

### Prerequisites

Make sure you have vagrant installed. Then run `vagrant up` in the cloned repository. You are now able to connect with `ssh vagrant@172.25.12.6:22`, password `vagrant` and find the contents of this repository at `/vagrant/`.

Create the virtual env with `virtualenv /vagrant/venv` and activate it with `. /vagrant/venv/bin/activate`. Install the dependencies via `pip install -e /vagrant/`.


<a id="org95805cd"></a>

### Running tests

You can run the tests via `nosetests /vagrant/lslock.py`.

