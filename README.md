# Trie-based chinese word segmenting


基於中文字典構建trie tree， 加速 Dictionary-based Segmenting

## 使用方法

python
```python
from token_tree import *

# Load dictionary data 
Data = LoadData("./dictionary.txt")

# construct trie tree
Trie_tree = Create_trie_tree(Data)


sentence = "顏面部撕裂傷，騎車汽車發生車禍致鼻樑撕裂傷"

# 斷詞
toke = tokenize(Trie_tree, sentence)
print(toke)

# 將斷詞結果字串長度只有1的進行結合並輸出
Combine(toke)

```

