from ..esra.transformers.conjunction_relations_merger import merge_conjuction_relation
  
def test_merge_conjuction_relation():
    data_in = {'entities': [['Task', 'language understanding'],
                        ['Method', 'convolutional architecture'],
                        ['Method', 'Dynamic Convolutional Neural Network'],
                        ['Task', 'semantic modelling'],
                        ['Method', 'Dynamic k-Max Pooling'],
                        ['Method', 'global pooling operation'],
                        ['OtherScientificTerm', 'feature graph'],
                        ['OtherScientificTerm', 'parse tree'],
                        ['Task', 'multi-class sentiment prediction'],
                        ['Task', 'six-way question classification'],
                        ['Task', 'Twitter sentiment prediction'],
                        ['OtherScientificTerm', 'distant supervision'],
                        ['Abbreviation', 'DCNN']],
            'relations': [['HYPONYM-OF', 2, 1],
                        ['HYPONYM-OF', 2, 1],
                        ['USED-FOR', 4, 2],
                        ['USED-FOR', 7, 2],
                        ['CONJUNCTION', 8, 9],
                        ['CONJUNCTION', 8, 10],
                        ['CONJUNCTION', 9, 10],
                        ['USED-FOR', 11, 10],
                        ['REFER-TO', 12, 2]]}
    data_out = {'entities': [['Task', 'language understanding'], 
                             ['Method', 'convolutional architecture'],
                             ['Method', 'Dynamic Convolutional Neural Network'],
                             ['Task', 'semantic modelling'], 
                             ['Method', 'Dynamic k-Max Pooling'], 
                             ['Method', 'global pooling operation'], 
                             ['OtherScientificTerm', 'feature graph'], 
                             ['OtherScientificTerm', 'parse tree'], 
                             ['Task', 'multi-class sentiment prediction'], 
                             ['Task', 'six-way question classification'], 
                             ['Task', 'Twitter sentiment prediction'], 
                             ['OtherScientificTerm', 'distant supervision'], 
                             ['Abbreviation', 'DCNN']], 
                'relations': [['HYPONYM-OF', 2, 1], 
                              ['HYPONYM-OF', 2, 1],
                              ['USED-FOR', 4, 2], 
                              ['USED-FOR', 7, 2], 
                              ['USED-FOR', 11, 10], 
                              ['REFER-TO', 12, 2], 
                              ['USED-FOR', 11, 8], 
                              ['USED-FOR', 11, 9]]}
    assert data_out == merge_conjuction_relation(data_in)