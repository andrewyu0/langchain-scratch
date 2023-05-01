# https://python.langchain.com/en/latest/getting_started/getting_started.html
from langchain.prompts import PromptTemplate 
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# ---- LLMs: Get predictions from a language model
llm = OpenAI(temperature=0.9)

text = "what would be a good company name for a company that makes colorful socks?"
# print(llm(text))


# ---- Prompt Templates: Manage prompts for LLMs
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

print(prompt.format(product="colorful socks"))

# --- Chains: Combine LLMs and prompts in multi-step workflows
chain = LLMChain(llm=llm, prompt=prompt)
chain.run("colorful socks")

# Agents: Dynamically Call Chains Based on User Input
