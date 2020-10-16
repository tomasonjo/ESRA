import sys
from esra.extractors import SciERC, SpERT


if __name__ == '__main__':
    abstracts = ["Due to the black-box nature of deep learning models, methods for explaining the models’ results are crucial to gain trust from humans and support collaboration between AIs and humans. In this paper, we consider several model-agnostic and model-specific explanation methods for CNNs for text classification and conduct three human-grounded evaluations, focusing on different purposes of explanations: (1) revealing model behavior, (2) justifying model predictions, and (3) helping humans investigate uncertain predictions. The results highlight dissimilar qualities of the various explanation methods we consider and show the degree to which these methods could serve for each purpose."]
    a = SpERT.extract(abstracts)
    b = SciERC.extract(abstracts)
    print(a)
    print(b)