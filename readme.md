# Ngram counter

Set of functions that counts words/tokens ar n-grams in a file (1. and 2.).

# Conll context manager

A context manager for specially prepared conll files (3.).

# Original assignment content

1. Napisać funkcję, która zlicza wystąpienia wszystkich słów w pliku tekstowym. Umożliwić wyświetlenie n najczęściej
   występujących słów _z remisami_ (tzn. jeśli słowa na pozycji n+1 i n+2 wystąpiły tyle samo razy co to na pozycji n,
   to także mają zostać wyświetlone). Przetestować na załączonym pliku potop.txt.

2. Napisać funkcje, które zliczają wystąpienia wszystkich n-gramów słownych w pliku tekstowym. Również umożliwić
   wyświetlenie czołówki z remisami.
   N-gram to KAŻDE n występujących po sobie słów (albo innych jednostek, w zależności od kontekstu). Np. zdanie "Ala ma
   kota" ma 2 digramy: "Ala ma" i "ma kota".

3. Napisać context manager do obsługi pliku .conll. Iteracja po pliku powinna zwracać kolejne linie w postaci krotki
   bądź listy.
   Przykładowe użycie:

   with open_conll('ala_ma_kota.conll') as infile:
   for token in infile:
   print(token)

Przykładowe wyjście:
('Ala', 'Ala', 'noun')
('ma', 'mieć', 'verb')
('kota', 'kot', 'noun')
('.', '.', 'punct')

Termin oddania: czw. 23.11.2023 20:00