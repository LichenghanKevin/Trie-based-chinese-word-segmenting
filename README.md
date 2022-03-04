# Trie-based-word-segmenting


基於中文字典構建trie tree， 加速 Dictionary-based Segmenting

## 使用方法

python
```python
from token_tree import *

# Load dictionary data 
Data = LoadData("./dictionary.txt")

# construct trie tree
Trie_tree = createTokenTree(Data)

sentence = "顏面部撕裂傷，騎車汽車發生車禍致鼻樑撕裂傷"
NER_output = tokenize(Trie_tree, sentence)
print(NER_output)

"""
NER_output=
[
  ['token1', token1_start_index, token1_end_index],
  ['token2', token2_start_index, token2_end_index],
  ['token3', token3_start_index, token3_end_index],
]

"""

```

## output

將Trie tree 寫入 display.txt

```python
from NER_Tree import *

# Load dictionary data and construct trie tree
Data = LoadData("./dictionary.txt")
Trie_tree = createTokenTree(Data)

# Display trie tree
# Write to display.txt
Trie_tree.disp()
```
