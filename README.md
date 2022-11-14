# Grammar Correction using Happy Transformer
### Fine tuned happy transformer model for effective grammar correction


Happy Transformer is a package built on top of Hugging Face’s transformer library that makes it easy to utilize state-of-the-art NLP models.

#### Link to happy transformer github repository - https://github.com/EricFillion/happy-transformer

## Dataset Used:
JFLEG (JHU FLuency-Extended GUG) is an English grammatical error correction (GEC) corpus. It is a gold standard benchmark for developing and evaluating GEC systems with respect to fluency (extent to which a text is native-sounding) as well as grammaticality. For each source document, there are four human-written corrections.

#### Data Fields
  sentence: original sentence written by an English learner
  corrections: corrected versions by human annotators. The order of the annotations are consistent (eg first sentence will always be written by annotator "ref0").

### Data Splits
  This dataset contains 1511 examples in total and comprise a dev and test split.
  There are 754 and 747 source sentences for dev and test, respectively.
  Each sentence has 4 corresponding corrected versions.
