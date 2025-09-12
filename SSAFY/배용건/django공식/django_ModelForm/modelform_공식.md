# modelform 유형

```python
<create 로직>

from .forms import ArticleForm  # 폼을 불러온다

def creat(request):  #요청이 오면 함수가 열린다
  form = ArticleForm(request.POST)
   # 사용자가 보낸 데이터를 DB에 넣는다 
   #(ex. 글쓰기, 회원가입, 로그인등 숨겨야하는 데이터는 POST로 처리한다)
  if form.is_valid(): 
    # 사용자가 입력한 데이터가 올바른지 확인한다
    # 데이터가 올바르다면..
    article = form.save()  
    # 입력한 데이터를 DB에 저장. 
    # 저장된 데이터를 article 변수에 담는다. 
    return redirect('articles:detail', article.pk)
  context = {
    'form': form,
  }
  # 폼 유효성 검사를 성공했을때 detail 페이지를 보여주기 위해
  # redirect를 사용 (views가 실행)

  return render(request, 'articles/new.html', context) 
  # 그화면을 다시 보여주는 이유는 폼 유효성 검사 실패했을 경우 
  
```

#

```python

<edit 로직>

def edit(request, pk):  
  #edit 함수로 요청과 글번호를 받는다(글을 수정하고 싶다는 요청이 오면 실행)
  article = Article.objects.get(pk=pk)  
  # DB에서 pk 번호(id)에 맞는 글을 가져온다
  form = ArticleForm(instance=article) #수정폼에 기존내용 채우기
  context = {
    'article': article,
    'form': form,
  }
  
  return render(request, 'articles/edit.html', context)
  # edit.html 페이지를 열어서 보여주기 
```


#

```python

<update 로직>

def update(request, pk): # 함수 요청과 글 번호를 받는다
  article = Article.objects.get(pk=pk) # pk 에 맞는 글을 가져온다
  form = ArticleForm(request.POST, instance=article)
  # 사용자가 보낸 데이터를 DB에 넣고 수정폼에 기존내용을 채우기
  if form.is_valid(): # 유효성 검사를 진행하고
    form.save() # 유효성 검사가 맞으면 입력한 데이터를 DB에 저장한다
    return redirect('articles:detail', article.pk)
    # 유효성 맞으면 detail 이동 views 실행
  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/edit.html', context)
   # 유효성이 맞지 않다면 edit.html 페이지를 열어서 보여주기

```

```python

<new + create view 함수 로직 >

def create(request):
  if request.method == 'POST': # 사용자가 글을 제출했다면 
    form = ArticleForm(request.POST) 
    # 사용자가 제출한 데이터를 ArticleForm에 담는다
    if form.is_valid(): # 유효성 검사를 진행한다
      article = form.save() # 사용자가 입력한 데이터를 DB 에 저장한다
      return redirect('articles:detail', article.pk) # 저장했다면 해당글의 상세페이지로 이동
  else: # 사용자가 빈 글을 제출했다면
    form = ArticleForm()  # 빈폼을 만든다
  context = {
    'form': form, #context에 담아 
  }
  return render(request, 'articles/new.html', context)
  # new.html 을 보여준다
  ```

  ```python

  <edit + update view 함수 로직>

  def update(request, pk):
    article = Article.objects.get(pk=pk) #pk에 맞는 글을 가져온다
    if request.method == 'POST': # 사용자가 글을 제출했다면
      form = ArticleForm(request.POST, instance=article)
      # 사용자가 제출한 데이터를 DB에 넣고 수정한 글에 기존 글을 채운다
      if form.is_valid(): # 유효성 검사를 통과햇다면
        form.save() # 사용자가 제출한 데이터를 DB 에 저장
        return redirect('articles:detail', article.pk)
        # DB 를 저장했으면 detail 페이지로 이동
    else:
      form = ArticleForm(instance=article) # 기존 글을 담은 데이터를 보여준다
    context = {
      'article': article,
      'form': form,
    }
    return render(request, 'articles/update.html', context)
    # update.html 화면을 열어준다
  ```
