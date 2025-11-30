import streamlit as st
from src.langgraphagenticai.ui.streamlit.loadui import LoadStreamlitUI
import os
from src.langgraphagenticai.LLMs.openai_llm import OpenAILLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlit.display_result import DisplayResult
def load_langgraph_agenticai_ui():

    """
    
    Load the LangGraph Agentic AI ChatBot Streamlit UI.
    
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_ui()

    if not user_input:
        st.warning("Please select LLM model and use case to proceed.")
        return
    
    user_message = st.chat_input("Enter your message here...")
    print(user_message)

    if user_message:
        try:
            llm_obj = OpenAILLM(user_controls_input=user_input)
            llm = llm_obj.get_llm()
            if not llm:
                st.error("Failed to initialize the LLM. Please check your API key and settings.")
                return
            usecase = user_input.get("selected_use_case")
            print(f"Selected use case: {usecase}")
            if usecase == "Basic Chatbot" or "Chatbot with Web":

                print("Building graph for Basic Chatbot...")

                graph_builder = GraphBuilder(model=llm)
                print("Setting up graph...")
                try:
                    graph = graph_builder.setup_graph(usecase)
                    print("Graph setup complete.")
                    DisplayResult(usecase, graph, user_message).display_result_on_ui()
                except ValueError as ve:
                    st.error(str(ve))
                    return
            else:
                st.error(f"Unsupported use case selected: {usecase}")
                return

        except Exception as e:
            st.error(f"An error occurred: {e}")
            return               

