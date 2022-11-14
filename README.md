# Grammar Correction using Happy Transformer
### Fine tuned happy transformer model for effective grammar correction


Happy Transformer is a package built on top of Hugging Face’s transformer library that makes it easy to utilize state-of-the-art NLP models.

#### Link to happy transformer github repository - https://github.com/EricFillion/happy-transformer

## Dataset Used:
JFLEG (JHU FLuency-Extended GUG) is an English grammatical error correction (GEC) corpus. It is a gold standard benchmark for developing and evaluating GEC systems with respect to fluency (extent to which a text is native-sounding) as well as grammaticality. For each source document, there are four human-written corrections.

#### Data Fields
  <li>sentence: original sentence written by an English learner
  <li>corrections: corrected versions by human annotators. The order of the annotations are consistent (eg first sentence will always be written by annotator "ref0").

#### Data Splits
  <li>This dataset contains 1511 examples in total and comprise a dev and test split.
  <li>There are 754 and 747 source sentences for dev and test, respectively.
  <li>Each sentence has 4 corresponding corrected versions.

@InProceedings{napoles-sakaguchi-tetreault:2017:EACLshort,
  author    = {Napoles, Courtney  and  Sakaguchi, Keisuke  and  Tetreault, Joel},
  title     = {JFLEG: A Fluency Corpus and Benchmark for Grammatical Error Correction},
  booktitle = {Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers},
  month     = {April},
  year      = {2017},
  address   = {Valencia, Spain},
  publisher = {Association for Computational Linguistics},
  pages     = {229--234},
  url       = {http://www.aclweb.org/anthology/E17-2037}
}

@InProceedings{heilman-EtAl:2014:P14-2,
  author    = {Heilman, Michael  and  Cahill, Aoife  and  Madnani, Nitin  and  Lopez, Melissa  and  Mulholland, Matthew  and  Tetreault, Joel},
  title     = {Predicting Grammaticality on an Ordinal Scale},
  booktitle = {Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  month     = {June},
  year      = {2014},
  address   = {Baltimore, Maryland},
  publisher = {Association for Computational Linguistics},
  pages     = {174--180},
  url       = {http://www.aclweb.org/anthology/P14-2029}
}
