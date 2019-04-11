Flake8 pytest plugin
====================

Check for uses of Django-style assert-statements in tests. So no more ``self.assertEqual(a, b)``,
but instead ``assert a == b``.

This module provides a plugin for ``flake8``, the Python code checker.


Installation
------------

You can install or upgrade ``flake8-pytest`` with these commands::

  $ pip install flake8-pytest
  $ pip install --upgrade flake8-pytest


Plugin for Flake8
-----------------

When both ``flake8`` and ``flake8-pytest`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    2.0 (pep8: 1.4.5, flake8-pytest: 1.1, pyflakes: 0.6.1)


