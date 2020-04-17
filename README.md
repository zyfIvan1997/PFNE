# SGNS-PFNE: PATI Filtered Segmentation-free word Embedding.
**SGNS-PFNE** is an open source implementation of PFNE with skip-gram with negative sampling.

## Environment
  * Linux(Tested with Ubuntu Linux release 16.04)

## Requirment
  * Python3
  * gcc(>=5)
  * Numpy
  * argparse
  * pickle
  
## Contents
  1. data/: Pre-processed corpous.
  2. ngram2~ngram6/: Computing PATI score from 2-gram to 6-gram.
  3. embedding/: Training distributed word vectors based on SGNS-PFNE.
 
## Reference
  1. Oshikiri, T. (2017). Segmentation-Free Word Embedding for Unsegmented Languages. In Proceedings of EMNLP2017.
  2. Mikolov, T., Corrado, G., Chen, K., & Dean, J. (2013). Efficient Estimation of Word Representations in Vector Space. In Proceedings of ICLR2013.
