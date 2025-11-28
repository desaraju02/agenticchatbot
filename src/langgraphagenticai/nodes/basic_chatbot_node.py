
from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
        Basic chatbox implementation for LangGraphAgent.

    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
            Process the input state and generate a response using the LLM model.
        """
        return {"message": self.llm.invoke(state['message'])}