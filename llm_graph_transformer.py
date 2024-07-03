
import openai
import logging
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
#from langchain_openai import ChatOpenAI

# class LLMGraphTransformer:
#     def __init__(self, graph, openai_api_key):
#         self.graph = graph
#         openai.api_key = openai_api_key
#         llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo",openai_api_key=openai_api_key)
#         prompt_template = PromptTemplate(template="{query}\nContext: {context}", input_variables=["query", "context"])
#         self.chain = LLMChain(llm=llm, prompt=prompt_template)

#     def generate_response(self, query):
#         context = self.graph.retrieve_context(query)
#         response = self.chain.run(query=query, context=context)
#         return response


class LLMGraphTransformer:
    def __init__(self, graph, openai_api_key):
        self.graph = graph
        
        # Setup OpenAI API key
        openai.api_key = openai_api_key

        # Initialize LLM and PromptTemplate
        try:
            llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
        except Exception as e:
            logging.error(f"Failed to initialize OpenAI model: {e}")
            raise

        prompt_template = PromptTemplate(template="{query}\nContext: {context}", input_variables=["query", "context"])
        self.chain = LLMChain(llm=llm, prompt=prompt_template)

    def generate_response(self, query):
        try:
            context = self.graph.retrieve_context(query)
            response = self.chain.run(query=query, context=context)
            return response
        except Exception as e:
            logging.error(f"Failed to generate response: {e}")
            return "An error occurred while generating the response."