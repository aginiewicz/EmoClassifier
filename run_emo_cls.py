#!/usr/bin/env python
# -*- encoding: utf-8

from src.emo_cls import EmoClassifier

if __name__ == '__main__':
   e = EmoClassifier(is_use_emoticons=True,
                     is_dump_cls=True,
                     is_load_cached_cls=True,
                     verbose=True)

   e.terms_cls.show_most_informative_features(10)
   e.bigrams_cls.show_most_informative_features(10)
   e.trigrams_cls.show_most_informative_features(10)

   example_sents = ( ('Było super, to były moje najfajniejsze wakacje!'),
                     ('To chyba najzabawniejszy kabaret jaki oglądałem'),
                     ('Wszystkiego najlepszego i wesołych świąt'),
                     ('Niestety, mieliśmy dużego pecha i przegraliśmy'),
                     ('Zachorowałem i leżę w łóżku'),
                     ('To bardzo smutna wiadomość, nie mogę tego zrozumieć'),
                     ('Zxcjhgoiu ooijasddnakjz zczxnzbxcz qdqdqqfefw sdsdfsdfsdf'),
                     ('Przystojniaczek! :-) :D :('))

   for sent in example_sents:
      print('Sentence:', sent)
      res = e.classify(sent)
      print('Classified as: %s (%.2f)\n' % res)
