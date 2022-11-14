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

## Model Architecture

Happy transformer is transfomer model build on top of Hugging Face's transformer module. Here my model specifically is trained on top of T5 model by google.

T5 is an encoder-decoder model and converts all NLP problems into a text-to-text format.    
### The T5 Framework
![image](https://user-images.githubusercontent.com/81613474/201695090-b6310713-a906-40b3-8bfa-1dc07e6357b8.png)
    
<i>A diagram of the T5 framework. Source: T5 paper.</i>

Link to T5 paper: https://github.com/google-research/text-to-text-transfer-transformer

## Installation
Steps to run the application:
    
To run this code in your local system you have to download this repository using-

    git clone https://github.com/nakulvarma2000/Grammar-correction.git

Now install the Happy Transformer module in anaconda prompt using:
    
    pip install happytransformer

Now open the download folder in terminal and run:
    
    streamlit run app.py
    
## Training and Evaluation
I have used google colab for training this model.

CPU : Xeon Processors @2.3Ghz

GPU : Tesla T4, 15110MiB

Evaluation is done with loss of the model
    
    Loss before training: 1.2658780813217163
    
    Loss after training: 0.30751293897628784
    
Here we can see that the fine-tuned model shows a significant reduction in loss.
    
## Working Example:    
![image](https://user-images.githubusercontent.com/81613474/201715393-4cfa017d-65e8-48cf-ae56-e3bc158fb42e.png)

## Further Modification’s:
  <li>Improve the model with new dataset.
    
  <li>Run the model on high end hardware to reduce prediction latency.
    
  <li>Optimize the hyperparameters by applying techniques like grid search.

## Author
#### Name: Nakul Ramesh Varma
