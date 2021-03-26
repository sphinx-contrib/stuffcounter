.. Stuff Counter documentation main file, created by
   sphinx-quickstart on Wed Oct 17 22:55:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Stuff Counter's documentation!
=========================================

`This project <https://framagit.org/spalax/sphinxcontrib-stuffcounter>`_ is a dummy extension meant to serve as an example for extensions writers. It illustrates the definition of a directive that:

- is automatically numbered,
- can be referenced (using ``:ref:`` or ``:numref:``).

If you want to write such a directive, study this `extension source code <https://framagit.org/spalax/sphinxcontrib-stuffcounter/blob/main/sphinxcontrib/stuffcounter/__init__.py>`_. The main points to look at (and copy) are:

- in the ``setup()`` function, the call to ``add_enumerable_node()``;
- definition of the directive (class ``StuffDirective`` in this example).

Good luck!

.. contents:: Table of contents
   :local:

.. _example:

Example
-------

.. _this:

.. stuffcounter:stuff::
   :caption: A stuff *with* a caption

   The :ref:`next stuff <that>` does not have a caption.

.. _that:

.. stuffcounter:stuff::

   This stuff does not have a caption
   (althouth :numref:`this` has one).

Source
------

The following code has produced the :ref:`above example <example>`.

.. code-block:: rst

   .. _this:

   .. stuffcounter:stuff::
      :caption: A stuff *with* a caption.

      The :ref:`next stuff <that>` does not have a caption.

   .. _that:

   .. stuffcounter:stuff::

      This stuff does not have a caption
      (althouth :numref:`this` has one).

Features
--------

- Automatic numbering.
- Directives are labelled `the Sphinx way <http://www.sphinx-doc.org/en/stable/usage/restructuredtext/roles.html#role-ref>`_.
- Directives can be referenced with ``:ref:``:

  - ``:ref:`this``` produces :ref:`this`;
  - ``:ref:`That <that>``` produces :ref:`That <that>`.

- Directives can be referenced with ``:numref:``

  - ``:numref:`that``` produces :numref:`that`;
  - ``:numref:`Stuff {number} ({name}) <this>``` produces :numref:`Stuff {number} ({name}) <this>`.

- Documentation can be rendered in HTML and LaTeX.
