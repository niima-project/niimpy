.. _introduction-reference:

Introduction
============

What
----

Niimpy is a Python package for analyzing and quantifying behavioral data. It uses pandas to read data from disk, perform basic manipulations, provides explorative data analysis functions, offers many high-level preprocessing functions for various types of data, and has functions for behavioral data analysis.

For Who
-------

Niimpy is intended for researchers and data scientists analyzing digital behavioral data. Its purpose is to facilitate data analysis by providing a standardized replicable workflow.

Why
---

Digital behavioral studies using personal digital devices typically produce rich multi-sensor longitudinal datasets of mixed data types. Analyzing such data requires multidisciplinary expertise and software designed for the purpose. Currently, no standardized workflow or tools exist to analyze such data sets. The analysis requires domain knowledge in multiple fields and programming expertise. Niimpy package is specifically designed to analyze longitudinal, multimodal behavioral data. Niimpy is a user-friendly open-source package that can be easily expanded and adapted to specific research requirements. The toolbox facilitates the analysis phase by providing tools for data management, preprocessing, feature extraction, and visualization. The more advanced analysis methods will be incorporated into the toolbox in the future.


How
---

The toolbox is divided into four layers by functionality: 1) reading, 2) preprocessing, 3) exploration, and 4) analysis. For more information about the layers, refer the toolbox :doc:`architecture` chapter. The :doc:`quick start </quick-start>` guide is be a good place to start. More detailed demo Jupyter notebooks are provided in the :doc:`user guide </user_guide/Exploration>` chapter. Instructions for individual functions can be found under API chapter :doc:`/api/niimpy`.

This documentation has following chapters:

- Basic information about the toolbox
- Quickstart guide
- API documentation
- User guide
- Community guide
- Data documentation

Basic information contain this :ref:`introduction <introduction-reference>`, :doc:`installation instructions<installation>`, :doc:`software architecture and workflow schematics<architecture>`, and information about :doc:`compatible data </user_guide/reading>` and the :doc:`required data schema<schema>`.

The :doc:`quickstart guide </quick-start>` provides a minimal working analysis example to get you started.

The :doc:`API documentation</api/niimpy>` has all technical details, containing instruction about how to use the toolbox functions, classes, return types, arguments and such.

The :doc:`user guide</user_guide/Exploration>` provide more thorough examples of each toolbox layer functionalities. The examples are in Jupyter notebook format.

The community guide has information in the :doc:`contribution_guide<contribution_guide>`.
