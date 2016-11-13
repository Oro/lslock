<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org7429b48">1. lslock</a>
<ul>
<li><a href="#org76d60e3">1.1. Installation</a></li>
<li><a href="#org02caf2d">1.2. Development</a>
<ul>
<li><a href="#org02bb3c7">1.2.1. Prerequisites</a></li>
<li><a href="#org2eff80f">1.2.2. Running tests</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org7429b48"></a>

# lslock

    lslock /tmp

    File /tmp/locks/my.lock is locked by PID 5421

`lslock` comes with two executables, `lslock` and `lslock-test`.

-   `lslock` checks a given directory (and subdirectories) for any locked files and outputs them.
-   `lslock-test` locks a given number of files in a given directory and is used to check the validity of `lslock`.

See `lslock --help` or `lslock-test --help` for parameters.

`lslock` was tested on Ubuntu 12.04, but should work on Linux with Python >= 2.7.
For a leaner method of testing for locks on specific files, check out [lsof](https://linux.die.net/man/8/lsof).


<a id="org76d60e3"></a>

## Installation

    cd <path-to-repo>
    pip install -e .


<a id="org02caf2d"></a>

## Development


<a id="org02bb3c7"></a>

### Prerequisites

Make sure you have vagrant installed. Then run `vagrant up` in the cloned repository. You are now able to connect with `ssh vagrant@172.25.12.6:22`, password `vagrant` and find the contents of this repository at `/vagrant/`.

Create the virtual env with `virtualenv /vagrant/venv` and activate it with `. /vagrant/venv/bin/activate`. Install the dependencies via `pip install -e /vagrant/`.


<a id="org2eff80f"></a>

### Running tests

You can run the tests via `nosetests lslock.py`.

