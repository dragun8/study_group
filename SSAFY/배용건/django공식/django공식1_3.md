# render 함수

# 작성 순서 

urls.py - views.py - templates(--.html)


# render 함수 작성시

render(request, template_name, context)

request - 응답을 생성하는데 사용되는 요청 객체

template_name - 템플릿 경로 이름

context - 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)

Model - 데이터와 관련된 로직을 관리

Template - 레이아웃과 화면을 처리

View - Model 과 Template 관련한 로직을 처리해서 응답을 반환


# views.py 에서 작성시 

def 템플릿(request):
    context = {
        '옥수수': '옥수수',
    }
    return render(request, 경로/템플릿.html, context)

# Variable(변수)

위에 views.py 작성시 context 는 딕셔너리 데이터를 담은 변수로 render 함수의 3번째인자에 작성

해당 변수의 key 값을 {{ 옥수수 }}로 작성해 template 에서 변수로 사용함
' . ' dot을 사용해 변수 속성에 접근할수 있음
{{ 옥수수.attribute }}

# Filters

표시할 변수를 수정할때 사용 (변수 + | + 필터)
chained(연결)이 가능하며 일부 필터는 인자를 받기도 함

{{ 옥수수|filter }}
{{ name|truncatewords:30 }}

# Tags

반복 또는 논리를 수행

일부는 시작과 종료 태그가 필요

{% tag %}

{% if %} {% endif %}


