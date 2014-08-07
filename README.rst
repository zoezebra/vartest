IS 210: Software Application Programming
****************************************

Welcome to IS 210: Software Application Programming

.. contents:: Table of Contents

Repository Cloning
==================

[stub]

Running Tests (Optional)
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

        PYTHONPATH=$PYTHONPATH pylint -r n lessons

To test a specific lesson or file, pass it the package or filename:

    .. code-block:: bash

        PYTHONPATH=$PYTHONPATH pylint -r n lessons/lesson_01/analyze.py

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

        python -m unittest discover test/unit/