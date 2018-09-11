from keras import models
from keras.layers import Input, Dense
from keras import layers

from ..model import Model

from ...lib.text_lib import *

from ...lib.general_lib import *

import numpy as np

import random



class Text_Generation_Model(Model):
    def __init__(self, model_path = None):
        """Initializes a model.
        
        Arguments:
            Model {class} -- A super class of neural network models.
        
        Keyword Arguments:
            model_path {str} -- A path of model file. (default: {None})
        """        
        if type(model_path) != type(None):
            Model.__init__(self, model_path)
        else:
            Model.__init__(self)

    def prepare_train_data(self, train_text, sentences, next_characters, max_sentence_size = None):
        if hasattr(self.model, 'output_dictionary') == False:
            sorted_unique_characters = get_unique_characters(train_text)
            char_index_dict = dict((c, i) for i, c in enumerate(sorted_unique_characters))
        else:
            try:
                char_index_dict = reverse_dict(self.model.output_dictionary)
            except:
                raise TypeError('invalid output_dictionary')
        
        number_of_sentences = len(sentences)
        number_of_unique_characters = len(char_index_dict)        
        if hasattr(self, 'input_shape') == True:
            max_sentence_size = self.input_shape[0]
        else:
            self.input_shape = (max_sentence_size, number_of_unique_characters)
            output_dictionary = reverse_dict(char_index_dict)
            self.model = self.create_model( len( output_dictionary ) )
            self.set_output_dictionary( output_dictionary )

        data_shape = (number_of_sentences, self.input_shape[0], self.input_shape[1])
        target_shape = (number_of_sentences, self.input_shape[1])
        self.x = np.zeros(data_shape, dtype=np.bool)
        self.y = np.zeros(target_shape, dtype=np.bool)

        print('initializing training data')
        for index_of_sentence, sentence in enumerate(sentences):
            for index_of_char, sentence_char in enumerate(sentence):
                self.x[ index_of_sentence, index_of_char, char_index_dict[sentence_char] ] = 1
            next_character_of_sentence = next_characters[index_of_sentence]
            self.y[ index_of_sentence, char_index_dict[next_character_of_sentence] ] = 1
        print('initialization finished')
    
    def create_model(self, num_classes):
        input_layer = Input(shape = self.input_shape)
        lstm1 = layers.LSTM(512)(input_layer)
        output_layer = Dense(num_classes, activation='softmax')(lstm1)
        return models.Model(inputs=input_layer, outputs=output_layer)

    def train(self,
            batch_size = None,
            steps_per_epoch = None,
            epochs = 1,
            verbose = 1,
            callbacks = None,
            shuffle = True):
            self.compile_model(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
            self.model.fit(self.x, self.y, batch_size=batch_size, steps_per_epoch=steps_per_epoch, epochs = epochs, verbose = verbose, callbacks = callbacks, shuffle = shuffle)

    def choose_index_from_possibility_array(self, possibility_array, diversity = 0.2):
        possibility_array = np.asarray(possibility_array).astype('float64')
        log_array = np.log(possibility_array) / diversity
        exp_array = np.exp(log_array)
        changed_possibility_array = exp_array / np.sum(exp_array)
        multinomial_choice_array = np.random.multinomial(1, changed_possibility_array, 1)
        return np.argmax(multinomial_choice_array)

    def generate_text(self, starting_sentence, generated_text_size):
        char_index_dict = reverse_dict(self.model.output_dictionary)
        sentence_array_shape = (1, self.input_shape[0], self.input_shape[1])

        sentence = starting_sentence
        generated_text = sentence
        for i in range(generated_text_size):
            sentence_array = np.zeros(sentence_array_shape, dtype=np.bool)
            for index_of_char, sentence_char in enumerate(sentence):
                sentence_array[ 0, index_of_char, char_index_dict[sentence_char] ] = 1
            
            prediction_result = self.predict(sentence_array, predict_classes = False)
            possibility_array = prediction_result[0]
            chosen_index = self.choose_index_from_possibility_array(possibility_array)
            next_char = self.model.output_dictionary[chosen_index]
            generated_text += next_char
            sentence = sentence[1:] + next_char
        return generated_text

    


