from secret_key import openapi_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature = 0.7)

def generate_restaurant_name_and_items(cuisine):
    
    llm = OpenAI(temperature = 0.7)

    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want top open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "restaurant_name")

    prompt_template_items = prompt_template_name = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = " Suggest some menu items for {restaurant_name} food. Return it as a comma seperated list"
    )

    food_items_chain = LLMChain(llm = llm, prompt = prompt_template_items, output_key = "menu_items")   
    
    chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine'})

    return response




