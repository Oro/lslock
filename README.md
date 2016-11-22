- [lslock](#sec-1)
  - [Installation](#sec-1-1)
  - [Development](#sec-1-2)
    - [Prerequisites](#sec-1-2-1)
    - [Running tests](#sec-1-2-2)
- [s](#sec-2)

# lslock<a id="sec-1"></a>

```sh
lslock /tmp
```

    File /tmp/locks/my.lock is locked by PID 5421

`lslock` comes with two executables, `lslock` and `lslock-test`.

-   `lslock` checks a given directory (and subdirectories) for any locked files and outputs them.
-   `lslock-test` locks a given number of files in a given directory and is used to check the validity of `lslock`.

See `lslock --help` or `lslock-test --help` for parameters.

`lslock` was tested on Ubuntu 12.04, but should work on Linux with Python >= 2.7. For a leaner method of testing for locks on specific files, check out [lsof](https://linux.die.net/man/8/lsof).

## Installation<a id="sec-1-1"></a>

Make sure you have python and pip installed. If you are on a debian/ubuntu based system, you can install them via

```sh
sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential
sudo pip install --upgrade pip virtualenv
```

Then run the following to be able to run `lslock` and `lslock-test`. If you are not using a virtualenv, you might need to run this as sudo as well.

```sh
cd <path-to-repo>
virtualenv venv
. venv/bin/activate
pip install -e .
```

## Development<a id="sec-1-2"></a>

### Prerequisites<a id="sec-1-2-1"></a>

Make sure you have vagrant installed. Then run `vagrant up` in the cloned repository. You are now able to connect with `ssh vagrant@172.25.12.6:22`, password `vagrant` and find the contents of this repository at `/vagrant/`.

Create the virtual env with `virtualenv /vagrant/venv` and activate it with `. /vagrant/venv/bin/activate`. Install the dependencies via `pip install -e /vagrant/`.

### Running tests<a id="sec-1-2-2"></a>

You can run the tests via `nosetests /vagrant/lslock.py`.

# TODO s<a id="sec-2"></a>

-   Make sure that lslock actually follows symlinks. It currently errors on `lslock /`
-   For large data sets (like `/`) lslock will take a long time and probably die of memory exhaustion. Check [lsock:72ff](lslock.py) to compare files in batches instead of all at once.
-   For lslock-test, use the actuall lslock methods to check for locked files instead of circumventing the call.
