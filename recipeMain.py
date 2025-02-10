import streamlit as st

st.title("🍽️ 요리 레시피 추천")

# 사용자 입력 (재료 입력)
ingredients = st.text_input("사용 가능한 재료를 입력하세요 (예: 닭고기, 감자, 양파)")

# 레시피 목록 (임시 데이터)
recipes = {
    "닭고기, 감자": "닭볶음탕",
    "양파, 토마토": "토마토 스프",
    "계란, 당근": "당근 오믈렛"
}

# 버튼 클릭 시 레시피 추천
if st.button("레시피 추천받기"):
    recipe = recipes.get(ingredients, "해당 재료로 만들 수 있는 레시피가 없습니다. 😢")
    st.success(f"🥗 추천 요리: {recipe}")
