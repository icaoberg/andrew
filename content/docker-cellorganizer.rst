docker-cellorganizer
####################

:date: 2018-03-15 18:00
:slug: docker-cellorganizer
:authors: icaoberg
:tags: docker, cellorganizer, matlab
:category: software
:summary: Docker container for CellOrganizer binaries

|

.. raw:: html
	
	<p><a href="https://travis-ci.org/icaoberg/docker-cellorganizer" target="_blank"><img src="https://camo.githubusercontent.com/f1e1fc11bd5e86faa233a3ed8ce1921afdd2bd00/68747470733a2f2f7472617669732d63692e6f72672f6963616f626572672f646f636b65722d66616c636f6e2e7376673f6272616e63683d6d6173746572" alt="Build Status" data-canonical-src="https://travis-ci.org/icaoberg/docker-cellorganizer.svg?branch=master" style="max-width:100%;">
	</a><a href="https://github.com/icaoberg/docker-cellorganizer/issues"><img src="https://camo.githubusercontent.com/18454ba1d561cd14242f9ca5554fe7b9ea2ae01c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6963616f626572672f646f636b65722d66616c636f6e2e737667" alt="GitHub issues" data-canonical-src="https://img.shields.io/github/issues/icaoberg/docker-cellorganizer.svg" style="max-width:100%;"></a><a href="https://github.com/icaoberg/docker-cellorganizer/network"><img src="https://camo.githubusercontent.com/c31380e6240058e65af62478f0b40c34e070179d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6963616f626572672f646f636b65722d66616c636f6e2e737667" alt="GitHub forks" data-canonical-src="https://img.shields.io/github/forks/icaoberg/docker-cellorganizer.svg" style="max-width:100%;"></a><a href="https://github.com/icaoberg/docker-cellorganizer/stargazers"><img src="https://camo.githubusercontent.com/6aaa97ee6d96ef6dfe05b5c7a08fbda25410c1a0/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6963616f626572672f646f636b65722d66616c636f6e2e737667" alt="GitHub stars" data-canonical-src="https://img.shields.io/github/stars/icaoberg/docker-cellorganizer.svg" style="max-width:100%;"></a><a href="https://raw.githubusercontent.com/icaoberg/docker-cellorganizer/master/LICENSE" rel="nofollow"><img src="https://camo.githubusercontent.com/dcb3a3de32cb31ae6a7edf80d88747f989878809/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d47504c76332d626c75652e737667" alt="GitHub license" data-canonical-src="https://img.shields.io/badge/license-GPLv3-blue.svg" style="max-width:100%;"></a></p>

.. figure:: {filename}/images/docker-logo.png
    :align: left

The CellOrganizer project provides tools for

* learning generative models of cell organization directly from images
* storing and retrieving those models
* synthesizing cell images (or other representations) from one or more models

Model learning captures variation among cells in a collection of images. Images used for model learning and instances synthesized from models can be two- or three-dimensional static images or movies.

The first release of CellOrganizer for Docker contains binaries for the two main functions

* *img2slml*, the top-level function to train generative models of cell morphology, and
* *slml2img*, the top-level function to generate simulated instances from a trained generative model.

Downloads
=========

* `Dockerfile <https://github.com/icaoberg/docker-cellorganizer>`_
* `Dockerhub <https://hub.docker.com/r/murphylab/docker-cellorganizer/>`_

References
==========

* Robert Murphy (2016) Building cell models and simulations from microscope images. Methods 96: 33-39 (Special Issue on High-throughput Imaging).
* Robert Murphy (2012) CellOrganizer: Image-derived Models of Subcellular Organization and Protein Distribution. Methods in Cell Biology 110: 179-193.
* Robert Murphy (2010) Communicating Subcellular Distributions. Cytometry Part A 77A:686-692. This review provides a perspective on methods for estimating pattern fractions and learning generative models.  It addresses the critical problem of representing information learned about subcellular organization for comparison between cell and tissue types and for use in systems simulations.



