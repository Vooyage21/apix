## This is for my personal use i am trying to store some useful library here


##### you can install this project by
#####  
```sh
pip install git+https://github.com/Vivekkumar-IN/External-Plugins@main
```


## ChatGpt


```python
from YUKKI import api

results= api.chatgpt("hello ai")

print(results)
```
Result of print(results):

```python

{'results': 'Hello! How can I assist you today?', 'join': '@ZeroXCoderZChat', 'success': True}
```


## Random quote

```python
from YUKKI import api

results= api.quote()

print(results)

```

Result of print(results):

```python


{'quote': 'The truest greatness lies in being kind, the truest wisdom in a happy mind.', 'author': 'Ella Wheeler Wilcox', 'join': '@ZeroXCoderZChat'}

```

## Write
```python
from YUKKI import api

text = "Jai shree Ram"

results= api.write(text)

print(results)

```

Result of print(results):

```python
https://telegra.ph/file/63ff2e31cae67d511cfae.jpg
```


## Telegraph text

### This project includes code from the [python273's telegraph](https://github.com/python273/telegraph) library, which is licensed under the MIT License.

## [MIT License](https://github.com/python273/telegraph/blob/master/LICENSE)
### [Copyright (c) 2018 python273](https://github.com/python273/telegraph/blob/master/LICENSE)


```python
from YUKKI import api
title = "A Title for telegraph page"
query = "text that you want to upload to telegraph"
results= api.telegraph(title,query)

print(results)

```
Result of print(results):

```python

{'results': 'https://telegra.ph/A-Title-for-telegraph-page-05-25', 'join': '@ZeroXCoderZChat', 'success': True}

```



This Project is Licensed under [License](https://github.com/Vivekkumar-IN/External-Plugins/blob/main/LICENSE)