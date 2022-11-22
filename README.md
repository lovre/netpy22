# NetPy '22: Introduction to Network Science in Python

###### Workshop instructor

[Lovro Šubelj](http://lovro.fri.uni-lj.si), University of Ljubljana

###### Workshop schedule

Saturday, 3rd December 2022, 9:00-16:00 (with breaks and lunch)

###### Workshop location

Lecture room 3 at [UL FRI](http://www.fri.uni-lj.si), Večna pot 113, Ljubljana, Slovenia

###### High-level description

This workshop is primarily aimed at Python programmers, either academics, professionals or students, that wish to learn the basics of modern network science and practical analyses of real networks such as social and information networks. Familiarity with the basics of probability theory and statistics, linear algebra, and machine learning is strongly encouraged.

The workshop is based on masters level course [Network Analysis](https://lovro.fri.uni-lj.si/posters/frinets.pdf) offered at the University of Ljubljana, Faculty of Computer and Information Science.

###### Recommended prerequisites

It is recommended that attendees bring a laptop with a working installation of [Python](http://www.python.org), and in particular [NetworkX](http://networkx.github.io), [CDlib](http://cdlib.readthedocs.io) and [node2vec](https://github.com/eliorc/node2vec) packages. Alternatively, you can work with any other network analysis package such as [igraph](http://igraph.org), [graph-tool](http://graph-tool.skewed.de) or [SNAP.py](http://snap.stanford.edu/snappy/). For visualization of smaller networks, it can be useful to have an installation of some network analysis software such as [Gephi](http://gephi.org) or [visone](http://visone.info).

###### Tentative syllabus
1. From classical graph theory to **modern network science** (20 min)
2. **Large-scale structure** of real networks and **graph models** (60+20 min)
3. Measures of **node importance** and **link analysis** algorithms (45+15 min)
4. Network **community structure**, blockmodeling and **core-periphery** (60+20 min)
5. Network **visualization**, **machine learning** and some applications (45+15 min)

+ **Hands-on**: Abstraction, centrality, communities, visualization, learning etc. 

###### Networks data

All networks are available in Pajek format.

+ [Simple toy example network](https://github.com/lovre/netpy22/blob/master/nets/toy.net) (5 nodes)
+ [Zachary's karate club network](https://github.com/lovre/netpy22/blob/master/nets/karate.net) (34 nodes)
+ [Davis's southern women network](https://github.com/lovre/netpy22/blob/master/nets/women.net) (32 nodes)
+ [Lusseau's bottlenose dolphins network](https://github.com/lovre/netpy22/blob/master/nets/dolphins.net) (62 nodes)
+ [Game of Thrones character appearance network](https://github.com/lovre/netpy22/blob/master/nets/got-appearance.net) (107 nodes)
+ [Human diseasome network by common symptoms](https://github.com/lovre/netpy22/blob/master/nets/diseasome.net) (117 nodes)
+ [Conflicts and alliances between world nations](https://github.com/lovre/netpy22/blob/master/nets/wars.net) (180 nodes)
+ [Game of Thrones character kills network](https://github.com/lovre/netpy22/blob/master/nets/got-kills.net) (284 nodes)
+ [Ljubljana public bus transport network](https://github.com/lovre/netpy22/blob/master/nets/lpp.net) (416 nodes)
+ [SICRIS computer scientists co-authorship network](https://github.com/lovre/netpy22/blob/master/nets/sicris.net) (680 nodes)
+ [US airplane traffic transport network](https://github.com/lovre/netpy22/blob/master/nets/transport.net) (1,323 nodes)
+ [Norwegian boards of directors network](https://github.com/lovre/netpy22/blob/master/nets/directors.net) (1,421 nodes)
+ [Java software class dependency network](https://github.com/lovre/netpy22/blob/master/nets/java.net) (1,516 nodes)
+ [Ingredients network by common compounds](https://github.com/lovre/netpy22/blob/master/nets/ingredients.net) (1,525 nodes)
+ [Map of Darknet from Tor network](https://github.com/lovre/netpy22/blob/master/nets/darknet.net) (7,178 nodes)
+ [IMDb actors collaboration network](https://github.com/lovre/netpy22/blob/master/nets/imdb.net) (17,577 nodes)
+ [Human protein-protein interaction network](https://github.com/lovre/netpy22/blob/master/nets/ppi.net) (19,634 nodes)
+ [WikiLeaks cable reference network](https://github.com/lovre/netpy22/blob/master/nets/wikileaks.net) (52,416 nodes)
+ [Internet map of autonomous systems](https://github.com/lovre/netpy22/blob/master/nets/internet.net) (75,885 nodes)
+ [Amazon product copurchase network](https://github.com/lovre/netpy22/blob/master/nets/amazon.net) (262,111 nodes)
+ [Paper citation network of APS](https://github.com/lovre/netpy22/blob/master/nets/aps.net) (438,943 nodes)
+ [Small part of Google web graph](https://github.com/lovre/netpy22/blob/master/nets/google.net) (875,713 nodes)
+ [Road/highway network of Texas](https://github.com/lovre/netpy22/blob/master/nets/texas.net) (1,379,917 nodes)

###### Networks atlas

Coscia, M., [The atlas for the aspiring network scientist](https://www.networkatlas.eu), e-print _arXiv:210100863v2_, pp. 761 (2021).

## 1. Classical graph theory → modern network science

###### Brief description

Introduction of networks and selected **motivational examples**. From **classical graph theory** to social network analysis and **modern network science**. Network perspectives in different **fields of science**.

![transportation](figs/transportation.png)

###### Lecture slides

+ [**Networks introduction and examples**](https://github.com/lovre/netpy22/blob/master/lectures/1-1-intro.pdf)
+ [**Historical development of network science**](https://github.com/lovre/netpy22/blob/master/lectures/1-2-history.pdf)
+ [**Network perspectives through science**](https://github.com/lovre/netpy22/blob/master/lectures/1-3-perspects.pdf) (later on)

###### Book chapters

+ Ch. 1: [Introduction](http://networksciencebook.com/chapter/1) in Barabási, A.-L., [_Network Science_](http://networksciencebook.com) (Cambridge University Press, 2016).
+ Ch. 1-5: Introduction etc. in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 1: [Overview](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch01.pdf) in Easley, D. & Kleinberg, J., [_Networks, Crowds, and Markets_](https://www.cs.cornell.edu/home/kleinber/networks-book/) (Cambridge University Press, 2010).

###### Selected must-reads

+ Barabási, A.-L., The network takeover, _Nat. Phys._ **8**(1), 14-16 (2012).
+ Motter, A.E. & Yang, Y., The unfolding and control of network cascades, _Phys. Today_ **70**(1), 33-39 (2017).
+ Cramer, C., Porter, M.A. et al., [_Network Literacy: Essential Concepts and Core Ideas_](https://sites.google.com/a/binghamton.edu/netscied/Network-Literacy-low-res.pdf?attredirects=0) (Creative Commons Licence, 2015).

###### Selected papers

+ Newman, M.E.J., The physics of networks, _Phys. Today_ **61**(11), 33-38 (2008).
+ Cimini, G., Squartini, T. et al., [The statistical physics of real-world networks](https://arxiv.org/abs/1810.05095), _Nat. Rev. Phys._ **1**(1), 58-71 (2019).
+ Newman, M.E.J., Communities, modules and large-scale structure in networks, _Nat. Phys._ **8**(1), 25-31 (2012).
+ Vespignani, A., Modelling dynamical processes in complex socio-technical systems, _Nat. Phys._ **8**(1), 32-39 (2012).
+ Hegeman, T. & Iosup, A., [Survey of graph analysis applications](https://arxiv.org/abs/1807.00382), e-print _arXiv:180700382v1_, pp. 23 (2018).
+ Hidalgo, C.A., Disconnected, fragmented, or united? A trans-disciplinary review of network science, _Appl. Netw. Sci._ **1**, 6 (2016).

## 2. Large-scale network structure and graph models

###### Brief description

Classical **graph theory** and modern **network analysis**. **Random graphs** and **network structure**, and scale-free and small-world networks. **Network representations**, data formats and repositories. 

![smallworld](figs/smallworld.png)

###### Lecture slides

+ [**Graph theory and network analysis**](https://github.com/lovre/netpy22/blob/master/lectures/2-1-networkology.pdf)
+ [**Random graphs and network structure**](https://github.com/lovre/netpy22/blob/master/lectures/2-2-randoms.pdf)
+ [**Scale-free and small-world network models**](https://github.com/lovre/netpy22/blob/master/lectures/2-3-models.pdf)
+ [**Network representations, formats and data**](https://github.com/lovre/netpy22/blob/master/lectures/2-4-represent.pdf)

###### Hands-on analysis

+ [**Network structure and random graphs**](https://github.com/lovre/netpy22/blob/master/labs/structure.pdf) ([starter.py](https://github.com/lovre/netpy22/blob/master/scripts/structure-starter.py))

###### Book chapters

+ Ch. 2: [Graph theory](http://networksciencebook.com/chapter/2), Ch. 3.8-3.9: [Small worlds etc.](http://networksciencebook.com/chapter/3) & Ch. 4-5: [Scale-free property etc.](http://networksciencebook.com/chapter/4) in Barabási, A.-L., Network Science (Cambridge University Press, 2016).
+ Ch. 6: Mathematics of networks & Ch. 12-15: Random graphs etc. in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 2: [Graphs](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch02.pdf), Ch. 18: [Power laws etc.](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch18.pdf) & Ch. 20: [Small-world phenomenon](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch20.pdf) in Easley, D. & Kleinberg, J., Networks, Crowds, and Markets (Cambridge University Press, 2010).

###### Selected must-reads

+ Newman, M.E.J., Watts, D.J. & Strogatz, S.H., [Random graph models of social networks](https://www.pnas.org/content/pnas/99/suppl_1/2566.full.pdf?sid=2662d769-c2c0-48a5-afe5-6da549153812), _P. Natl. Acad. Sci. USA_ **99**, 2566-2572 (2002).
+ Ugander, J., Karrer, B. et al., [The anatomy of the Facebook social graph](https://arxiv.org/abs/1111.4503), e-print _arXiv:1111.4503v1_, pp. 17 (2011).
+ Backstrom, L., Boldi, P. et al., [Four degrees of separation](https://arxiv.org/abs/1111.4570), In: _Proceedings of WebSci '12_ (Evanston, IL, USA, 2012), pp. 45-54.

###### Selected papers

+ Erdős, P. & Rényi, A., [On random graphs I](http://ftp.math-inst.hu/~p_erdos/1959-11.pdf), _Publ. Math. Debrecen_ **6**, 290-297 (1959).
+ Milgram, S., The small world problem, Psychol. Today 1(1), 60-67 (1967). 
Granovetter, M.S., The strength of weak ties, _Am. J. Sociol._ **78**(6), 1360-1380 (1973).
+ Watts, D.J. & Strogatz, S.H., Collective dynamics of 'small-world' networks, _Nature_ **393**(6684), 440-442 (1998).
+ Barabási, A.-L. & Albert, R., Emergence of scaling in random networks, _Science_ **286**(5439), 509-512 (1999).
+ Faloutsos, M., Faloutsos, P. & Faloutsos, C., On power-law relationships of the Internet topology, _Comput. Commun. Rev._ **29**(4), 251-262 (1999).
+ Albert, R., Jeong, H. & Barabási, A.-L., Error and attack tolerance of complex networks, _Nature_ **406**(6794), 378-382 (2000).
+ Dorogovtsev, S.N. & Mendes, J.F.F., [Evolution of networks](https://arxiv.org/abs/cond-mat/0106144), _Adv. Phys._ **51**(4), 1079-1187 (2002).
+ Clauset, A., Shalizi, C.R. & Newman, M.E.J., [Power-law distributions in empirical data](https://arxiv.org/abs/0706.1062), _SIAM Rev._ **51**, 661-703 (2009).
+ De Domenico, M. & Arenas, A., [Modeling structure and resilience of the dark network](https://arxiv.org/abs/1612.01284), _Phys. Rev. E_ **95**(2), 022313 (2017).
+ Broido, A.D. & Clauset, A., [Scale-free networks are rare](https://www.nature.com/articles/s41467-019-08746-5), _Nat. Commun._ **10**(1), 1017 (2019).
+ Barabási, A.-L., [Love is all you need](https://uploads-ssl.webflow.com/58bcae2c9d6c401e73a26fed/5aa01d3e24eebb000199a0a2_loveisallyouneed.pdf), reply to e-print _arXiv:1801.03400v1_, pp. 6 (2018).
+ Holme, P., [Rare and everywhere](https://www.nature.com/articles/s41467-019-09038-8), _Nat. Commun._ **10**(1), 1016 (2019).

## 3. Measures of node importance and link analysis

###### Brief description

Node importance and **measures of centrality**, i.e. clustering coefficient, spectral analysis, closeness and betweenness centrality, and **link analysis** algorithms. Link importance and **measures of bridging**, i.e. betweenness, embeddedness and topological overlap.

![centrality](figs/centrality.png)

###### Lecture slides

+ [**Node importance and measures of centrality**](https://github.com/lovre/netpy22/blob/master/lectures/3-1-centrality.pdf)
+ [**Link analysis algorithms for web page importance**](https://github.com/lovre/netpy22/blob/master/lectures/3-2-analysis.pdf)
+ [**Link importance and measures of bridging**](https://github.com/lovre/netpy22/blob/master/lectures/3-3-bridging.pdf) (tentative)

###### Hands-on analysis

+ [**IMDb actors collaboration network**](https://github.com/lovre/netpy22/blob/master/labs/position.pdf) ([starter.py](https://github.com/lovre/netpy22/blob/master/scripts/position-starter.py))

###### Book chapters

+ Ch. 7: Measures and metrics in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 14: [Link analysis and Web search](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch14.pdf) in Easley, D. & Kleinberg, J., [_Networks, Crowds, and Markets_](https://www.cs.cornell.edu/home/kleinber/networks-book/) (Cambridge University Press, 2010).
+ Ch. 14-15: Classical node centrality etc. in Estrada, E. & Knight, P.A., [_A First Course in Network Theory_](https://global.oup.com/academic/product/a-first-course-in-network-theory-9780198726463?cc=si&lang=en&) (Oxford University Press, 2015).

###### Selected must-reads

+ Jeong, H., Mason, S.P. et al., Lethality and centrality in protein networks, _Nature_ **411**, 41-42 (2001).
+ Jensen, P., Morini, M. et al., [Detecting global bridges in networks](https://arxiv.org/abs/1509.08295), _J. Complex Netw._ **4**(3), 319-329 (2015).
+ Tong, H., Faloutsos, C. & Pan, J.-Y., Fast random walk with restart and its applications, In: _Proceedings of ICDM ’06_ (Washington, DC, USA, 2006), pp. 613-622.

###### Selected papers

+ Freeman, L., A set of measures of centrality based on betweenness, _Sociometry_ **40**(1), 35-41 (1977).
+ Bonacich, P., Power and centrality: A family of measures, _Am. J. Sociology_ **92**(5), 1170-1182 (1987).
+ Kleinberg, J., Authoritative sources in a hyperlinked environment, _J. ACM_ **46**(5), 604-632 (1999).
+ Franceschet, M. & Bozzo, E., [A theory on power in networks](https://arxiv.org/abs/1510.08332), e-print _arXiv:1510.08332v2_, pp. 19 (2016).
+ Everett, M.G. & Valente, T.W., Bridging, brokerage and betweenness, _Soc. Networks_ **44**, 202-208 (2016).
+ Berkhin, P., A survey on PageRank computing, _Internet Math._ **2**(1), 73-120 (2005).

## 4. Network clustering and mesoscopic structure

###### Brief description

Network **community structure**, blockmodeling and **core-periphery structure**. Graph partitioning, **community detection**, stochastic block models and **k-core decomposition**.

![community](figs/community.png)

###### Lecture slides

+ [**Node clustering and community structure**](https://github.com/lovre/netpy22/blob/master/lectures/4-1-community.pdf)
+ [**Graph partitioning and community detection**](https://github.com/lovre/netpy22/blob/master/lectures/4-2-clustering.pdf)
+ [**Blockmodeling and stochastic block models**](https://github.com/lovre/netpy22/blob/master/lectures/4-3-blockmodeling.pdf)
+ [**Core-periphery decomposition**](https://github.com/lovre/netpy22/blob/master/lectures/4-4-cores.pdf) (tentative)

###### Hands-on analysis

+ [**Community structure and k-cores**](https://github.com/lovre/netpy22/blob/master/labs/clusters.pdf) ([starter.py](https://github.com/lovre/netpy22/blob/master/scripts/clusters-starter.py))

###### Book chapters

+ Ch. 9: [Communities](http://networksciencebook.com/chapter/9) in Barabási, A.-L., [_Network Science_](http://networksciencebook.com) (Cambridge University Press, 2016).
+ Ch. 7.12-7.13: Homophily etc. & Ch. 11: Graph partitioning in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 21: Communities in networks in Estrada, E. & Knight, P.A., [_A First Course in Network Theory_](https://global.oup.com/academic/product/a-first-course-in-network-theory-9780198726463?cc=si&lang=en&) (Oxford University Press, 2015).
+ Ch. 3: [Strong and weak ties](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch03.pdf) in Easley, D. & Kleinberg, J., [_Networks, Crowds, and Markets_](https://www.cs.cornell.edu/home/kleinber/networks-book/) (Cambridge University Press, 2010).

###### Selected must-reads

+ Hric, D., Darst, R.K. & Fortunato, S., [Community detection in networks: Structural communities versus ground truth](https://arxiv.org/abs/1406.0146), _Phys. Rev. E_ **90**(6), 062805 (2014).
+ Fortunato, S. & Hric, D., [Community detection in networks: A user guide](https://arxiv.org/abs/1608.00163), _Phys. Rep._ **659**, 1-44 (2016).
+ Schaub, M.T., Delvenne, J.-C. et al., [The many facets of community detection in complex networks](https://arxiv.org/abs/1611.07769), _Appl. Netw. Sci._ **2**, 4 (2017).
+ Rossetti, G., Milli, L., & Cazabet, R., [CDlib: A python library to extract, compare and evaluate communities from complex networks](https://link.springer.com/article/10.1007/s41109-019-0165-9), _Appl. Netw. Sci._ **4**(1), 1–26 (2019).

###### Selected papers

+ Granovetter, M.S., The strength of weak ties, _Am. J. Sociol._ **78**(6), 1360-1380 (1973).
+ Girvan, M. & Newman, M.E.J., [Community structure in social and biological networks](https://arxiv.org/abs/cond-mat/0112110), _P. Natl. Acad. Sci. USA_ **99**(12), 7821-7826 (2002).
+ Fortunato, S., [Community detection in graphs](https://arxiv.org/abs/0906.0612), _Phys. Rep._ **486**(3-5), 75-174 (2010).
+ Leskovec, J., Lang, K.J. et al., [Community structure in large networks](https://arxiv.org/abs/0810.1355), _Internet Math._ **6**(1), 29–123 (2009).
+ Borgatti, S.P. & Everett, M.G., Models of core/periphery structures, _Soc. Networks_ **21**(4), 375–395 (2000).
+ Holme, P., [Core-periphery organization of complex networks](https://arxiv.org/abs/physics/0506035), _Phys. Rev. E_ **72**(4), 46111 (2005).
+ Newman, M.E.J. & Leicht, E.A., [Mixture models and exploratory analysis in networks](https://arxiv.org/abs/physics/0611158), _P. Natl. Acad. Sci. USA_ **104**(23), 9564 (2007).
+ Raghavan, U.N., Albert, R. & Kumara, S., [Near linear time algorithm to detect community structures in large-scale networks](https://arxiv.org/abs/0709.2938), _Phys. Rev. E_ **76**(3), 036106 (2007).
+ Rosvall, M. & Bergstrom, C.T., Maps of random walks on complex networks reveal community structure, _P. Natl. Acad. Sci. USA_ **105**(4), 1118-1123 (2008).
+ Blondel, V.D., Guillaume, J.-L. et al., [Fast unfolding of communities in large networks](https://arxiv.org/abs/0803.0476), _J. Stat. Mech._, P10008 (2008).
+ Traag, V.A., Waltman, L. & Van Eck, N.J., [From Louvain to Leiden: Guaranteeing well-connected communities](https://www.nature.com/articles/s41598-019-41695-z), _Sci. Rep._ **9**, 5233 (2019).
+ Peixoto, T.P., [Bayesian stochastic blockmodeling](http://arxiv.org/abs/1705.10225), e-print _arXiv:170510225v7_, pp. 44 (2018).

## 5. Network visualization, machine learning and applications

###### Brief description

Force-directed node layouts and **network visualization**. Modern **machine learning** with network data (e.g. node embeddings and graph neural networks). Selected applications of network analysis (i.e. automobile **insurance fraud** and tracking **scientific knowledge**).

![collisions](figs/collisions.png)

###### Lecture slides

+ [**Network layout and visualization**](https://github.com/lovre/netpy22/blob/master/lectures/5-1-visuals.pdf)
+ [**Machine learning with network data**](https://github.com/lovre/netpy22/blob/master/lectures/5-2-learning.pdf)
+ [**Insurance fraud detection**](https://github.com/lovre/netpy22/blob/master/lectures/5-x-fraud.pdf) (application)
+ [**Tracking scientific knowledge**](https://github.com/lovre/netpy22/blob/master/lectures/5-y-science.pdf) (application)

###### Demo analysis

+ Node features and embeddings ([demo.py](https://github.com/lovre/netpy22/blob/master/scripts/learning-demo.py), [demo.ows](https://github.com/lovre/netpy22/blob/master/scripts/learning-demo.ows))

###### Selected must-reads

+ Grover, A. & Leskovec, J., [node2vec](https://arxiv.org/abs/1607.00653), In: _Proceedings of KDD ’16_ (San Francisco, CA, USA, 2016), pp. 855-864.
+ Zanin, M., Papo, D. et al., [Combining complex networks and data mining: Why and how](https://arxiv.org/abs/1604.08816), _Phys. Rep._ **635**, 1-44 (2016).
+ Makarov, I., Kiselev, D. et al., [Survey on graph embeddings and its applications to machine learning problems](https://peerj.com/articles/cs-357/), _PeerJ Comput. Sci._ **7**, e357 (2021).
+ Hamilton, W.L., [_Graph Representation Learning_](https://www.cs.mcgill.ca/~wlh/grl_book/), (Morgan and Claypool, 2020).

###### Selected papers

+ Getoor, L. & Diehl, C.P., Link mining: A survey, _SIGKDD Explor._ **7**(2), 3–12 (2005).
+ Getoor, L., Friedman, N. et al., Learning probabilistic models of link structure, _J. Mach. Learn. Res._ **3**, 679–707 (2002).
+ Neville, J. & Jensen, D., Iterative classification in relational data, In: _Proceedings of SRL ’00_ (Austin, TX, USA, 2000), pp. 13–20.
+ Macskassy, S.A. & Provost, F., Classification in networked data: A toolkit and a univariate case study, _J. Mach. Learn. Res._ **8**, 935-983 (2007).
+ Bhagat, S., Cormode, G. & Muthukrishnan, S., Node classification in social networks, e-print _arXiv:1101.3291v1_, pp. 37 (2011).
+ Šubelj, L., Exploratory and predictive tasks of network community detection, In: _Proceedings of NetSci '15_ (Zaragoza, Spain, 2015), p. 1.
+ Hric, D., Peixoto, T.P. & Fortunato, S., [Network structure, metadata and the prediction of missing nodes](https://arxiv.org/abs/1604.00255), _Phys. Rev. X_ **6**(3), 031038 (2016).
+ Perozzi, B., Al-Rfou, R. & Skiena, S., [DeepWalk](https://arxiv.org/abs/1403.6652), In: _Proceedings of KDD ’14_ (New York, NY, USA, 2014), pp. 701-710.
+ Figueiredo, D.R., Ribeiro, L.F.R. & Saverese, P.H.P., [struc2vec](https://arxiv.org/abs/1704.03165), In: _Proceedings of KDD ’17_ (Halifax, Canada, 2017), pp. 1–9.
+ Peel, L., [Graph-based semi-supervised learning for relational networks](https://arxiv.org/abs/1612.05001), In: _Proceedings of SDM ’17_ (Houston, TX, USA, 2017), pp. 1-11.

<span> </span>

+ Eades, P., A heuristic for graph drawing, _Congressus Numerantium_ **42**, 146-160 (1984).
+ Kamada, T. & Kawai, S., An algorithm for drawing general undirected graphs, _Inform. Process. Lett._ **31**(1), 7-15 (1989).
+ Fruchterman, T.M.J. & Reingold, E.M., Graph drawing by force-directed placement, _Softw: Pract. Exper_. **21**(11), 1129-1164 (1991).
+ Kobourov, S.G., [Spring embedders and force directed graph drawing algorithms](https://arxiv.org/abs/1201.3011), e-print _arXiv:1201.3011v1_, pp. 23 (2012).
+ Gibson, H., Faith, J. & Vickers, P., A survey of two-dimensional graph layout techniques for information visualisation, _Infor. Visual._ **12**(3-4), 324-357 (2013).
+ Ma, K.-L. & Muelder, C.W., Large-scale graph visualization and analytics, _Computer_ **46**(7), 39-46 (2013).

<span> </span>

+ Šubelj, L., Furlan, Š. & Bajec, M., [An expert system for detecting automobile insurance fraud using social network analysis](https://arxiv.org/abs/1104.3904), _Expert Syst. Appl._ **38**(1), 1039-1052 (2011).
+ Šubelj, L., Waltman, L. et al., [Intermediacy of publications](https://arxiv.org/abs/1812.08259), _R. Soc. Open Sci._, pp. 19 (2019). 
