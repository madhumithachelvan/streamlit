import streamlit as st

# Initialize session state for page navigation and responses
if "page" not in st.session_state:
    st.session_state.page = 1
if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = None
if "satisfaction" not in st.session_state:
    st.session_state.satisfaction = ""
if "comments" not in st.session_state:
    st.session_state.comments = ""


# Function to go to the next page
def next_page():
    st.session_state.page += 1


# Function to go to the previous page
def prev_page():
    st.session_state.page -= 1


# Page 1: Basic Information
if st.session_state.page == 1:
    st.title("Page 1: Basic Information")

    # Collect user input
    name = st.text_input("What is your name?", value=st.session_state.name)
    age = st.number_input("What is your age?", min_value=0, max_value=120, value=st.session_state.age or 0)

    # Save responses to session state
    st.session_state.name = name
    st.session_state.age = age

    # Navigation button
    if st.button("Next Page"):
        if name.strip() == "" or age == 0:
            st.error("Please fill out all fields before proceeding.")
        else:
            next_page()
            st.rerun()

# Page 2: Feedback
elif st.session_state.page == 2:
    st.title("Page 2: Feedback")

    st.write(f"Hello, {st.session_state.name}! Let's get your feedback.")

    # Collect user input
    satisfaction = st.radio(
        "How satisfied are you with our service?",
        ("Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"),
        index=["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"].index(
            st.session_state.satisfaction) if st.session_state.satisfaction else 0
    )

    comments = st.text_area("Any additional comments?", value=st.session_state.comments)

    # Save responses to session state
    st.session_state.satisfaction = satisfaction
    st.session_state.comments = comments

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous Page"):
            prev_page()
            st.rerun()
    with col2:
        if st.button("Submit"):
            # Display thank you message and responses
            st.success("Thank you for completing the survey!")
            st.write(f"**Name:** {st.session_state.name}")
            st.write(f"**Age:** {st.session_state.age}")
            st.write(f"**Satisfaction:** {st.session_state.satisfaction}")
            st.write(f"**Comments:** {st.session_state.comments}")

            # Optionally, save responses to a file or database here
            # For example, save to a CSV file:
            import pandas as pd

            responses = pd.DataFrame({
                "Name": [st.session_state.name],
                "Age": [st.session_state.age],
                "Satisfaction": [st.session_state.satisfaction],
                "Comments": [st.session_state.comments]
            })
            responses.to_csv("survey_responses.csv", mode="a",
                             header=not pd.io.common.file_exists("survey_responses.csv"), index=False)