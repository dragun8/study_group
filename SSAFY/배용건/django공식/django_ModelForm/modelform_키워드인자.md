# modelform 키워드인자 구성

data 는 첫번째에 위치한 키워드 인자이기 때문에
생략이 가능함

```python
form = ArticleForm(request.POST)



#이것과 같은 코드는

form = ArticleForm(data=request.POST)

# 그렇기에 생략이 가능

```

```python
form = ArticleForm(instance=article)

# 이부분에서 instance를 생략한다면

form = ArticleForm(article)

# 그냥 data에 article을 담은 의미밖에 안됨