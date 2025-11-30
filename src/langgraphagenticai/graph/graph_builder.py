from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import create_tool_node, get_tools
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode


class GraphBuilder:
    def __init__(self, model):
       self.llm = model
       self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
            Build a basic chatbot graph structure using Langgraph.
            This method initializes a chatbot node using the BasicChatbot Node class
            and integrated it into the graph structure.
            The  chatbot node  is set as both the enntry and exit point of the graph.
        """
        print("Building Basic Chatbot node...")
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        print("llm integrated is: ", self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        print("Basic Chatbot graph built successfully.")


    def  chatbot_with_web_build_graph(self):
        """
            A chatbot with web integration graph structure.
            This method creates a choatbot graph that includes both a choatbot node and a tool node.
            It defines tools, initializes the chatbot with tool capabilities and sets up conditional and direct edges between nodes.
            The chatbot node is set as the entry point.

        """
        ## Define tool and tool node
        #   # To be implemented in the future
        tools = get_tools() 
        print("Got the tools: ", tools)
        print("Creating Tool node...")
        tool_node = create_tool_node(tools)
        print("Tool node created.")

        # Define the LLM
        llm = self.llm
        print("LLM defined.")
        # Define the chatbot node with tool capabilities
        print("Creating Chatbot with Tool node...")
        chat_with_tools_llm =  ChatbotWithToolNode(llm)
        print("Building Chatbot with Tool node...")
       
        chatbot_with_tool_node = chat_with_tools_llm.create_chatbot(tools)
        print("Chatbot with Tool node created.")
        # Add nodes
        self.graph_builder.add_node("chatbot", chatbot_with_tool_node)
        self.graph_builder.add_node("tools", tool_node)
        print("Nodes added to the graph.")
        # Add Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        print("Edges added to the graph.")

    def setup_graph(self, usecase: str):
        """
            Setup the graph based on the selected use case.
            Currently supports only "Basic ChatBot" use case.
        """
        if usecase == "Basic Chatbot":
            print("Setting up Basic Chatbot graph...")
            self.basic_chatbot_build_graph()
            return self.graph_builder.compile()
        elif usecase == "Chatbot with Web":
            print("Setting up Chatbot with Web graph...")
            self.chatbot_with_web_build_graph()
            return self.graph_builder.compile()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")