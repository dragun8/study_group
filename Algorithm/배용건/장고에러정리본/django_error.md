Django 에러 코드별 일반적인 원인 & 대응




1. ModuleNotFoundError: No module named 'xxx'

원인: 모듈을 찾을 수 없음

대응:

앱 내부라면 from .models import Article 처럼 상대경로 사용

외부 라이브러리라면 pip install xxx 확인

INSTALLED_APPS에 앱 등록 여부 확인



2. ImportError: cannot import name 'XXX'

원인: 모듈은 있는데 해당 클래스/함수가 없음

대응:

오타 확인 (Atricle → Article)

모듈 안에 실제 정의돼 있는지 확인

순환 import 발생 여부 확인



3. AttributeError: 'XXX' object has no attribute 'yyy'

원인: 없는 속성 호출

대응:

objects 오타 확인 (object ❌ → objects ✅)

모델 필드명과 호출하는 이름 일치 확인

dir(객체)로 가능한 속성 확인



4. DoesNotExist: ModelName matching query does not exist.

원인: .get() 조건을 만족하는 데이터 없음

대응:

DB에 해당 데이터가 있는지 확인 (Model.objects.all())

.filter().first()로 안전하게 처리

요청한 pk 값이 올바른지 확인



5. TemplateDoesNotExist: xxx.html

원인: 템플릿 파일을 찾을 수 없음

대응:

앱/templates/앱/index.html 구조 확인

settings.py → TEMPLATES['APP_DIRS'] = True 확인

INSTALLED_APPS에 앱 등록 여부 확인



6. NoReverseMatch: 'xxx' is not a registered namespace

원인: {% url 'xxx' %}에 해당 경로 없음

대응:

urls.py에서 app_name = "앱이름" 추가

include(..., namespace="앱이름") 확인

템플릿에서는 {% url '앱이름:뷰이름' %} 사용



7. IntegrityError

원인: DB 제약조건 위반

null=False인데 값이 없음

unique=True인데 중복 삽입

대응:

모델 정의 다시 확인

입력 데이터 유효성 검사

migration 정상 반영 확인



8. staticfiles.W004

원인: STATICFILES_DIRS에 지정된 폴더가 없음

대응:

프로젝트 루트에 static/ 폴더 생성

당장 필요 없으면 STATICFILES_DIRS 주석 처리



9. OperationalError: no such table: ...

원인: DB 테이블 없음

대응:

python manage.py makemigrations

python manage.py migrate

앱이 INSTALLED_APPS에 포함되어 있는지 확인



10. SyntaxError

원인: 파이썬 문법 오류

대응:

: (콜론) 빠짐

괄호 안 닫힘

from .models import 뒤에 클래스 이름 빠짐


🔑 디버깅 습관

에러 메시지 마지막 줄 집중하기

File "...", line X → 코드 줄 번호 찾아보기

수정 후 서버 재시작 (CTRL+C → python manage.py runserver)

DB/쿼리 문제면 python manage.py shell_plus에서 직접 실행해보기
