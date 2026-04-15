Contributing
============

If you find errors,
omissions,
inconsistencies,
or other things
that need improvement,
please create an issue_.
If you would like to add new functionality
create a `merge request`_ .
Contributions are always welcome!

.. _issue: https://gitlab.audeering.com/tools/sphinx-apipages/issues/new?issue%5BD=
.. _merge request: https://gitlab.audeering.com/tools/sphinx-apipages/-/merge_requests


Development Installation
------------------------

Instead of installing the latest release from PyPI with pip_,
you should get the newest development version from Github_::

    git clone git@github.com:audeering/sphinx-apipages.git
    cd sphinx-apipages

.. _pip: https://pip.pypa.io
.. _uv: https://docs.astral.sh/uv/
.. _Github: https://github.com/audeering/sphinx-apipages/

This way,
your installation always stays up-to-date,
even if you pull new changes
from the Gitlab repository.


Coding Convention
-----------------

We follow the PEP8_ convention for Python code
and use ruff_ as a linter and code formatter.
In addition,
we check for common spelling errors with codespell_.
Both tools and possible exceptions
are defined in :file:`pyproject.toml`.

The checks are executed in the CI using `pre-commit`_.
You can enable those checks locally by executing::

    uvx pre-commit install
    uvx pre-commit run --all-files

Afterwards ruff_ and codespell_ are executed
every time you create a commit.

You can also install ruff_ and codespell_
and call it directly::

    uvx ruff check --fix .  # lint all Python files, and fix any fixable errors
    uvx ruff format .  # format code of all Python files
    uvx codespell

It can be restricted to specific folders::

    uvx ruff check sphinx-apipages/ tests/
    uvx codespell sphinx-apipages/ tests/


.. _codespell: https://github.com/codespell-project/codespell/
.. _PEP8: http://www.python.org/dev/peps/pep-0008/
.. _pre-commit: https://pre-commit.com
.. _ruff: https://beta.ruff.rs


Building the Documentation
--------------------------

If you make changes to the documentation, you can re-create the HTML pages
using Sphinx_.
To create the HTML pages, use::

	uv run sphinx-build docs/ build/html -b html

The generated files will be available in the directory ``build/sphinx/html/``.

It is also possible to automatically check if all links are still valid::

    uv run sphinx-build docs/ build/linkcheck -b linkcheck

.. _Sphinx: http://sphinx-doc.org


Running the Tests
-----------------

To execute the tests, simply run::

    uv run pytest

pytest_ is configured inside :file:`pyproject.toml`.

.. _pytest: https://pytest.org


Creating a New Release
----------------------

New releases are made using the following steps:

#. Update ``CHANGELOG.rst``
#. Commit those changes as "Release X.Y.Z" with a pull request
#. Create an (annotated) tag with ``git tag -a vX.Y.Z``
#. Push the commit and the tag to Gitlab
