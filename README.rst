
py-image-comparer
=================

Compares two images using `Siamese Network <https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf>`_ trained from a `Pytorch Implementation <https://github.com/joeyism/siamese-pytorch>`_

Installation
------------

To install, run

.. code-block:: bash

   pip install image-comparer

Usage
-----

CLI
^^^

.. code-block:: bash

   image-compare

which wil show the follow help screen

.. code-block::

   usage: image-compare [-h] [--threshold THRESHOLD] Image1-Path Image2-Path

For example, you can compare two images with

.. code-block:: bash

   image-compare tests/images/kobe.jpg tests/images/kobe2.jpg

which gives the result

.. code-block::

   kobe.jpg and kobe2.jpg are not similar

Programmatically
^^^^^^^^^^^^^^^^

With PIL

.. code-block:: python

   import image_comparer
   from PIL import Image

   image = Image.open("test/kobe.jpg")
   image2 = Image.open("test/kobe2.jpg")
   image_comparer.is_similar(image, image2, threshold=0.5)

or with OpenCV

.. code-block:: python

   import image_comparer
   import cv2

   image = cv2.imread("test/kobe.jpg")
   image2 = cv2.imread("test/kobe2.jpg")
   image_comparer.is_similar(image, image2, threshold=0.5)

Development
-----------

Installation
^^^^^^^^^^^^

.. code-block:: bash

   pip install -r requirements-test.txt

Tests
^^^^^

To run tests, run

.. code-block:: bash

   pytest
