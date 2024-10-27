from langgraph.graph import StateGraph, MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from tools import query_knowledge_base, check_product_availability, data_protection_check, create_new_customer, place_order, retrieve_existing_customer_orders, track_delivery

import os


prompt = """#Purpose 

You are a customer service chatbot for a grocery store. You can help the customer achieve the goals listed below.

#Goals

1. Answer questions the user might have relating to services offered
2. Check product availability and recommend alternatives if needed
3. Help the customer check on an existing order status or track their delivery
4. To place and manage orders, you will need a customer profile (with an associated id). If the customer already has a profile, perform a data protection check to retrieve their details. If not, create them a profile.

#Tone

Helpful and friendly. Use casual language to keep things approachable. You MUST always include a fun food-related pun in every response."""

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', prompt),
        ('placeholder', "{messages}")
    ]
)

with open('./.env', 'r', encoding='utf-8') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

tools = [query_knowledge_base, check_product_availability, data_protection_check, create_new_customer, place_order, retrieve_existing_customer_orders, track_delivery]

llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=os.environ['OPENAI_API_KEY']
)

llm_with_prompt = chat_template | llm.bind_tools(tools)


def call_agent(message_state: MessagesState):
    
    response = llm_with_prompt.invoke(message_state)

    return {
        'messages': [response]
    }

def is_there_tool_calls(state: MessagesState):
    last_message = state['messages'][-1]
    if last_message.tool_calls:
        return 'tool_node'
    else:
        return '__end__'


graph = StateGraph(MessagesState)

tool_node = ToolNode(tools)

graph.add_node('agent', call_agent)
graph.add_node('tool_node', tool_node)

graph.add_conditional_edges(
    "agent",
    is_there_tool_calls
)
graph.add_edge('tool_node', 'agent')

graph.set_entry_point('agent')

app = graph.compile()

