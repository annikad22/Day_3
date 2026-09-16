
if "senario" not in st.session_state:
    st.session_state.senario = None

if "offer" not in st.session_state:
    st.session_state.offer = False 

st.subheader("Scenario")
st.session_state.scenario = st.text_area(label="scenario, label_visibility = "hidden")

if st.session_state.scanario is not None and st.session_state.scenario != "":
    st.session("I have a scenario") #testing 

st.session_state.offer = ask_ai_yes_no(f"For Scenario: {st.session_state.scanario}, has there been an offer")
st.subheader("Offer?")
st.write(st.session_state.offer)
    #test line by line 
    #pull previous ask ai yes or no function from above. 
    #if answering yes to everything - then problem with logic for prompt 

    add in 'has there been a contractual offer? So you know, a contractual offer is something that is capable of acceptance or rejection. Something that is enforced is not an offer'
    #this is hardcoding - can also use from PDFs

    #to design - if there has been no offer 
    1. could tell you what an offer is - if element is not satisfied - stop and explain to user what the element requirenents and why it isn't satisfied.
    #as its explanatory - ask AI