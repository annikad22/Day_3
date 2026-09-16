import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
from io import StringIO
from pypdf import PdfReader
import pypdf
import re
import os

load_dotenv()
client = OpenAI() 

st.header("Elements of a Contract")

st.header("Part 1 - Upload Contract")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        st.write(text)
    else:
        bytes_data = uploaded_file.getvalue()
        string_data = bytes_data.decode("utf-8")
        st.write(string_data)

st.divider()

st.header("Step 1: Offer and Acceptance")

# ---- Reference material ----
REFERENCE_TEXT = """
Offer and Acceptance.
A contract is formed when an offer by one party is accepted by the other party.
An enforceable offer must be distinguished from mere willingness by one person to
negotiate further details with the other party.
• For example, a used car dealer, A, offers to sell B a car. Before any agreement is
reached on brand, type, or price, B decides he does not wish to buy a car from A.
At this stage, there is no legally binding contract between A and B because there
is no definite offer for B to accept until the essential terms of the bargain have
been decided.
An offer does not need to be made to a specific person. It can be made to a class of
people, or to the whole world.
An offer is a definite promise to be bound, provided the terms of the offer are
accepted. This means that there must be acceptance of precisely what has been
offered.
• Continuing the example above, say A offers to sell B a Holden panel van for
$1000, without a roadworthy certificate. If B decides to buy the Holden panel
van, but insists on a roadworthy certificate being provided, then B is not
accepting A’s offer. Rather, B is making a counter offer. It is then up to A to
accept or reject the counter offer.
A person can withdraw the offer that has been proposed before that offer is
accepted. For withdrawal to be effective, the person who has proposed the offer
must communicate to the other party that the offer has been withdrawn.
• To continue the same example, A may say to B that he will check with his
supervisor and maybe a roadworthy certificate can be provided. If, while waiting
for a reply, B decides he no longer wants to buy the Holden panel van and tells A
of his change of mind, then there is no binding contract.
It is always advisable to have the details of such conversations in writing, so follow
up with an email or letter confirming the details of the conversation.
Acceptance of an offer occurs when the party responding to the offer (called the
offeree) agrees to the offer by way of a clear statement to indicate their acceptance
or by some conduct or act on their part. Acceptance must be unequivocal and
effectively communicated to the offeror; the law does not deem or presume a person
has accepted an offer merely because they have not expressly rejected it. However,
acceptance of an offer can also be implied by the parties’ conduct.
• If, for example, A gives B a quote to provide cleaning services and, after receiving
this quote, B tells A to do the work, this constitutes acceptance of the offer and is
a binding contract such that B is bound to pay A the quoted amount.
"""

SYSTEM_PROMPT = f"""You are a legal explainer assistant. You must ONLY use the reference text provided below to answer questions.
Do not use any outside knowledge, assumptions, or general legal information beyond what is explicitly stated in this text.
If the answer cannot be found in the reference text, respond exactly with: "This information is not available in the provided reference material."

REFERENCE TEXT:
{REFERENCE_TEXT}
"""

if st.button("Explain Offer and Acceptance"):
    with st.spinner("Generating explanation..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": "Explain what 'Offer' and 'Acceptance' mean in contract law, in exactly two lines."}
            ],
            max_tokens=100,
            temperature=0,
        )
        st.write(response.choices[0].message.content)


st.header("Step 2: Does the Contract Show a Valid Offer and Acceptance?")

if uploaded_file is not None and text.strip():
    if st.button("Analyze for Offer and Acceptance"):
        with st.spinner("Analyzing..."):
            analysis_prompt = f"""Based ONLY on the reference text provided in your instructions, analyze the following contract/scenario text.

Determine:
1. Whether a clear, definite offer was made (Yes/No)
2. Whether that offer was accepted (Yes/No)
3. A brief explanation (2-3 lines) referencing the relevant rule from the reference text

TEXT TO ANALYZE:
{text}

Respond in this exact format:
Offer Made: [Yes/No]
Accepted: [Yes/No]
Explanation: [your explanation]
"""
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": analysis_prompt}
                ],
                max_tokens=200,
                temperature=0,
            )
            st.write(response.choices[0].message.content)
else:
    st.info("Upload a contract or scenario above to run this analysis.")
    

offer_made = st.radio(
    "Did Sarah make a clear, definite offer?",
    ["Yes", "No"],
    index=None,
)


if offer_made is None:
    st.info("Answer the question above to continue.")

elif offer_made == "Yes":
    st.success("✅ Step 1 passed: a clear, definite offer was made. Proceed to Step 2 (Offer Communicated).")

elif offer_made == "No":
    st.error(
        "❌ No contract can be formed: without a clear, definite offer, there is nothing "
        "capable of being accepted. (This may instead be a mere invitation to treat.)"
    )






if "Bubble1" not in st.session_state:
    st.session_state.bubble1 = False

if "Bubble2" not in st.session_state:
    st.session_state.bubble2 = False

if "Bubble3" not in st.session_state:
    st.session_state.bubble3 = False

if st.session_state.bubble1 is False and st.session_state.bubble2 is False and st.session_state.bubble3 is False:
    st.write("All bubbles are False")

if st.session_state.bubble1 is False and st.session_state.bubble2 is False and st.session_state.bubble3 is False:
    st.write("Only bubble 3 is True")

if st.session_state.bubble1 is False:
    st.write("Bubble1 is False")
    if st.session_state.bubble2 is False:
        st.write("And bubble2 is False")
    else:
        st.write("Bubble 3 is True")

def ask_ai_yes_no(question):
    response = client.responses.create(
        model="gpt-4o",
        instructions="Answer strictly with a single word: Yes or No. No punctuation, no explanation.",
        input=question,
        max_output_tokens=16,
        temperature=0,
    )
    return response.output_text.strip()

user_input = st.text_area(label="question")

answer = ask_ai_yes_no(user_input)
st.write(answer)
