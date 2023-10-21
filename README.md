# kgbasedvalidation


# Introduction
Our software is designed for the validation of knowledge graphs and the relationships between each node.
Our architecture extracts node-to-node relationships from open-source models for computational validation. 
The large language model we utilized is called Vicuna.
![New](https://github.com/collaborativebioinformatics/kgbasedvalidation/assets/71843044/92ad26a0-e253-4a1d-92ad-65ac8670237c)
 
# Obtaining Query Data
Query data was obtained both from pubmed using edirect in conjunction with DisGeNET, where snp variant data was downloaded as tsv and used to
create triplicate data in subject predicate subject form. The csv of the SPO objects can be found in SPO.csv. The DisGeNET SPO table can be found 
below and the literature used for prompting the LLM can be found in prompt.txt. 


Table of SNPs Evaluated
|SNP| Diseases|
|--------|---------|
|rs113993960| BRONCHIECTASIS|
|rs113993960|Stenosis of duodenum|
|rs113993960| Congenital bilateral aplasia of vas deferens|
|rs113993960|Hereditary pancreatitis|
|rs113993960|Recurrent pancreatitis|
|rs113993960|Cystic Fibrosis|
|rs199473282|LONG QT SYNDROME 3|
|rs199473282|Brugada Syndrome (disorder)|
|rs199473282|Brugada Syndrome 1|
|rs199473282|Long QT Syndrome|
|rs199473282|Hereditary bundle branch system defect|
|rs121909211|Plaque, Amyloid|
|rs121909211|Familial Amyloid Polyneuropathy, Type V|
|rs121909211|Corneal dystrophy|
|rs121909211|Corneal deposit|
|rs121909211|Corneal Dystrophy, Lattice Type IIIA|
|rs121909211|Dystrophy, granular|
|rs121909211|Reis-Bucklers' corneal dystrophy|
|rs121909211|Corneal guttata|
|rs121909211|Lattice corneal dystrophy Type I|
|rs121909211|Amyloidosis|
|rs121909211|Neoplasms|
|rs121909211|Granular Dystrophy, Corneal|
|rs121909211|Thiel-Behnke corneal dystrophy|
|rs121909211|Stromal Dystrophies, Corneal|
|rs121909211|Avellino corneal dystrophy|


# Data compression
As an optional step we attempted to compress the abstracts into summaries to decrease the context window. We found that when the context was pushed past
its recommended context window size it failed to write out accurate SPO objects. Therefore using GPT3.5 or 4 to summarize key abstracts could be 
instrumental in reconstructing knowledge graph SPO objects.

# 
# What is <this software>?


#Dependencies


Entrez-Direct



#Vicuna_Model7B
git clone https://github.com/fredi-python/llama.cpp.git && cd llama.cpp && make -j && cd models && wget -c https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF/resolve/main/vicuna-7b-v1.5.Q4_K_M.gguf
