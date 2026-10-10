import streamlit as st

st.set_page_config(
    page_title="Trace AI",
    page_icon="🔎"
)

st.title("🔎 Trace AI")
st.subheader("AI Claim Analysis Assistant")

st.write(
    "Check claims carefully and organize "
    "evidence before reaching a conclusion."
)

claim = st.text_area(
    "Enter your claim here",
    placeholder="Example: All exams are cancelled today."
)

if st.button("Analyze Claim"):
    if claim.strip():
        st.subheader("Your Claim")
        st.write(claim)

        st.info(
            "Claim received successfully!"
        )

        st.warning(
            "This prototype does not yet verify "
            "whether the claim is true or false."
        )
    else:
        st.error("Please enter a claim first.")
