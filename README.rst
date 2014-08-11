IS 210: Software Application Programming
****************************************

Welcome to IS 210: Software Application Programming

.. contents:: Table of Contents

Repository Cloning
==================

[stub]

Tests (Optional)
========================

Code and syntax checks may be optionally run on-site by the following methods.
These are the same tests that will be executed upon a pull request.

PyLint
------

Linting is a form of syntax checking that enforces conformance to best practices
in code writing and documentation. While it is generally best to strive for 100%
success in linting, there are instances where the lint checker may cause
spurious warnings or errors. If you believe you have received a spurious
notification, please wait for your instructor to assist you. They will be able
to identify unnecessary warnings.

To execute linting for all lesson packages, please type the following from the
project root:

    .. code-block:: bash

        PYTHONPATH=$PWD:$PYTHONPATH pylint -r n lessons

To test a specific lesson or file, pass it the package or filename:

    .. code-block:: bash

        PYTHONPATH=$PWD:$PYTHONPATH pylint -r n lessons/lesson_01/analyze.py

Unittest
--------

Unit tests are discrete tests that seek to test the smallest possible unit of
code in an application. Such tests are usually written to test the functionality
of a single function or parameter and are bundled together in TestCases. The
benefit of unit tests is their ability to be run quickly and guarantee that
methods and modules have predictable input and output.

This course will use unit tests extensively in order to test that student
work conforms to the expected input/output standards at a minimum.

To execute unit tests, type the following from the project root:

    .. code-block:: bash

        nosetests -w test/unit

Continuous Integration
----------------------

    .. code-block:: bash

        git clone git@github.com:cheuschober/jenkins-docker-executors.git
        cd jenkins-docker-executors
        docker build -t jenkins-docker .
        docker run --name jenkins-docker -i -t -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 -e "JENKINS_HOME=/var/jenkins_home" -v /my/persistent/store:/var/jenkins_home jenkins-docker


The above will set up a useable docker server, however, if you wish to run the tests yourself,
use the following commands.

    .. code-block:: bash

        cd ..
        git clone git@github.com:cheuschober/vartest.git
        cd vartest
        docker build -t infosys-pytest-env .
        docker run --rm -v $PWD:/var/workspace/ infosys-pytest-env /var/workspace/build.sh
