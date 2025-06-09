# from langchain_openai import ChatOpenAI
# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# from dotenv import load_dotenv


# load_dotenv()

# llm = ChatOpenAI(model="gpt-4o")

# result = llm.invoke("What is the capital of France?")
# print(result)


# llm = HuggingFacePipeline.from_model_id(
#     model_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         max_new_tokens=512,
#         do_sample=False,
#         repetition_penalty=1.03,
#     ),
# )

# chat_model = ChatHuggingFace(llm=llm)
# result = chat_model.invoke("what is 5 X 5?")
# print(result)


# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatOpenAI(model='gpt-4o')
# chat_history = []
# system_message = SystemMessage('you are a helpful assistant')
# chat_history.append(system_message)

# while True:
#     query = input("You:")
#     if query.lower() == 'exit':
#         break
#     chat_history.append(HumanMessage(content=query))
#     result = llm.invoke(chat_history)
#     chat_history.append(AIMessage(content=result.content))
#     print(f"AI:{result.content}")

# print("Message History")
# print(chat_history)


from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

PROJECT_ID = "langchain-5eaaa"
SESSION_ID = "sadjlksdjf"
COLLECTION_NAME = "chat_history"

firestore_client = firestore.Client(project=PROJECT_ID)
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID, collection=COLLECTION_NAME, client=firestore_client
)
print("chat history initialized", chat_history.messages)
model = ChatOpenAI(model="gpt-4o")
print("model initialized", model)
while True:
    query = input("You:")
    if query.lower() == "exit":
        break
    chat_history.add_user_message(query)
    result = model.invoke(chat_history.messages)
    chat_history.add_ai_message(result.content)
    print(f"AI:{result.content}")
print("Message History")
print(chat_history.messages)
