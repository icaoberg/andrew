Cellorganizer v2.7.0
####################

:date: 2018-03-07 18:00
:slug: cellorganizer_v2.7.0
:authors: icaoberg
:tags: matlab
:category: software
:summary: CellOrganizer v2.7.0 Release!

.. figure:: {filename}/images/cellorganizer.png
    :align: left

Release Highlights
==================

Features
--------

* Included new model class/type constructive_geometry/half-ellipsoid
* Included new model class/type:framework/pca
* Included support for constructing models with OME.TIFF containing regions of interest

Enhancements
------------

* img2slml now checks the combination of model class and type for every submodel before attempting to extract parameters from images
* Added demo3D44 to show how to synthesize from a model class/type constructive_geometry/half-ellipsoid
* Added a battery of unit test for demos using Matlab testing framework
* Added demo3D45 to show how to use OME.TIFF files with ROIs
* Added demo2D05, demo2D06, demo2D07 to show how to train and synthesize from a classtype framework/pca model

Downloads
=========

* `CellOrganizer v2.7 <http://www.cellorganizer.org/cellorganizer-2-7-0/>`_

Requirements
============

* Matlab 2015b or newer
* Image Processing Toolbox for Matlab
* Statistics and Machine Learning Toolbox/Statistics Toolbox
* SymBiology Toolbox
* Curve Fitting Toolbox

Compatibility
=============

CellOrganizer releases for the 2.0 family have been tested on

* Matlab 2015a/Ubuntu 12.04
* Matlab 2014a/Ubuntu 12.04
* Matlab 2016a/MacOSX El Capitan
