import streamlit as st
import os
from langchain_openai import ChatOpenAI

class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm(self):
        try:

            api_key = self.user_controls_input.get("api_key") or os.getenv("OPENAI_API_KEY")
            if not api_key:
                st.error("OpenAI API key is required. Please provide it in the user controls or set the OPENAI_API_KEY environment variable.")
                return None

            model_name = self.user_controls_input.get("selected_openai_model", "gpt-4")
            temperature = self.user_controls_input.get("openai_temperature", 0)

            llm = ChatOpenAI(
                model_name=model_name,
                temperature=temperature,
                openai_api_key=api_key
            )
        except Exception as e:
            st.error(f"Error initializing OpenAI LLM: {e}")
            return None
        return llm