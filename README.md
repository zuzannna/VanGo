# VanGo

While completing PhD at NYU I often spent my weekends at numerous galleries and art museums in NYC, and I quickly realized that there is simply too much to see at any given time. 

__There should be a way to curate your trip depending on your personal preferences__

That is how the idea of VanGo was born. During Insight, a program that helps PhDs transition from academia to careers as data scientists, I got to spend three weeks developing VanGo from scratch. I started with building the database, then I designed and implemented the algorithm in Python, and finally developed the front-end using Flask and AWS. Let me walk you through the steps.

![VanGo_main](VanGo_main)

As a data source, I used curatorial descriptions of paintings and drawings which I queried in SPARQL (a language for semantic databases, used by cultural heritage institutions) from British Museum's collection. Their database is awesome, by the way! After some web scraping, and text processing (such as tokenizing and lemmatizing), I ran principal component analysis (PCA) to reduce the dimensionality of my dataset and basically describe every drawing and painting as a vector of numbers corresponding to the components of the PCA. Importantly, it will only return matches for words initially used in curatorial descriptions, so if you try anything like "cool" or "stuff" it won't work (finding a way to bridge these words with expert descriptions would be another awesome project). In other words, the search results will reflect similarities between artworks which were discovered by PCA - which don't necessarily reflect "the grand truth". What's particularly cool about this collection is that the majority of works originates from Asia, so the themes discovered by my algorithm reflect those favored by artists. Happy exploring!


