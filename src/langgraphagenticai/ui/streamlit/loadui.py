import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfig_reader import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
            st.subheader("Configuration Settings")

            llm_models = self.config.get_llms()
            default_llm = self.config.config['DEFAULT'].get('DEFAULT_LLM_MODEL', llm_models[0])
            selected_llm = st.selectbox("Select LLM Model", llm_models, index=llm_models.index(default_llm))
            self.user_controls['selected_llm'] = selected_llm

            use_cases = self.config.get_use_cases()
            selected_use_case = st.selectbox("Select Use Case", use_cases)
            self.user_controls['selected_use_case'] = selected_use_case

            if self.user_controls['selected_llm'] == "Groq API":
                groq_models = self.config.get_groq_models()
                selected_groq_model = st.selectbox("Select Groq Model", groq_models)
                self.user_controls['selected_groq_model'] = selected_groq_model
                self.user_controls['api_key'] = st.session_state = st.text_input("Enter Groq API Key", type="password")
            elif self.user_controls['selected_llm'] == "OpenAI":
                openai_models = self.config.config['DEFAULT'].get('OPENAI_MODELS', '').split(', ')
                selected_openai_model = st.selectbox("Select OpenAI Model", openai_models)
                self.user_controls['selected_openai_model'] = selected_openai_model
                self.user_controls['api_key'] = st.session_state = st.text_input("Enter OpenAI API Key", type="password")
            elif self.user_controls['selected_llm'] == "Anthropic Claude":
                anthropic_models = self.config.config['DEFAULT'].get('ANTHROPIC_MODELS', '').split(', ')
                selected_anthropic_model = st.selectbox("Select Anthropic Model", anthropic_models)
                self.user_controls['selected_anthropic_model'] = selected_anthropic_model
                self.user_controls['api_key'] = st.session_state = st.text_input("Enter Anthropic API Key", type="password")
            else:
                st.warning("No models available for the selected LLM.")
    
        return self.user_controls