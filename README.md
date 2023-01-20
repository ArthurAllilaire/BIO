A set of children’s blocks, each illustrated with a single different letter, have been chained together in a
line. They have been arranged so that it is not possible to find three (not necessarily adjacent) letters,
from left to right, that are in alphabetical order.
For example, if there are four blocks (A, B, C and D) the possible block-chains are:
ADCB BADC BDAC BDCA CADB
CBAD CBDA CDAB CDBA DACB
DBAC DBCA DCAB DCBA

Write a program that enumerates block-chains.
Your program should input a single integer l (1 ≤ l ≤ 19) indicating that the blocks are
illustrated with the first l letters of the alphabet, followed by a word p of between 1
and l uppercase letters indicating (in order) the leftmost letters of the block chain. p
will only contain letters take from the first l letters of the alphabet and will not
contain any duplicates.
You should output a single integer giving the number of possible block-chains that
begin with p.

Sample Input:
4 CB
OUTPUT:
2
