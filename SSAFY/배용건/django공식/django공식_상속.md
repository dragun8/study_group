# 템플릿 상속

(페이지의 공통요소를 포함) 
하고
(하위 템플릿이 재정의 할 수 있는 공간)
을 정의하는 
기본 스켈레톤을 작성하여 상속 구조를 구축 
번거로움을 줄인다

# 상속 구조 만들기 

앱에서 상위 템플릿(base.html)을 만든후

! + enter 로 html 기본 구조 세팅

<body>
    {% block content %}
        
    {% endblock content %}
</body>


# 다른 하위 템플릿(index.html) 구성

{% extends 'articles/base.html' %}  상위 템플릿을 작성해 extends 로 상속받는다.

{% block content %}
    <h1>Hello, {{ name }} </h1>
{% endblock content %}

하위 템플릿에 작성한 글 구조들이 
상위 템플릿에 나타날 수 있도록 상속한다.


# extends tag

{% extends 상위템플릿.html %}

자식 템플릿이 부모템플릿을 확장한다
반드시 최상단에 작성해야 하며 (2개이상 사용불가)

# block tag

{% block 변수 %} {% endblock 변수 %}

하위 템플릿에서 재정의 할 수 있는 블록을 정의
(상위 템플릿에 작성하며 하위 템플릿이 작성할 수있는 공간)

# 

