> [!NOTE]
> This is for my personal use i am trying to store some useful library here


<details>
  <summary>Installation</summary>

```sh
pip install git+https://github.com/Vivekkumar-IN/TheApi@main
```
</details>

<details>
  <summary>Advice</summary>


  ```python

  from TheApi import api

  advice = api.get_advice()
  
  print(advice)

  ```

  Result of print(advice):

  ```python
  
{'results': 'If you are feeling down, try holding a pencil between your top lip and your nose for five minutes.', 'join': '@TheTeamVivek', 'success': True}

  ```
</details>


<details>
  <summary>ChatGpt</summary>


  ```python
  from TheApi import api

  results= api.chatgpt("hello ai")

  print(results)
  ```
  Result of print(results):

  ```python

  {'results': 'Hello! How can I assist you today?', 'join': '@vk_zone', 'success': True}
  ```
</details>

<details>
  <summary>Random quote</summary> 

  ```python
  from TheApi import api

  results= api.quote()

  print(results)

  ```

  Result of print(results):

  ```python


  {'quote': 'The truest greatness lies in being kind, the truest wisdom in a happy mind.', 'author': 'Ella Wheeler Wilcox', 'join': '@vk_zone'}

  ```
</details>

<details>
  <summary>Write</summary>


  ```python

  from TheApi import api

  text = "Jai shree Ram"

  results= api.write(text)

  print(results)
  ```

  Result of print(results):

  ```python
  https://telegra.ph/file/63ff2e31cae67d511cfae.jpg

  ```
</details>


<details>
<summary>Telegraph Text</summary>

  ```python
  from TheApi import api
  title = "A Title for telegraph page"
  query = "text that you want to upload to telegraph"
  results= api.telegraph(title,query)

  print(results)

  ```
  Result of print(results):

  ```python

  {'results': 'https://telegra.ph/A-Title-for-telegraph-page-05-25', 'join': '@vk_zone', 'success': True}

   ```
</details>

<details>
<summary>Jokes</summary>


  ```python
  import json
  from TheApi import api

  response = api.get_jokes()

  data = json.loads(response)

  jokes = data["jokes"]
  num = 1
  Jokes = ""
  if isinstance(jokes, dict):
    
      for key in jokes:
          a = jokes[key]
          Jokes+=(f"{num}. {a}\n\n")
          num+=1
      print(Jokes)

  else:
      print(jokes["joke"])
  ```

  results of print
  ```python

  1. Two fish in a tank. One turns to the other and says, "Do you know how to drive this thing?"

  ```

  ```python

  response = api.get_jokes()
  # This will return 1 Jokes

  response = api.get_jokes(2)
  # This will return 1 Jokes

  # like this you can get 10 Jokes

  # if the number is greater then 10 in cause an exception returns 

  # Example : 

  import json
  from TheApi import api

  response = api.get_jokes(13)

  data = json.loads(response)

  jokes = data["jokes"]
  num = 1
  Jokes = ""
  if isinstance(jokes, dict):
    
      for key in jokes:
          a = jokes[key]
          Jokes+=(f"{num}. {a}\n\n")
          num+=1
      print(Jokes)

  else:
      print(jokes["joke"])

  # in this api.get_jokes(13) the jokes is greater then 10 so the an exception returns 


raise InvalidAmountError(amount)
  TheApi.errors.InvalidAmountError:Invalid amount of jokes requested: 11. Maximum allowed is 10. Minimum allowed is 1.

  ```
</details>

<details>
  <summary>Hindi Joke </summary>


  ```python
  from TheApi import api

  joke = api.get_hindi_jokes()

  print(joke)

  ```
  Result of print(joke):

  ```python

  हमारे समाज में रीति रिवाज और प्रथाएं इतनी महान है कि एक निकम्मा पुरुष भी विवाह के बाद परमेश्वर बन जाता है 😆🤣😋😉
  ```
</details>

<details>
  <summary>Generate Random Image</summary>

  ```python
  from TheApi import api
  image = api.gen_image()
  print(image)
  ```

  results of image

  ```python

  {'photo': 'https://images.unsplash.com/photo-1708938828404-24834946b6bf?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=720&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcxNzQxODAyOA&ixlib=rb-4.0.3&q=80&w=1280', 'join': '@TheTeamVivek', 'success': True
  ```

Also you can use with height and width

  ```python
  image = api.gen_image()
  'here you can also use height and weight '
  width=1280
  height=720
  image = api.gen_image(width, height)
  ```

</details>


This Project is Licensed under [License](https://github.com/Vivekkumar-IN/TheApi)
