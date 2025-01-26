def page7():
    st.header("Survey Questions (Part I)")
    st.markdown(
        """
        <div class="custom-text">
            <ul>
                <strong>Text 1</strong>
            </ul>
        </div> <br><br>
        """,
        unsafe_allow_html=True,
    )

    if "style" not in st.session_state:
        st.session_state["style"] = None  # No default value

    # Callback function to update session state
    def update_slider():
        st.session_state["style"] = st.session_state["style_slider"]

    # Create columns for the labels and slider
    col1, col2, col3 = st.columns([1, 4, 1])

    # Add "Very Feminine" label on the left
    with col1:
        st.markdown("<div style='text-align: right;'>Very Feminine</div>", unsafe_allow_html=True)

    # Add the slider in the middle
    with col2:
        # Use a unique key for the slider and link it to the callback

        selected_value = st.slider(
            "",
            min_value=1,
            max_value=5,
            step=1,
            value=st.session_state["style"],  # Link to session state
            key="style_slider",  # Unique key for the slider
            on_change=update_slider,  # Callback to update session state
        )

    # Add "Very Masculine" label on the right
    with col3:
        st.markdown("<div style='text-align: left;'>Very Masculine</div>", unsafe_allow_html=True)

    # Display the selected value (if any)
    if st.session_state["style"] is not None:
        st.write(f"Selected value: {st.session_state['style']}")
    else:
        st.write("No value selected yet.")



    st.session_state["confidence"] = st.selectbox(
        "Confidence Level",
        ["1: Not Confident. You were unsure or found the text ambiguous",
         "2: Somewhat Confident. You made a judgment but still felt uncertain or had significant doubts",
         "3: Moderately Confident. You felt reasonably sure of your judgment but had some doubts",
         "4: Very Confident. You were very certain about your judgment with no hesitation"],
        index=None  # Set index based on the stored value
    )
    st.session_state["comments"] = st.text_area(
        "Comments (Optional)",
        value=st.session_state.get("comments", ""),
    )

    if st.button("Next", disabled=not st.session_state.get("style")):
        st.session_state["current_page"] = "Page 8"
        st.rerun()
    if st.button("Back"):
        st.session_state["current_page"] = "Page 6"
        st.rerun()
