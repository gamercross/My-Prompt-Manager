# 🧠 My Prompt Manager

> **나만의 프롬프트를 저장하고, 검색하고, 관리하는 Python 콘솔 프로그램**

프롬프트를 작성하다 보면 좋은 프롬프트가 점점 쌓이지만,
정작 필요할 때 원하는 프롬프트를 찾기 어려운 문제가 발생합니다.

**My Prompt Manager**는 이러한 문제를 해결하기 위해 제작한
Python 기반의 프롬프트 관리 콘솔 프로그램입니다.

프롬프트를 카테고리별로 관리하고,
키워드로 검색하며,
자주 사용하는 프롬프트는 ⭐ 즐겨찾기로 관리할 수 있도록 구현했습니다.

---

# 📚 Chapter 1. 프로젝트 소개

## 1-1. 미션 배경

GenAI를 활용하면서 다양한 프롬프트를 작성하게 되었습니다.

텍스트 생성용 프롬프트부터 이미지 생성, 영상 생성,
페르소나 설정, 업무 자동화용 프롬프트까지 사용 목적도 다양해졌습니다.

하지만 프롬프트가 많아질수록 다음과 같은 문제가 발생했습니다.

- 📋 필요한 프롬프트를 찾기 어렵다.
- 🔎 어떤 프롬프트가 어떤 용도였는지 기억하기 어렵다.
- 📂 프롬프트가 메모장, 문서, 메신저 등에 흩어진다.
- ⭐ 자주 사용하는 프롬프트를 따로 관리하기 어렵다.
- ♻️ 이전에 만들었던 프롬프트를 다시 활용하기 번거롭다.

따라서 단순히 프롬프트를 작성하는 것에서 끝나는 것이 아니라,
**프롬프트를 체계적으로 저장하고 관리할 수 있는 프로그램**을 직접 제작하기로 했습니다.

---

## 1-2. 프로젝트 목표

이번 프로젝트의 핵심 목표는
**Python 기초 문법과 Git/GitHub를 실제 프로젝트에 적용하는 것**입니다.

단순히 Python 문법을 공부하는 것이 아니라,
각 문법이 실제 프로그램의 기능으로 어떻게 연결되는지를 이해하는 것을 목표로 합니다.

### 🐍 Python

Python을 이용하여 다음 기능을 직접 구현.

- ➕ 프롬프트 추가
- 📋 프롬프트 목록 확인
- 🗂️ 카테고리별 조회
- 🔍 키워드 검색
- 📖 프롬프트 상세 보기
- ⭐ 즐겨찾기 추가/해제
- ⭐ 즐겨찾기 목록 확인

이를 통해 다음 Python 개념을 실제 코드 적용.

| Python 개념 | 프로젝트 적용 |
|---|---|
| 변수 | 프롬프트 데이터 저장 |
| 리스트 | 여러 프롬프트 관리 |
| 딕셔너리 | 프롬프트의 제목/내용/카테고리 저장 |
| 조건문 | 메뉴 선택 및 입력 검증 |
| 반복문 | 메뉴 반복 실행 및 데이터 검색 |
| 함수 | 기능별 코드 분리 |
| `input()` | 사용자 입력 |
| `print()` | 프로그램 결과 출력 |

---

## 1-3. Git / GitHub 활용 목표

이번 프로젝트에서는 프로그램을 만드는 것이 아닌
**Git을 이용하여 개발 과정을 기록하고 GitHub에서 프로젝트를 관리하는 것**

Git을 사용하여 기능을 하나씩 개발하고
변경 사항을 의미 있는 단위로 커밋함.

또한 별도의 브랜치에서 기능을 개발한 뒤
`main` 브랜치에 병합까지 해야하는 미션

### 🌿 Git 작업 흐름

```text
기능 계획
   ↓
코드 작성
   ↓
기능 테스트
   ↓
git add
   ↓
git commit
   ↓
필요한 경우 branch 생성
   ↓
기능 개발
   ↓
checkout
   ↓
merge
   ↓
main
   ↓
git push
   ↓
GitHub
```

---

## 1-4. 프로젝트에서 해결하려는 문제

### ❌ 기존 방식
```
메모장
   ├── 이미지 프롬프트
   ├── 광고 프롬프트
   └── 페르소나 프롬프트

Notion
   ├── 업무용 프롬프트
   └── 개인용 프롬프트

메신저
   └── 예전에 사용했던 프롬프트
```
QA: 프롬포트가 여러 장소에 분산되면 필요한 프롬포트를 다시 찾는 데 시간이 소요됨

### ✅ My Prompt Manager
```
             🧠 My Prompt Manager
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    📂 분류        🔍 검색        ⭐ 즐겨찾기
       │             │             │
       └─────────────┼─────────────┘
                     ↓
              원하는 프롬프트
```

---

## 1-5. 프로그램의 핵심 데이터 구조
```
{
    "title": "블로그 글 작성 도우미",
    "content": "당신은 전문 블로그 작가입니다...",
    "category": "텍스트 생성",
    "favorite": False
}
```

```
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 전문 블로그 작가입니다...",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "AI 광고 이미지 생성",
        "content": "제품의 특징을 분석하여...",
        "category": "이미지 생성",
        "favorite": False
    }
]
```

---

## 1-6. 기본 프롬프트 카테고리
| 카테고리      | 설명                     |
| --------- | ---------------------- |
| ✍️ 텍스트 생성 | 글쓰기, 요약, 보고서 등의 프롬프트   |
| 🎨 이미지 생성 | 이미지 제작을 위한 프롬프트        |
| 🎬 영상 생성  | 영상 제작 및 영상 프롬프트        |
| 👤 페르소나   | 특정 역할이나 전문가를 설정하는 프롬프트 |
| ⚙️ 자동화    | 반복 업무 및 업무 자동화용 프롬프트   |
| 📦 기타     | 위 카테고리에 포함되지 않는 프롬프트   |

---

## 1-7. 프로그램 메뉴 구성
```
========================================
       🧠 My Prompt Manager
========================================
1. ➕ 프롬프트 추가
2. 📋 프롬프트 목록
3. 🗂️ 카테고리별 조회
4. 🔍 프롬프트 검색
5. 📖 프롬프트 상세 보기
6. ⭐ 즐겨찾기 관리
7. ⭐ 즐겨찾기 목록
0. 🚪 종료
========================================
선택:
```

---
## 1-8. 현재 개발 환경
| 항목                 | 환경                 |
| ------------------ | ------------------ |
| 💻 OS              | macOS              |
| 🛠️ IDE            | Visual Studio Code |
| 🐍 Language        | Python 3.10 이상     |
| 🌿 Version Control | Git                |
| ☁️ Repository      | GitHub             |
| 📦 외부 라이브러리        | 사용하지 않음            |

---

## 1-9. 프로젝트 개발 방향
```
🐍 Python 환경 설정
        ↓
📌 기본 데이터 생성
        ↓
🧭 메인 메뉴 구현
        ↓
➕ 프롬프트 추가
        ↓
📋 프롬프트 목록
        ↓
🗂️ 카테고리별 조회
        ↓
🔍 검색
        ↓
📖 상세 보기
        ↓
⭐ 즐겨찾기
        ↓
🌿 Branch 활용
        ↓
🔀 Merge
        ↓
☁️ GitHub Push
```

---

## 1-10. 프로젝트 기대 결과

| "아이디어를 코드로 구현하고,
| Git으로 변경 이력을 관리하며,
| GitHub에서 프로젝트를 관리할 수 있는 개발 경험"

---

### 🚀 다음 Chapter
```
Chapter 1
📚 프로젝트 소개
        ↓
Chapter 2
🛠️ 개발 환경 설정
        ↓
Chapter 3
🐍 Python 프로그램 구현
        ↓
Chapter 4
🌿 Git / GitHub 관리
        ↓
Chapter 5
🧪 테스트 및 실행 결과
        ↓
Chapter 6
📸 제출 증빙
```

---

# 🛠️ Chapter 2. 개발 환경 설정

Chapter 1에서 프로젝트의 목적과 프로그램의 전체적인 방향을 정의,
Chapter 2에서는 실제 프로그램을 개발하기 위한 환경을 구성함.

**VSCode + Python + Git + GitHub**를 기본 개발 환경으로 사용함.
-> Python으로 프로그램을 작성하고 실행하며, Git으로 코드의 변경 이력을 관리하고, GitHub를 통해 프로젝트를 저장하고 관리하는 것을 목표로 함.

---

## 2-1. 개발 환경 구성

### 💻 사용 환경

| 항목        | 설정                 |
| --------- | ------------------ |
| 운영체제      | macOS              |
| 개발 도구     | VSCODE |
| 프로그래밍 언어  | Python             |
| Python 버전 | Python 3.10 이상     |
| 버전 관리     | Git                |
| 원격 저장소    | GitHub             |

---

## 2-2. VSCode 설정

### 🔧 설치 및 설정

* Visual Studio Code 설치
* Python Extension 설치
* GitHub 계정 연결

---

## 2-3. Python 설치 확인

macOS에서는 다음 명령어를 사용.

```bash
python3 --version
```

정상적으로 설치되었다면 다음과 같이 Python 버전이 표시됨.

```text
Python 3.x.x
```

이번 프로젝트의 요구사항은 **Python 3.10 이상**이므로 3.10 이상의 버전을 사용해야함.

### 🧪 Python 실행 테스트

Python 환경이 정상적으로 동작하는지 확인하기 위해 간단한 코드를 실행.

```python
print("Hello")
```

실행 결과:

```text
Hello
```

이 테스트를 통해 Python 파일 작성과 실행 환경이 정상적으로 구성되었는지 확인.

---

## 2-4. Python 실행 명령어

현재 프로젝트에서는 macOS 환경을 사용하기 때문에 Python 실행 시 `python3` 명령어 사용.

```bash
python3 main.py
```

처음 실행하면 프로그램의 메인 메뉴 출력.

```text
🧠 My Prompt Manager를 시작합니다!

========================================
       🧠 My Prompt Manager
========================================
1. ➕ 프롬프트 추가
2. 📋 프롬프트 목록
3. 🗂️ 카테고리별 조회
4. 🔍 프롬프트 검색
5. 📖 프롬프트 상세 보기
6. ⭐ 즐겨찾기 관리
7. ⭐ 즐겨찾기 목록
0. 🚪 종료
========================================
선택:
```

이를 통해 Python 프로그램이 실제 터미널에서 정상적으로 실행 확인.

---

## 2-5. Git 설치 확인

Git은 프로그램의 변경 이력을 관리하기 위해 사용

터미널에서 다음 명령어를 실행

```bash
git --version
```

정상적으로 설치되어 있다면 다음과 같이 버전이 출력

```text
git version 2.x.x
```

Git을 이용하면 프로그램을 개발하면서 발생한 변경 사항을 커밋으로 기록 가능

---

## 2-6. Git 사용자 정보 설정

Git 커밋을 생성하기 위해서는 사용자 이름과 이메일을 설정

### 👤 사용자 이름

```bash
git config --global user.name "사용자 이름"
```

### 📧 사용자 이메일

```bash
git config --global user.email "사용자 이메일"
```

설정한 정보는 다음 명령어로 확인 가능

```bash
git config --global user.name
```

```bash
git config --global user.email
```

또는 전체 Git 설정을 확인

```bash
git config --global --list
```

설정이 정상적으로 완료되면 다음과 같이 확인

```text
user.name=사용자 이름
user.email=사용자 이메일
```

이 설정은 이후 Git 커밋을 생성할 때 작성자 정보로 사용

---

## 2-7. 기본 브랜치 설정

이번 프로젝트에서는 기본 브랜치 이름을 `main`으로 사용한

Git의 기본 브랜치 이름을 `main`으로 설정

```bash
git config --global init.defaultBranch main
```

설정 확인:

```bash
git config --global init.defaultBranch
```

정상적인 결과:

```text
main
```

이후 새로운 Git 저장소를 생성하면 기본 브랜치가 `main`으로 생성되도록 설정

---

## 2-8. GitHub 연결

GitHub는 프로젝트의 원격 저장소로 사용함

프로젝트의 로컬 폴더에서 작성한 코드를 Git으로 관리하고, 이후 GitHub에 Push하여 원격 저장소에 업로드

전체적인 연결 구조

```text
💻 로컬 컴퓨터
      │
      │ Git
      ↓
📁 Local Repository
      │
      │ git push
      ↓
☁️ GitHub Repository
```

VSCode에서는 GitHub 계정으로 로그인하여 GitHub 저장소와 연결

정상적으로 연결되면 VSCode의 Source Control 기능을 이용하여 Git 변경 사항을 확인 가능

---

## 2-9. 프로젝트 폴더 구성

현재 프로젝트의 기본 폴더 구조는 다음과 같이 구성함.

```text
My-Prompt-Manager/
│
├── main.py
├── README.md
└── .gitignore
```

각 파일의 역할

| 파일           | 역할                   |
| ------------ | -------------------- |
| `main.py`    | 프롬프트 관리 프로그램의 메인 코드  |
| `README.md`  | 프로젝트 설명 및 개발 과정 기록   |
| `.gitignore` | Git에서 제외할 파일 및 폴더 설정 |

---

## 2-10. `.gitignore` 설정

GitHub에 업로드할 필요가 없는 파일을 제외하기 위해 `.gitignore`를 사용한다.

Python 프로젝트에서 생성될 수 있는 불필요한 캐시 파일 등을 제외한다.

```gitignore
__pycache__/
*.pyc
.DS_Store
.vscode/
```

이를 통해 프로젝트에 필요한 코드와 문서 중심으로 Git 저장소를 관리

---

## 2-11. 개발 환경 확인 체크리스트

체크리스트 확인

* [x] 💻 VSCode 설치
* [x] 🐍 Python Extension 설치
* [x] 🐍 Python 3.10 이상 확인
* [x] ▶️ `print("Hello")` 실행
* [x] 🐙 Git 설치 확인
* [x] 👤 Git `user.name` 설정
* [x] 📧 Git `user.email` 설정
* [x] 🌿 기본 브랜치 `main` 설정
* [x] ☁️ GitHub 계정 연결
* [x] 📁 프로젝트 폴더 생성
* [x] 📄 `main.py` 생성
* [x] 📄 `README.md` 생성
* [x] 🚫 `.gitignore` 생성

> 📌 위 체크리스트는 실제 개발 환경을 설정한 뒤 최종 제출 전에 다시 확인할 것.

---

## 2-12. 개발 환경 설정 결과

개발환경

```text
┌─────────────────────────────────────┐
│       🧠 My Prompt Manager          │
├─────────────────────────────────────┤
│ 💻 macOS                            │
│ 🛠️ VSCode                           │
│ 🐍 Python 3.10+                     │
│ 🐙 Git                              │
│ ☁️ GitHub                           │
└─────────────────────────────────────┘
```

---

## 🔗 Chapter 2 → Chapter 3

```text
Chapter 1
📚 프로젝트 소개
       ↓
Chapter 2
🛠️ 개발 환경 설정
       ↓
Chapter 3
🐍 Python 프로그램 구현
       ↓
📌 기본 데이터
       ↓
🧭 메뉴 시스템
       ↓
➕ 프롬프트 추가
       ↓
📋 목록 / 🔍 검색 / 🗂️ 카테고리
       ↓
📖 상세 보기
       ↓
⭐ 즐겨찾기
```

**Chapter 3에서는 `main.py`의 코드를 기능별로 나누어 설명하고, 실제 실행 결과와 함께 프로그램 구현 과정을 기록한다.**


# 🐍 Chapter 3. Python 프로그램 구현

> **데이터 구조 → 메뉴 → 기능별 함수 → 사용자 입력 → 기능 테스트**

---

## 3-1. 프로그램 구현 목표

### 🎯 구현할 기능

| 번호 | 기능 | 설명 |
|---:|---|---|
| 1 | ➕ 프롬프트 추가 | 새로운 프롬프트 등록 |
| 2 | 📋 프롬프트 목록 | 전체 프롬프트 확인 |
| 3 | 🗂️ 카테고리별 조회 | 특정 카테고리만 확인 |
| 4 | 🔍 프롬프트 검색 | 제목 또는 내용 검색 |
| 5 | 📖 상세 보기 | 선택한 프롬프트의 전체 내용 확인 |
| 6 | ⭐ 즐겨찾기 관리 | 즐겨찾기 추가/해제 |
| 7 | ⭐ 즐겨찾기 목록 | 즐겨찾기만 모아서 확인 |
| 0 | 🚪 종료 | 프로그램 종료 |

---

## 3-2. 기본 데이터 설계

## 데이터를 저장할 구조

각 프롬프트는 다음 네 가지 정보를 가짐

- 📝 제목
- 📄 내용
- 🗂️ 카테고리
- ⭐ 즐겨찾기 여부

Python에서는 하나의 프롬프트를 **딕셔너리(Dictionary)**로 표현하고,
여러 개의 프롬프트는 **리스트(List)**에 저장함.

### 📦 데이터 구조

```python
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "AI 광고 이미지 생성",
        "content": "제품의 특징을 분석하여 광고 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "전문가 페르소나 설정",
        "content": "당신은 해당 분야의 전문 컨설턴트입니다.",
        "category": "페르소나",
        "favorite": True
    }
]

```

## 3-3. 기본 카테고리 정의

```python
categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]
```
*** 🗂️ 카테고리 ***
| 카테고리      | 사용 목적        |
| --------- | ------------ |
| ✍️ 텍스트 생성 | 글쓰기, 요약, 보고서 |
| 🎨 이미지 생성 | 이미지 제작       |
| 🎬 영상 생성  | 영상 및 광고 제작   |
| 👤 페르소나   | 역할 및 전문가 설정  |
| ⚙️ 자동화    | 반복 업무 자동화    |
| 📦 기타     | 기타 프롬프트      |

## 3-4. 메인 메뉴 구현

```
def show_menu():
    print()
    print("=" * 40)
    print("       🧠 My Prompt Manager")
    print("=" * 40)
    print("1. ➕ 프롬프트 추가")
    print("2. 📋 프롬프트 목록")
    print("3. 🗂️ 카테고리별 조회")
    print("4. 🔍 프롬프트 검색")
    print("5. 📖 프롬프트 상세 보기")
    print("6. ⭐ 즐겨찾기 관리")
    print("7. ⭐ 즐겨찾기 목록")
    print("0. 🚪 종료")
    print("=" * 40)
```

*** 💡 함수로 분리한 이유 ***
메뉴 출력 코드를 show_menu() 함수로 분리하면
메인 프로그램에서 필요할 때마다 함수를 호출할 수 있다.
```
show_menu()
```

## 3-5. 프롬프트 추가 기능

### 입력받는 정보

```
제목
내용
카테고리
```

사용자가 빈 값을 입력하면 다시 입력하도록 처리한다.

### ➕ 입력 과정

```
=== 프롬프트 추가 ===

제목: 회의록 요약 도우미
내용: 회의 내용을 결정사항과 Action Items 중심으로 정리해주세요.

카테고리 선택:
1) 텍스트 생성
2) 이미지 생성
3) 영상 생성
4) 페르소나
5) 자동화
6) 기타

선택: 1

✅ 프롬프트가 추가되었습니다!
```

### 💻 함수 구조
```
def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ").strip()

    while not title:
        print("⚠️ 제목은 비워둘 수 없습니다.")
        title = input("제목: ").strip()

    content = input("내용: ").strip()

    while not content:
        print("⚠️ 내용은 비워둘 수 없습니다.")
        content = input("내용: ").strip()

    print("\n카테고리 선택:")

    for i, category in enumerate(categories, 1):
        print(f"{i}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            break

        print("⚠️ 올바른 카테고리 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("\n✅ 프롬프트가 추가되었습니다!")
```

## 3-6. 프롬프트 목록 기능

목록에서는 다음 정보를 표시한다.

```
번호
카테고리
제목
즐겨찾기 여부
```

### 📋 실행 예시
```
=== 프롬프트 목록 ===

1. [텍스트 생성] 블로그 글 작성 도우미
2. [이미지 생성] AI 광고 이미지 생성
3. [페르소나] 전문가 페르소나 설정 ⭐
4. [자동화] 회의록 정리 도우미

총 4개의 프롬프트
```

### 💻 함수
```
def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("📭 등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        favorite = " ⭐" if prompt["favorite"] else ""

        print(
            f"{i}. "
            f"[{prompt['category']}] "
            f"{prompt['title']}"
            f"{favorite}"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")
```

## 3-7. 카테고리별 조회

### 🗂️ 실행 예시
```
=== 카테고리별 조회 ===

1) 텍스트 생성
2) 이미지 생성
3) 영상 생성
4) 페르소나
5) 자동화
6) 기타

선택: 1

[텍스트 생성]

1. 블로그 글 작성 도우미
2. 회의록 요약 도우미

총 2개의 프롬프트
```

### 💻 함수
```
def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    for i, category in enumerate(categories, 1):
        print(f"{i}) {category}")

    choice = input("선택: ").strip()

    if not choice.isdigit():
        print("⚠️ 올바른 번호를 입력해주세요.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(categories):
        print("⚠️ 존재하지 않는 카테고리입니다.")
        return

    selected_category = categories[index]

    print(f"\n[{selected_category}]")

    count = 0

    for i, prompt in enumerate(prompts, 1):
        if prompt["category"] == selected_category:
            favorite = " ⭐" if prompt["favorite"] else ""
            print(f"{i}. {prompt['title']}{favorite}")
            count += 1

    if count == 0:
        print("📭 해당 카테고리에 등록된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 프롬프트")
```

## 3-8. 프롬프트 검색

색 기능에서는 사용자가 입력한 키워드가

* 제목
* 내용

중 하나에 포함되어 있는지 확인한다.

### 🔍 실행 예시
```
=== 프롬프트 검색 ===

검색어: 광고

검색 결과:

1. [이미지 생성] AI 광고 이미지 생성

총 1개의 프롬프트를 찾았습니다.
```
### 💻 함수
```
def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip().lower()

    if not keyword:
        print("⚠️ 검색어를 입력해주세요.")
        return

    results = []

    for i, prompt in enumerate(prompts, 1):
        title = prompt["title"].lower()
        content = prompt["content"].lower()

        if keyword in title or keyword in content:
            results.append((i, prompt))

    if not results:
        print("🔎 검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for i, prompt in results:
        favorite = " ⭐" if prompt["favorite"] else ""

        print(
            f"{i}. "
            f"[{prompt['category']}] "
            f"{prompt['title']}"
            f"{favorite}"
        )

    print(f"\n총 {len(results)}개의 프롬프트를 찾았습니다.")
```

## 3-9. 프롬프트 상세 보기

### 📖 실행 예시
```
=== 프롬프트 상세 보기 ===

번호 입력: 1

────────────────────────────
제목: 블로그 글 작성 도우미
카테고리: 텍스트 생성
즐겨찾기: -
────────────────────────────

내용:

주어진 주제에 대해 SEO에 최적화된
블로그 글을 작성해주세요.

────────────────────────────
```
### 💻 함수
```
def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("📭 등록된 프롬프트가 없습니다.")
        return

    choice = input("번호 입력: ").strip()

    if not choice.isdigit():
        print("⚠️ 올바른 번호를 입력해주세요.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("⚠️ 존재하지 않는 번호입니다.")
        return

    prompt = prompts[index]

    favorite = "⭐" if prompt["favorite"] else "-"

    print("\n" + "─" * 30)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite}")
    print("─" * 30)
    print("내용:")
    print(prompt["content"])
    print("─" * 30)
```

### 3-10. 즐겨찾기 관리
사용자가 프롬프트 번호를 입력하면
```
False → True
True → False
```
형태로 상태를 변경한다.

### ⭐ 실행 예시
```
=== 즐겨찾기 관리 ===

프롬프트 번호 입력: 2

⭐ 'AI 광고 이미지 생성'
프롬프트를 즐겨찾기에 추가했습니다!
```
다시 선택하면:
```
☆ 'AI 광고 이미지 생성'
프롬프트의 즐겨찾기를 해제했습니다!
```

###
```
def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("📭 등록된 프롬프트가 없습니다.")
        return

    choice = input("프롬프트 번호 입력: ").strip()

    if not choice.isdigit():
        print("⚠️ 올바른 번호를 입력해주세요.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("⚠️ 존재하지 않는 번호입니다.")
        return

    prompt = prompts[index]

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(
            f"⭐ '{prompt['title']}' "
            "프롬프트를 즐겨찾기에 추가했습니다!"
        )
    else:
        print(
            f"☆ '{prompt['title']}' "
            "프롬프트의 즐겨찾기를 해제했습니다!"
        )
```

## 3-11. 즐겨찾기 목록

### 💻 함수
```
def show_favorites():
    print("\n=== ⭐ 즐겨찾기 목록 ===")

    favorite_count = 0

    for i, prompt in enumerate(prompts, 1):
        if prompt["favorite"]:
            print(
                f"{i}. "
                f"[{prompt['category']}] "
                f"{prompt['title']} ⭐"
            )

            favorite_count += 1

    if favorite_count == 0:
        print("⭐ 등록된 즐겨찾기가 없습니다.")
    else:
        print(f"\n총 {favorite_count}개의 즐겨찾기")
```

## 3-12. 메인 프로그램 연결
```
def main():
    while True:
        show_menu()

        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()

        elif choice == "2":
            show_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_detail()

        elif choice == "6":
            toggle_favorite()

        elif choice == "7":
            show_favorites()

        elif choice == "0":
            print("\n👋 프로그램을 종료합니다.")
            break

        else:
            print("\n⚠️ 올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    main()
```

## 3-13.전체 프로그램 구조
```
main.py
│
├── prompts
│   └── 기본 프롬프트 데이터
│
├── categories
│   └── 카테고리 목록
│
├── show_menu()
│   └── 메인 메뉴 출력
│
├── add_prompt()
│   └── 프롬프트 추가
│
├── show_list()
│   └── 전체 목록
│
├── show_by_category()
│   └── 카테고리별 조회
│
├── search_prompt()
│   └── 키워드 검색
│
├── show_detail()
│   └── 상세 보기
│
├── toggle_favorite()
│   └── 즐겨찾기 추가/해제
│
├── show_favorites()
│   └── 즐겨찾기 목록
│
└── main()
    └── 전체 프로그램 실행
```

## 3-14. 입력 오류 처리

| 상황              | 처리              |
| --------------- | --------------- |
| 존재하지 않는 메뉴 번호   | ⚠️ 안내 후 메뉴로 돌아감 |
| 빈 제목            | ⚠️ 다시 입력        |
| 빈 내용            | ⚠️ 다시 입력        |
| 잘못된 카테고리        | ⚠️ 다시 선택        |
| 존재하지 않는 프롬프트 번호 | ⚠️ 안내           |
| 빈 검색어           | ⚠️ 다시 입력        |
| 검색 결과 없음        | 🔎 결과 없음 안내     |

## 3-15. Python 기초 문법의 실제 적용
| 문법         | 실제 적용                           |
| ---------- | ------------------------------- |
| 변수         | `choice`, `keyword`, `category` |
| 리스트        | `prompts`, `categories`         |
| 딕셔너리       | 개별 프롬프트 데이터                     |
| `if`       | 메뉴 및 입력값 판단                     |
| `for`      | 프롬프트 목록 탐색                      |
| `while`    | 메뉴 반복 및 입력 검증                   |
| 함수         | 기능별 코드 분리                       |
| `input()`  | 사용자 입력                          |
| `print()`  | 결과 출력                           |
| `append()` | 새로운 프롬프트 추가                     |

## 3-16. Chapter 3 개발 결과
현재 구현된 기능은 다음과 같다.

 ➕ 프롬프트 추가
 📋 프롬프트 목록
 🗂️ 카테고리별 조회
 🔍 프롬프트 검색
 📖 프롬프트 상세 보기
 ⭐ 즐겨찾기 추가/해제
 ⭐ 즐겨찾기 목록
 ⚠️ 입력 오류 처리
 🧩 기능별 함수 분리

# 🌿 Chapter 4. Git / GitHub 버전 관리


 **Git과 GitHub를 이용하여 프로젝트의 변경 이력을 관리한다.**

이번 프로젝트에서는 단순히 GitHub에 최종 코드를 업로드하는 것이 아니라,

> **기능 개발 → 커밋 → 브랜치 개발 → 병합 → 원격 저장소 Push**

의 전체 과정을 직접 경험하는 것을 목표로 한다.

---

## 4-1. Git을 사용하는 이유

Git은 프로젝트의 코드 변경 이력을 기록하고 관리하기 위한 버전 관리 시스템이다.

이번 프로젝트에서는 기능을 하나씩 완성할 때마다 커밋을 생성하여
어떤 기능이 언제 추가되었는지 확인할 수 있도록 한다.

## 4-2. Git 저장소 초기화

프로젝트 폴더에서 Git 저장소를 생성한다.
```
git init
```
정상적으로 실행되면 현재 프로젝트 폴더가 Git 저장소로 초기화된다.

확인:
```
git status
```
예상 결과:
```
On branch main

No commits yet
```
이제 My-Prompt-Manager 폴더는 Git으로 관리할 수 있는 프로젝트가 되었다.

## 4-3. 기본 브랜치 확인
확인:
```
git branch
```
또는 초기 설정:
```
git config --global init.defaultBranch main
```
현재 브랜치:
```
* main
```
* 표시가 현재 작업 중인 브랜치를 의미한다.

## 4-4. 첫 번째 Git 커밋
프로젝트의 파일을 Git의 관리 대상으로 추가한다.
```
git add .
```
변경 상태 확인:
```
git status
```
이후 첫 번째 커밋을 생성한다.
```
git commit -m "chore: initialize project"
```
📌 첫 번째 커밋의 의미

이 커밋은 프로젝트의 기본 구조를 기록한다.
```
My-Prompt-Manager
├── main.py
├── README.md
└── .gitignore
```

## 4-5. 기능별 커밋
기능을 완성할 때마다 변경 사항을 확인한다.
```
git status
```
변경된 파일을 추가한다.
```
git add main.py
```
커밋한다.
```
git commit -m "feat: add prompt list"
```
커밋 기록 확인:
```
git log --oneline
```

## 4-6. 기능별 커밋
이번 프로젝트에서는 main 브랜치에서 바로 모든 기능을 수정하지 않고,
프롬프트 목록 기능을 별도의 브랜치에서 개발하는 과정을 수행한다.
```
main
 │
 ├── 기본 프로그램
 │
 └── prompt-list 기능
          │
          ↓
      기능 개발
          │
          ↓
        merge
          │
          ↓
        main
```
이를 통해 실제 협업 개발에서 사용되는 Branch → 개발 → Merge 과정을 경험한다.

## 4-7. 기능 브랜치 생성
현재 main 브랜치에서 새로운 브랜치를 생성한다.
```
git checkout -b feature/prompt-list
```
브랜치 확인:
```
git branch
```

## 4-8. Branch Merge
개발한 기능을 main 브랜치에 병합한다.
```
git merge feature/prompt-list
```
정상적으로 병합되면
feature 브랜치에서 개발한 기능이 main 브랜치에도 반영된다.

🔀 Merge 구조
```
main
 │
 ├── 초기 코드
 │
 └───────────────┐
                 │
feature/prompt-list
 │               │
 ├── 목록 기능   │
 │               │
 └───────────────┘
                 ↓
              merge
                 ↓
               main
```

## 4-9. GitHub에 Push
원격 저장소의 변경 사항을 로컬 저장소로 가져오기 위해 pull을 사용한다.
```
git pull origin main
```

## 4-10. Git 명령어 정리
| 명령어               | 역할                    |
| ----------------- | --------------------- |
| `git init`        | 새로운 Git 저장소 생성        |
| `git status`      | 현재 변경 상태 확인           |
| `git add`         | 변경 파일을 커밋 대상으로 추가     |
| `git commit`      | 변경 사항을 Git에 기록        |
| `git push`        | 로컬 변경 사항을 GitHub에 업로드 |
| `git pull`        | GitHub의 변경 사항을 로컬에 반영 |
| `git checkout`    | 브랜치 이동                |
| `git checkout -b` | 새로운 브랜치 생성 및 이동       |
| `git merge`       | 브랜치의 변경 사항 병합         |
| `git clone`       | 원격 Repository 복제      |
| `git log`         | 커밋 기록 확인              |
| `git branch`      | 브랜치 목록 확인             |

## 4-11. 최종 Git 작업 흐름
```
              🧠 My Prompt Manager
                       │
                       ↓
                 git init
                       │
                       ↓
                기본 프로젝트
                       │
                       ↓
                 git add .
                       │
                       ↓
              첫 번째 commit
                       │
                       ↓
             기능별 개발 / commit
                       │
                       ↓
          🌿 feature/prompt-list
                       │
                       ↓
                기능 개발
                       │
                       ↓
                   commit
                       │
                       ↓
               checkout main
                       │
                       ↓
                    merge
                       │
                       ↓
                    main
                       │
                       ↓
                  git push
                       │
                       ↓
              ☁️ GitHub Repository
```
# 🧪 Chapter 5. 기능 테스트 및 결과 검증

Chapter 1부터 Chapter 4까지의 과정을 통해
My Prompt Manager의 개발 환경을 구성하고,
Python으로 프로그램을 구현한 뒤,
Git과 GitHub를 이용하여 프로젝트의 변경 이력을 관리했다.

이제 마지막 단계로 실제 프로그램을 실행하여
각 기능이 요구사항에 맞게 정상적으로 동작하는지 확인한다.

단순히 프로그램이 실행되는 것에서 끝나는 것이 아니라,

> **입력 → 처리 → 출력 → 예외 상황 확인**

의 과정을 통해 각 기능을 직접 테스트하고 결과를 기록한다.

---

## 5-1. 테스트 목적

이번 테스트의 목적은 다음과 같음.

### 🎯 주요 검증 항목

- 프로그램이 정상적으로 실행되는가?
- 메뉴가 정상적으로 출력되는가?
- 잘못된 입력을 처리할 수 있는가?
- 프롬프트를 추가할 수 있는가?
- 등록된 프롬프트를 확인할 수 있는가?
- 카테고리별 조회가 가능한가?
- 키워드 검색이 가능한가?
- 프롬프트 상세 내용을 확인할 수 있는가?
- 즐겨찾기를 추가하거나 해제할 수 있는가?
- 프로그램 종료 시 정상적으로 종료되는가?

또한 프로그램 실행 과정에서 발생할 수 있는
예외 상황도 함께 확인해야함

---

## 5-2. 프로그램 실행

터미널에서 프로젝트 폴더로 이동한 후 프로그램을 실행한다.

```bash
python3 main.py
```

## 5-3. 전체 테스트 결과
| 번호 | 테스트 항목      |   결과   |
| -: | ----------- | :----: |
| 01 | 프로그램 실행     | ✅ PASS |
| 02 | 메뉴 출력       | ✅ PASS |
| 03 | 기본 프롬프트 데이터 | ✅ PASS |
| 04 | 프롬프트 추가     | ✅ PASS |
| 05 | 빈 입력 검증     | ✅ PASS |
| 06 | 프롬프트 목록     | ✅ PASS |
| 07 | 카테고리별 조회    | ✅ PASS |
| 08 | 키워드 검색      | ✅ PASS |
| 09 | 검색 결과 없음 처리 | ✅ PASS |
| 10 | 프롬프트 상세 보기  | ✅ PASS |
| 11 | 잘못된 번호 처리   | ✅ PASS |
| 12 | 즐겨찾기 추가     | ✅ PASS |
| 13 | 즐겨찾기 해제     | ✅ PASS |
| 14 | 즐겨찾기 목록     | ✅ PASS |
| 15 | 프로그램 종료     | ✅ PASS |

## 5-4. 최종 결과
| 요구사항          | 구현 여부 | 검증 방법     |
| ------------- | :---: | --------- |
| 메뉴 출력         |   ✅   | 프로그램 실행   |
| 번호 선택         |   ✅   | 메뉴 입력     |
| 잘못된 입력 처리     |   ✅   | 잘못된 번호 입력 |
| 프로그램 종료       |   ✅   | 0번 선택     |
| 기본 프롬프트 3개 이상 |   ✅   | 목록 확인     |
| 리스트/딕셔너리 사용   |   ✅   | 코드 확인     |
| 프롬프트 추가       |   ✅   | 추가 테스트    |
| 빈 입력 검증       |   ✅   | 빈 값 입력    |
| 카테고리별 조회      |   ✅   | 카테고리 테스트  |
| 프롬프트 검색       |   ✅   | 키워드 테스트   |
| 상세 보기         |   ✅   | 번호 입력     |
| 즐겨찾기 추가/해제    |   ✅   | 즐겨찾기 테스트  |
| 즐겨찾기 목록       |   ✅   | 목록 확인     |
| 기능별 함수 분리     |   ✅   | 코드 구조 확인  |
| README 작성     |   ✅   | GitHub 확인 |

## 5-5. Git 최종 결과 증빙

Git 관련 과제 요구사항도 최종적으로 확인한다.

🌿 Branch 확인
```
git branch
```
📊 Commit 확인
```
git log --oneline
```
🌳 Branch / Merge 구조 확인
```
git log --oneline --graph --all
```
☁️ 원격 저장소 확인
```
git remote -v
```
📤 GitHub 업로드 상태 확인
```
git status
```

최종적으로 GitHub Repository에서
소스 코드와 README가 정상적으로 업로드되어 있는지 확인한다.

# 프로젝트 전체 결과

┌──────────────────────────────────────┐
│       🥔 My Prompt Manager           │
├──────────────────────────────────────┤
│                                      │
│ 📚 Chapter 1                         │
│ 프로젝트 소개                        │
│          ↓                           │
│ 🛠️ Chapter 2                         │
│ 개발 환경 설정                       │
│          ↓                           │
│ 🐍 Chapter 3                         │
│ Python 프로그램 구현                 │
│          ↓                           │
│ 🌿 Chapter 4                         │
│ Git / GitHub 버전 관리               │
│          ↓                           │
│ 🧪 Chapter 5                         │
│ 기능 테스트 및 결과 검증             │
│          ↓                           │
│ 🏆 최종 프로젝트 완성                │
│                                      │
└──────────────────────────────────────┘