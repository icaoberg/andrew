docker-omero.searcher
#####################

:date: 2018-01-05 18:00
:slug: docker-omero.searcher
:authors: icaoberg
:tags: docker, omero.searcher
:category: software
:summary: Docker container for OMERO.searcher v1.3

.. raw:: html

	<p><a href="https://camo.githubusercontent.com/0337589865afb07c0195fc22c29129fa5dd279c5/68747470733a2f2f7472617669732d63692e6f72672f6963616f626572672f646f636b65722d6f6d65726f2e73656172636865722e7376673f6272616e63683d6d6173746572" target="_blank"><img src="https://camo.githubusercontent.com/0337589865afb07c0195fc22c29129fa5dd279c5/68747470733a2f2f7472617669732d63692e6f72672f6963616f626572672f646f636b65722d6f6d65726f2e73656172636865722e7376673f6272616e63683d6d6173746572" alt="Build Status" data-canonical-src="https://travis-ci.org/icaoberg/docker-omero.searcher.svg?branch=master" style="max-width:100%;"></a><a href="https://github.com/icaoberg/docker-omero.searcher/issues"><img src="https://camo.githubusercontent.com/80917fbaa7542bb89e796376e43355a8d8243b6d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6963616f626572672f646f636b65722d6f6d65726f2e73656172636865722e737667" alt="GitHub issues" data-canonical-src="https://img.shields.io/github/issues/icaoberg/docker-omero.searcher.svg" style="max-width:100%;"></a><a href="https://github.com/icaoberg/docker-omero.searcher/network"><img src="https://camo.githubusercontent.com/c9d1f1f19806d2d7b1296a149bbb64c768a95397/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6963616f626572672f646f636b65722d6f6d65726f2e73656172636865722e737667" alt="GitHub forks" data-canonical-src="https://img.shields.io/github/forks/icaoberg/docker-omero.searcher.svg" style="max-width:100%;"></a><a href="https://github.com/icaoberg/docker-omero.searcher/stargazers"><img src="https://camo.githubusercontent.com/b1e50d3fc7e45e7e422ec339097811caf67e171c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6963616f626572672f646f636b65722d6f6d65726f2e73656172636865722e737667" alt="GitHub stars" data-canonical-src="https://img.shields.io/github/stars/icaoberg/docker-omero.searcher.svg" style="max-width:100%;"></a><a href="https://raw.githubusercontent.com/icaoberg/docker-omero.searcher/master/LICENSE" rel="nofollow"><img src="https://camo.githubusercontent.com/dcb3a3de32cb31ae6a7edf80d88747f989878809/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d47504c76332d626c75652e737667" alt="GitHub license" data-canonical-src="https://img.shields.io/badge/license-GPLv3-blue.svg" style="max-width:100%;"></a></p>

OMERO.searcher is an extension of the OMERO.web client that provides the ability to search for images by their content (e.g., subcellular patterns) rather than just by their annotations. It was developed by the Murphy group at Carnegie Mellon University.

OMERO.searcher

* finds images whose content, as reflected by subcellular location image features, is similar to one or more query images.
* can use positive and/or negative examples.
* can be iterative, meaning it allows the user to refine the search results (a process referred to as relevance feedback).

The OMERO.searcher local client is a local version of the OMERO.server plugin. 

The docker-omero.searcher is a container for OMERO.searcher local client.

Downloads
=========

* `Dockerfile <https://github.com/icaoberg/docker-omero.searcher>`_
* `Dockerhub <https://hub.docker.com/r/icaoberg/docker-omero.searcher/>`_

References
==========

* B.H. Cho, I. Cao-Berg, J.A. Bakal, and R.F. Murphy (2012) `OMERO.searcher: Content-based image search for microscope images <https://www.nature.com/articles/nmeth.2086>`_. Nature Methods 9:633-634.

* Leejay Wu, Christos Faloutsos, Katia P. Sycara, and Terry R. Payne. 2000. `FALCON: Feedback Adaptive Loop for Content-Based Retrieval <http://www.cs.cmu.edu/~christos/PUBLICATIONS/vldb2k-falcon.pdf>`_. In Proceedings of the 26th International Conference on Very Large Data Bases (VLDB '00), Amr El Abbadi, Michael L. Brodie, Sharma Chakravarthy, Umeshwar Dayal, Nabil Kamel, Gunter Schlageter, and Kyu-Young Whang (Eds.). Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 297-306.

Acknowledgments
===============

Development of OMERO.searcher has been supported by US National Institutes of Health grants GM075205 (R.F. Murphy, PI), EB008516 (K.W. Eliceiri, PI), and GM092708 (C.M. Kane, PI), and by grant 095931 from the Wellcome Trust (Jason Swedlow, PI).


