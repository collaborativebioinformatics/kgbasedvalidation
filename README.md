# kgbasedvalidation

![WFTemp](https://github.com/collaborativebioinformatics/kgbasedvalidation/assets/71843044/f048b14d-ce45-4257-8618-4f156ff48005)


# What is <this software>?

This code base takes a biological gene, pathology, or snp query and creates a 
knowledge graph of biological data. From this knowledge graph it samples pubmed
articles and uses these articles to train a vicuna model and generate new weights
and edges from the original knowledge graph. Then this new knowledge graph will be scored.
