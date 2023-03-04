Medical eponyms
===============

![License](https://img.shields.io/github/license/dtoddenroth/medicaleponyms)

![thumbnail](https://user-images.githubusercontent.com/20538437/212569365-a109ce29-823e-458e-a55b-4bd197ca59b2.png)

This repository accompanies an evaluation of 
[SciBERT](https://github.com/allenai/scibert)-based classifiers 
of medical eponymy in scientific abstracts, which has been submitted 
to [EFMI's Medical Informatics Europe conference 2023](https://www.mie2023.org/). 

The `annotations/` folder in this repository contains medical eponyms 
and counterexamples in the format of the 
[Brat](https://brat.nlplab.org/) annotation tool, 
labeled in a convenience sample of 1,079 Pubmed abstracts. 
Of 13,659 annotations, 1,582 (11.6%) refer to eponyms, 
with the three most frequent ones being 
*Fabry* (227x), *Alzheimer* (148x) and *Parkinson* (81x). 

Character positions in `.ann` files refer to concatenations of
publication titles and abstracts, separated by two newlines 
(assembled via `f"{title}\n\n{abstract}"`, and encoded as `utf-8`). 

Since some annotated abstracts may be subject to copyright restrictions, 
no text files are reproduced in this repository. 
Usage that adheres to 
[NCBI policies](https://www.ncbi.nlm.nih.gov/home/about/policies/)
may allow downloading and converting the corresponding `.txt` files via the 
[Entrez interface](https://www.ncbi.nlm.nih.gov/books/NBK25501/) 
from NLM sources with a python script that is provided under `downloadabstracts/`. 

Also note that annotations reflect data exported in early 2023, 
while NLM records can in principle be updated. 
To account for potential discrepancies between annotations and 
modified text files, only unmodified `.txt` files 
are copied to the `annotations/` folder. 
The following commands are geared to downloading abstracts in `.xml` format, 
converting titles plus abstracts into `.txt` files, 
and re-assembling unchanged (checksum-compatible) `.txt` files 
and `.ann` files in the `annotations/` folder: 

```
git clone https://github.com/dtoddenroth/medicaleponyms.git
cd medicaleponyms/downloadabstracts
python3 downloadabstracts.py
```
The `bratconfig/` folder contains configuration files for visualizing 
annotations in [Brat](https://brat.nlplab.org/). 
