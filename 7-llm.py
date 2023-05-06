from langchain.llms import OpenAI
llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

# result = llm("Tell me a joke")
# print(result)

llm_result = llm.generate(["Tell me a joke", "Tell me a poem"]*15)
print(len(llm_result.generations))
print(llm_result.generations[0])
print(llm_result.generations[-1])
