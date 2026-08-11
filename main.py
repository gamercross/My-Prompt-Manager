# ============================================
# 🧠 My Prompt Manager
# Python Prompt Management Console Program
# ============================================


# --------------------------------------------
# 1. 기본 설정
# --------------------------------------------

CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]


# --------------------------------------------
# 2. 기본 프롬프트 데이터
# --------------------------------------------

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": (
            "당신은 전문 블로그 작가입니다. "
            "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. "
            "서론, 본론, 결론 구조를 사용하고 제목 3개를 제안해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "AI 광고 이미지 생성",
        "content": (
            "제품의 특징을 분석하여 광고에 사용할 수 있는 "
            "고품질 이미지 생성 프롬프트를 작성해주세요. "
            "조명, 구도, 분위기, 색감, 카메라 연출을 포함해주세요."
        ),
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": (
            "당신은 10년 이상의 경력을 가진 IT 컨설턴트입니다. "
            "사용자의 기술적 문제를 분석하고 이해하기 쉬운 방식으로 "
            "해결 방법과 실행 단계를 제시해주세요."
        ),
        "category": "페르소나",
        "favorite": True
    }
]


# --------------------------------------------
# 3. 메뉴 출력
# --------------------------------------------

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


# --------------------------------------------
# 4. 프롬프트 추가
# --------------------------------------------

def add_prompt():
    print()
    print("=== ➕ 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("❌ 제목은 비워둘 수 없습니다.")

    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("❌ 내용은 비워둘 수 없습니다.")

    print()
    print("카테고리 선택")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit():
            category_number = int(choice)

            if 1 <= category_number <= len(CATEGORIES):
                category = CATEGORIES[category_number - 1]
                break

        print("❌ 올바른 카테고리 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print()
    print("✅ 프롬프트가 추가되었습니다!")


# --------------------------------------------
# 5. 프롬프트 목록
# --------------------------------------------

def show_list():
    print()
    print("=== 📋 프롬프트 목록 ===")

    if not prompts:
        print("❌ 등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. "
            f"[{prompt['category']}] "
            f"{prompt['title']}"
            f"{favorite_mark}"
        )

    print()
    print(f"총 {len(prompts)}개의 프롬프트")


# --------------------------------------------
# 6. 카테고리별 조회
# --------------------------------------------

def show_category():
    print()
    print("=== 🗂️ 카테고리별 조회 ===")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit():
            category_number = int(choice)

            if 1 <= category_number <= len(CATEGORIES):
                selected_category = CATEGORIES[category_number - 1]
                break

        print("❌ 올바른 카테고리 번호를 입력해주세요.")

    print()
    print(f"[{selected_category}] 카테고리 프롬프트")

    found = False
    count = 0

    for index, prompt in enumerate(prompts, start=1):
        if prompt["category"] == selected_category:
            favorite_mark = " ⭐" if prompt["favorite"] else ""

            print(
                f"{index}. "
                f"{prompt['title']}"
                f"{favorite_mark}"
            )

            found = True
            count += 1

    if not found:
        print("❌ 해당 카테고리에 등록된 프롬프트가 없습니다.")
    else:
        print()
        print(f"총 {count}개의 프롬프트")


# --------------------------------------------
# 7. 프롬프트 검색
# --------------------------------------------

def search_prompt():
    print()
    print("=== 🔍 프롬프트 검색 ===")

    while True:
        keyword = input("검색어: ").strip()

        if keyword:
            break

        print("❌ 검색어를 입력해주세요.")

    print()
    print("검색 결과:")

    found = False
    count = 0

    for index, prompt in enumerate(prompts, start=1):
        title = prompt["title"]
        content = prompt["content"]

        if keyword.lower() in title.lower() or keyword.lower() in content.lower():
            favorite_mark = " ⭐" if prompt["favorite"] else ""

            print(
                f"{index}. "
                f"[{prompt['category']}] "
                f"{prompt['title']}"
                f"{favorite_mark}"
            )

            found = True
            count += 1

    if not found:
        print("❌ 검색 결과가 없습니다.")
    else:
        print()
        print(f"총 {count}개의 프롬프트를 찾았습니다.")


# --------------------------------------------
# 8. 프롬프트 상세 보기
# --------------------------------------------

def show_detail():
    print()
    print("=== 📖 프롬프트 상세 보기 ===")

    if not prompts:
        print("❌ 등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("번호 입력: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("❌ 올바른 프롬프트 번호를 입력해주세요.")

    favorite_mark = "⭐" if prompt["favorite"] else "☆"

    print()
    print("─" * 40)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_mark}")
    print("─" * 40)
    print("내용:")
    print(prompt["content"])
    print("─" * 40)


# --------------------------------------------
# 9. 즐겨찾기 추가 / 해제
# --------------------------------------------

def toggle_favorite():
    print()
    print("=== ⭐ 즐겨찾기 관리 ===")

    if not prompts:
        print("❌ 등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("프롬프트 번호 입력: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("❌ 올바른 프롬프트 번호를 입력해주세요.")

    if prompt["favorite"]:
        prompt["favorite"] = False

        print(
            f"☆ '{prompt['title']}' "
            "프롬프트의 즐겨찾기를 해제했습니다."
        )
    else:
        prompt["favorite"] = True

        print(
            f"⭐ '{prompt['title']}' "
            "프롬프트를 즐겨찾기에 추가했습니다!"
        )


# --------------------------------------------
# 10. 즐겨찾기 목록
# --------------------------------------------

def show_favorites():
    print()
    print("=== ⭐ 즐겨찾기 목록 ===")

    favorite_count = 0

    for index, prompt in enumerate(prompts, start=1):
        if prompt["favorite"]:
            print(
                f"{index}. "
                f"[{prompt['category']}] "
                f"{prompt['title']} ⭐"
            )

            favorite_count += 1

    if favorite_count == 0:
        print("❌ 즐겨찾기된 프롬프트가 없습니다.")
    else:
        print()
        print(f"총 {favorite_count}개의 즐겨찾기")


# --------------------------------------------
# 11. 메인 프로그램
# --------------------------------------------

def main():

    print()
    print("🧠 My Prompt Manager를 시작합니다!")

    while True:

        show_menu()

        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()

        elif choice == "2":
            show_list()

        elif choice == "3":
            show_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_detail()

        elif choice == "6":
            toggle_favorite()

        elif choice == "7":
            show_favorites()

        elif choice == "0":
            print()
            print("👋 프로그램을 종료합니다.")
            break

        else:
            print()
            print("❌ 잘못된 번호입니다.")
            print("0~7 사이의 번호를 입력해주세요.")


# --------------------------------------------
# 프로그램 실행
# --------------------------------------------

if __name__ == "__main__":
    main()