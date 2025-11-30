from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:
    def __init__(self, llm):
        self.llm = llm
        

    def process(self, state: State) -> dict:
        """
            Process the input state and generate a response using the LLM model.
        """
        user_input = state['message'][-1] if state['message'] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        #Simulate tool specific logic here
        tools_response = f"Tool integration for input: {user_input}"

        return {"message": [llm_response, tools_response]}
    

    def create_chatbot(self, tools):
        """
          Returns a chatbot node function
        """
        llm_with_tools = self.llm.with_tools(tools)
        # llm_with_tools = initialize_agent(
        #     tools,
        #     self.llm,
        #     agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        #     verbose=True
        # )
      
        def chatbot_node(state: State):
            """
                Chatbot logic for processing the input state and returning a response
                
            """

            return {"message": llm_with_tools.invoke(state['message'])}
        return chatbot_node