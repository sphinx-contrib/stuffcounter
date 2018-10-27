.. Stuff Counter documentation master file, created by
   sphinx-quickstart on Wed Oct 17 22:55:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Stuff Counter's documentation!
=========================================

In this documentation, there are:

- automatically numbered stuff,
- that can be referenced.

This project is hosted at `framagit.org <https://framagit.org/spalax/sphinxcontrib-stuffcounter>`_ (the interesting file is `sphinxcontrib/stuffcounter/__init__.py <https://framagit.org/spalax/sphinxcontrib-stuffcounter/blob/master/sphinxcontrib/stuffcounter/__init__.py>`_.

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
