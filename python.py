PART 0. 환경 세팅 (2 STEP)
STEP 1. 파이썬 + 에디터 설치
할 것: Python 3.11 이상 설치 / VS Code 설치 / Python 확장 설치
실습: 터미널에서 python --version 확인 → hello.py 만들어서 print("hello") 실행
통과 조건: 터미널에서 python hello.py로 실행된다
자주 막히는 곳: 윈도우는 설치 시 "Add Python to PATH" 체크 필수. 안 하면 python을 못 찾음
STEP 2. 주피터 노트북 익히기
할 것: VS Code에서 .ipynb 파일 만들기 (또는 Google Colab)
실습: 셀 3개 만들어 각각 실행, 셀 순서 바꿔 실행해보기
통과 조건: 셀 단위 실행과 변수가 셀 사이에 유지된다는 걸 안다
왜 중요: 앞으로 데이터 분석·ML은 전부 노트북에서 해. 지금 익혀두면 편해

지금부터 학습은 노트북, 나중에 프로젝트는 .py 파일. 둘 다 사용

PART 1. 변수와 기본 자료형 (4 STEP)
STEP 3. 변수와 타입
배울 것: 변수 할당, int, float, str, bool, type(), 형변환 int() str() float()
실습:
변수 5개 만들어 각각 type() 출력
"10" + 5 실행해서 에러 보기 → 형변환으로 고치기
통과 조건: "5" + "5"와 5 + 5의 결과 차이를 설명한다
STEP 4. 연산자
배울 것: + - * /, //(몫), %(나머지), **(제곱), +=, 비교 연산자, and or not
실습:
17 // 5, 17 % 5 결과 확인
짝수 판별을 % 2 == 0으로
(3 > 2) and (5 < 1) 결과 예측하고 확인
통과 조건: %로 짝/홀 판별과 배수 판별을 할 수 있다
STEP 5. 문자열 다루기 ⭐
배울 것: 인덱싱 s[0], 슬라이싱 s[1:4], len(), upper(), lower(), strip(), split(), replace(), join(), in
실습:
"  Hello Python  "을 strip → split → 단어 리스트로
"2024-01-15"를 split("-")으로 연/월/일 분리
"apple" in "pineapple" 확인
통과 조건: 문자열을 나누고 합치는 걸 검색 없이 한다
왜 중요: 나중에 데이터 전처리의 절반이 문자열 정리야
STEP 6. f-string과 출력
배울 것: f"{변수}", 소수점 포맷 f"{x:.2f}", 천단위 f"{x:,}"
실습: 이름·나이·점수를 받아 "홍길동님(25세)의 점수는 87.50점입니다" 형태로 출력
통과 조건: f-string으로 소수점 2자리 포맷을 쓴다
왜 중요: 앞으로 모든 출력에 씀. +로 문자열 붙이는 습관은 버려
PART 2. 컬렉션 자료형 (5 STEP)
STEP 7. 리스트 ⭐
배울 것: 생성, 인덱싱, 슬라이싱, append(), insert(), remove(), pop(), len(), sort(), sorted(), reverse(), in
실습:
점수 리스트 만들어 최댓값·최솟값·평균 구하기 (max, min, sum)
리스트 정렬 후 상위 3개만 슬라이싱
sort()와 sorted()의 차이 확인 (원본 변경 여부)
통과 조건: 리스트 요소를 추가·삭제·정렬한다. list[-1]이 마지막 요소인 걸 안다
STEP 8. 딕셔너리 ⭐⭐
배울 것: {key: value}, 값 접근 d['key'], d.get('key'), 추가/수정, del, keys(), values(), items(), in
실습:
학생 정보 dict 만들기 {"name": "홍길동", "age": 20, "scores": [90, 85]}
없는 키를 d['없음']로 접근해 에러 보기 → get()으로 해결
items()로 반복문 돌며 전부 출력
중첩 dict: dict 안에 dict, dict 안에 list 만들어보기
통과 조건: 중첩된 dict에서 값을 꺼낸다. 예: data['user']['scores'][0]
왜 중요: 이게 가장 중요해. API 응답, JSON, 설정 파일, LLM 요청/응답이 전부 dict야. 7단계 OpenAI API도 {"role": "user", "content": "..."} 형태고, RAG의 메타데이터도 dict야. 여기서 시간을 더 써도 돼
STEP 9. 튜플과 세트
배울 것: 튜플 () 불변, 언패킹 a, b = (1, 2), 세트 set() 중복 제거, 집합 연산
실습:
리스트의 중복 제거를 set()으로
함수가 값 2개를 반환할 때 언패킹으로 받기
통과 조건: 리스트·튜플·세트·딕셔너리를 언제 쓸지 한 줄씩 말한다
STEP 10. 자료형 선택 훈련
실습: 아래 상황에 맞는 자료형 고르기 (정답을 주석으로 근거와 함께)
학생 30명의 시험 점수 → ?
학생 이름으로 점수 찾기 → ?
방문한 도시 목록에서 중복 제거 → ?
좌표 (x, y) → ?
통과 조건: 4개 다 근거를 대고 고른다
왜 중요: 이 판단이 코드 품질의 시작이야
STEP 11. 컬렉션 종합 실습
실습: 학생 5명의 정보를 dict의 리스트로 만들기
  students = [
      {"name": "A", "kor": 90, "eng": 85},
      ...
  ]

→ 전체 평균, 최고점 학생 이름 구하기

통과 조건: 반복문 없이도 구조가 머리에 그려진다
왜 중요: 이 구조가 그대로 나중의 DataFrame이야. Pandas는 사실상 이걸 표로 만든 것
PART 3. 제어문 (5 STEP)
STEP 12. if / elif / else
배울 것: 조건문, 들여쓰기 규칙, 중첩 if
실습: 점수 → 학점(A/B/C/D/F) 변환
통과 조건: 들여쓰기 에러(IndentationError)를 스스로 고친다
STEP 13. for 반복문 ⭐
배울 것: for x in 리스트, range(), enumerate(), zip(), dict 순회
실습:
리스트 순회하며 합계 구하기
enumerate로 번호와 값 동시 출력
zip으로 이름 리스트와 점수 리스트 짝짓기
dict를 items()로 순회
통과 조건: enumerate와 zip을 검색 없이 쓴다
STEP 14. while과 흐름 제어
배울 것: while, break, continue, 무한루프 주의
실습: 숫자 맞히기 게임 (정답 맞힐 때까지 반복, 힌트 제공)
통과 조건: break와 continue의 차이를 안다
STEP 15. 컴프리헨션 ⭐
배울 것: [x*2 for x in nums], 조건 붙이기 [x for x in nums if x > 5], dict 컴프리헨션
실습:
1~20 중 짝수만 리스트로
문자열 리스트를 전부 대문자로
같은 결과를 일반 for문으로도 작성해서 비교
통과 조건: 간단한 for문을 컴프리헨션으로 바꿔 쓴다
왜 중요: 데이터 처리 코드에 도배돼 있어. 못 읽으면 남의 코드를 못 봐
STEP 16. 제어문 종합
실습: STEP 11의 students 리스트에서
평균 80점 이상인 학생 이름만 리스트로 (컴프리헨션)
과목별 평균 계산 (반복문)
성적순 정렬 (sorted(key=...))
통과 조건: 세 문제를 막힘 없이 푼다
PART 4. 함수 (4 STEP)
STEP 17. 함수 기본
배울 것: def, 매개변수, return, 반환값 없는 함수
실습: 평균 구하는 함수, 최대값 찾는 함수 직접 구현 (max() 안 쓰고)
통과 조건: return이 있는 함수와 없는 함수의 차이를 안다
STEP 18. 함수 심화
배울 것: 기본값 인자, 키워드 인자, *args, **kwargs, 여러 값 반환
실습:
def greet(name, greeting="안녕") 형태
통계값 3개를 튜플로 반환하고 언패킹으로 받기
통과 조건: 기본값 인자를 쓴 함수를 작성한다
STEP 19. 스코프와 타입 힌트
배울 것: 지역변수 vs 전역변수, 타입 힌트 def f(x: int) -> str:
실습: STEP 17~18의 함수 전부에 타입 힌트 붙이기
통과 조건: 함수 안에서 만든 변수를 밖에서 못 쓴다는 걸 안다
왜 중요: 6단계 FastAPI가 타입 힌트 기반으로 동작해. 지금 습관 들이면 나중이 쉬워
STEP 20. 함수로 리팩터링
실습: STEP 16에서 짠 코드를 함수 3개로 쪼개기
  def get_high_scorers(students, cutoff=80) -> list
  def get_subject_average(students, subject) -> float
  def sort_by_score(students) -> list
통과 조건: 함수 이름만 보고 뭘 하는지 알 수 있다
왜 중요: 여기서 "코드를 짜는 사람"이 돼. ML 프로젝트의 train.py도 이 감각으로 만들어
PART 5. 파일과 예외 (4 STEP)
STEP 21. 파일 읽고 쓰기
배울 것: with open(path, 'r', encoding='utf-8'), read(), readlines(), write(), 모드 r/w/a
실습: 텍스트 파일에 여러 줄 쓰고, 다시 읽어서 줄 수 세기
통과 조건: with를 쓰는 이유(자동 닫힘)를 안다
자주 막히는 곳: 한글 깨지면 encoding='utf-8' 빠진 것
STEP 22. CSV 다루기
배울 것: csv.reader, csv.DictReader, csv.DictWriter
실습: STEP 11의 students를 CSV로 저장 → 다시 읽어서 dict 리스트로 복원
통과 조건: CSV ↔ dict 리스트 왕복이 된다
왜 중요: 3단계 Pandas가 이걸 자동화한 거야. 원리를 알고 가면 이해가 빨라
STEP 23. JSON 다루기 ⭐
배울 것: json.dump, json.load, json.dumps, json.loads, ensure_ascii=False
실습: 중첩 dict를 JSON 파일로 저장 → 다시 로드 → 값 수정 → 재저장
통과 조건: dump(파일)와 dumps(문자열)의 차이를 안다
왜 중요: API 통신의 표준 형식. 6·7단계 전체가 JSON 위에서 돌아가
STEP 24. 예외 처리
배울 것: try / except / else / finally, 예외 종류(ValueError, KeyError, FileNotFoundError, ZeroDivisionError), raise
실습:
숫자 입력받아 나누기 → 0 입력, 문자 입력 각각 처리
없는 파일 열기 → FileNotFoundError 처리
통과 조건: 에러 종류별로 다른 메시지를 출력한다
자주 하는 실수: except:로 전부 삼키기 → 어떤 에러인지 모르게 됨. 종류를 명시해
PART 6. 클래스 (3 STEP)

여기는 깊게 안 가도 돼. "남의 라이브러리 코드를 읽을 수 있는 수준"이 목표야.

STEP 25. 클래스 기본
배울 것: class, __init__, self, 인스턴스 변수, 메서드
실습: Student 클래스 만들기 (이름·점수 저장, 평균 구하는 메서드)
통과 조건: self가 "이 객체 자신"이라는 걸 안다
STEP 26. 클래스 활용
배울 것: __str__, 클래스 변수, 상속 기초
실습: STEP 11의 dict 리스트를 Student 객체 리스트로 바꾸기
통과 조건: print(객체)가 읽을 만하게 나온다
STEP 27. 라이브러리 코드 읽기
실습: scikit-learn 문서에서 LogisticRegression() 사용 예제를 보고 "이건 클래스고, 이건 메서드고, 이건 속성이다" 구분하기
통과 조건: model.fit()이 메서드고 model.coef_가 속성인 걸 구분한다
왜 중요: 클래스를 배우는 진짜 이유가 이거야. 직접 설계하기보다 남이 만든 걸 잘 쓰기 위해서
PART 7. 모듈과 환경 (4 STEP)
STEP 28. 표준 라이브러리
배울 것: import, from X import Y, random, datetime, os, math
실습:
random.sample로 로또 번호 생성
datetime.now()로 현재 시각, strftime으로 포맷
os.path.join으로 경로 만들기
통과 조건: 필요한 기능을 표준 라이브러리에서 찾아 쓴다
STEP 29. 내 모듈 만들기
배울 것: .py 파일 분리, import 내파일, if __name__ == "__main__":
실습: STEP 20의 함수들을 utils.py로 분리 → main.py에서 import
통과 조건: if __name__ == "__main__":이 왜 필요한지 설명한다
STEP 30. 가상환경 ⭐
배울 것: python -m venv venv, 활성화, pip install, pip freeze > requirements.txt, pip install -r requirements.txt
실습: 새 폴더에 venv 만들고 requests 설치 → requirements.txt 생성 → venv 지웠다가 재생성해서 복원
통과 조건: 프로젝트마다 venv를 만드는 게 습관이 된다
왜 중요: 이거 안 하면 나중에 패키지 버전 충돌로 프로젝트가 통째로 안 돌아가. 특히 9단계 LangChain에서
STEP 31. 외부 라이브러리 써보기
배울 것: requests로 API 호출
실습: 공개 API(예: https://api.github.com/users/사용자명) 호출 → JSON 응답을 dict로 받아 필요한 값만 출력
통과 조건: API 응답 dict에서 중첩된 값을 꺼낸다
왜 중요: 7단계 OpenAI API 호출의 예행연습이야
최종 관문 — 미니 프로젝트 3개

이걸 통과하면 1단계 완료. 각각 GitHub 저장소로 올려.

프로젝트 A. 가계부 CLI
요구사항: 수입/지출 입력 → CSV 저장 → 월별·카테고리별 합계 출력 → 잘못된 입력 예외 처리
쓰이는 STEP: dict, 리스트, 함수, CSV, 예외 처리
통과 조건: 프로그램을 껐다 켜도 데이터가 남아 있다
프로젝트 B. 텍스트 분석기
요구사항: 텍스트 파일 읽기 → 단어 빈도 세기(dict) → 상위 10개 출력 → 결과를 JSON으로 저장
쓰이는 STEP: 문자열, dict, 정렬, 파일, JSON, 컴프리헨션
통과 조건: 상위 N개를 인자로 바꿀 수 있게 함수화돼 있다
프로젝트 C. API 데이터 수집기
요구사항: 공개 API 호출 → 원하는 필드만 추출 → CSV 저장 → 네트워크 오류 예외 처리
쓰이는 STEP: requests, JSON, dict, CSV, 예외, 모듈 분리, venv
통과 조건: requirements.txt가 있고, 남이 clone해서 실행 가능
왜 중요: 이게 5단계 가격 예측 프로젝트의 데이터 수집 파트가 그대로 돼
1단계 졸업 체크
 100줄 정도 프로그램을 구조 잡아 작성한다
 중첩 dict에서 값을 자유롭게 꺼낸다
 Traceback을 읽고 문제 줄을 찾는다
 새 프로젝트를 venv + requirements.txt로 시작한다
 코드를 함수 단위로 쪼갠다
 GitHub에 저장소 3개가 README와 함께 있다
병행할 것 (2단계 Git)

STEP 3부터 매일 커밋해. 처음엔 git add . / git commit -m "..." / git push 세 개만 써도 돼. 브랜치·PR은 미니 프로젝트 시작할 때 배우면 충분해.

.gitignore에 반드시: venv/, __pycache__/, .env
