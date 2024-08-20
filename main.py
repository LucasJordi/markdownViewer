import streamlit as st
st.set_page_config(
    page_title="MarkDown Viewer",  # Page title that appears in the browser tab
)
def main():
    st.title("Markdown Viewer")

    # File uploader
    uploaded_file = st.file_uploader("Upload a Markdown file (.md)", type="md")

    # Text area for direct Markdown input
    st.sidebar.header("Or write Markdown text here:")
    markdown_text = st.sidebar.text_area("Markdown Text", height=300)

    if uploaded_file is not None:
        # Read and display the content from the uploaded file
        file_content = uploaded_file.read().decode("utf-8")
        st.markdown(file_content, unsafe_allow_html=True)
    elif markdown_text:
        # Display the content from the text area
        st.markdown(markdown_text, unsafe_allow_html=True)
    else:
        st.write("Upload a Markdown file or enter Markdown text in the sidebar.")

if __name__ == "__main__":
    main()
