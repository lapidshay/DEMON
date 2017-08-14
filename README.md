# DEMON - A local-first discovery method for overlapping communities.

![DEMON logo](http://www.giuliorossetti.net/about/wp-content/uploads/2013/07/Demon-300x233.png)


[![Build Status](https://travis-ci.org/GiulioRossetti/DEMON.svg?branch=master)](https://travis-ci.org/GiulioRossetti/DEMON)
[![Coverage Status](https://coveralls.io/repos/github/GiulioRossetti/DEMON/badge.svg?branch=master)](https://coveralls.io/github/GiulioRossetti/DEMON?branch=master)
[![pyversions](https://img.shields.io/pypi/pyversions/demon.svg)](https://badge.fury.io/py/DEMON)
[![PyPI version](https://badge.fury.io/py/demon.svg)](https://badge.fury.io/py/DEMON)
[![BCH compliance](https://bettercodehub.com/edge/badge/GiulioRossetti/DEMON?branch=master)](https://bettercodehub.com/)


Community discovery in complex networks is an interesting problem with a number of applications, especially in the knowledge extraction task in social and information networks. However, many large networks often lack a particular community organization at a global level. In these cases, traditional graph partitioning algorithms fail to let the latent knowledge embedded in modular structure emerge, because they impose a top-down global view of a network. We propose here a simple local-first approach to community discovery, able to unveil the modular organization of real complex networks. This is achieved by democratically letting each node vote for the communities it sees surrounding it in its limited view of the global system, i.e. its ego neighborhood, using a label propagation algorithm; finally, the local communities are merged into a global collection. 

## Citation
If you use our algorithm please cite the following works:

>Coscia, Michele; Rossetti, Giulio; Giannotti, Fosca; Pedreschi, Dino
> ["Uncovering Hierarchical and Overlapping Communities with a Local-First Approach"](http://dl.acm.org/citation.cfm?id=2629511)
>ACM Transactions on Knowledge Discovery from Data (TKDD), 9 (1), 2014. 

>Coscia, Michele; Rossetti, Giulio; Giannotti, Fosca; Pedreschi, Dino
> ["DEMON: a Local-First Discovery Method for Overlapping Communities"](http://dl.acm.org/citation.cfm?id=2339630)
>SIGKDD international conference on knowledge discovery and data mining, pp. 615-623, IEEE ACM, 2012, ISBN: 978-1-4503-1462-6.

## Installation


In order to install the package just download (or clone) the current project and copy the demon folder in the root of your application.

Alternatively use pip:
```bash
sudo pip install demon
```

## Implementation details

Required input format: tab separated edgelist (nodes represented with integer ids).

```
node_id0    node_id1
```

# Execution
Demon is written in python and requires the following package to run:
- python 2.7.10
- networkx
- tqdm

The algorithm can be used as standalone program as well as integrated in python scripts.

## Standalone

```bash

python demon filename epsilon -c min_com_size
```

where:
* filename: edgelist filename
* epsilon: merging threshold in [0,1]
* min_community_size: minimum size for communities (default 3 - optional)
* file_output: True if the results should be written in a file, False otherwise

The explicit removal version does not expose the ttl parameter.

## As python library
```python
import demon as d
dm = d.Demon("filename.tsc", epsilon=0.25, min_community_size=3, file_output=True)
dm.execute()
```
