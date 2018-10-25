.. Stuff Counter documentation master file, created by
   sphinx-quickstart on Wed Oct 17 22:55:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Stuff Counter's documentation!
=========================================

In this documentation, there are:

- automatically numbered stuff,
- that can be referenced.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. _this:

.. stuffcounter:stuff::
   :caption: A stuff *with* a caption.

   The :ref:`next stuff <that>` does not have a caption.

.. _that:

.. stuffcounter:stuff::

   This stuff does not have a caption (althouth :numref:`this` has one).


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
