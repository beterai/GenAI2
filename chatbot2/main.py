from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, PromptHelper, ServiceContext
from llama_index import *
from langchain import OpenAI

import os
import openai
import modal

os.environ["OPENAI_API_KEY"] = ""

class LOL:
    
    
    def createVectorIndex(path):

        openai.api_key=""
        max_input = 4096
        tokens = 256
        chunk_size = 600
        max_chunk_overlap = 0.5


        prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)
        
        lLMPredictor = LLMPredictor(llm=OpenAI(temperature=0, model="text-davinci-003", max_tokens=tokens, openai_api_key=os.getenv("OPENAI_API_KEY")))
        
        docs = SimpleDirectoryReader(path).load_data()

        service_context = ServiceContext.from_defaults(llm_predictor=lLMPredictor, prompt_helper=prompt_helper)
        vectorIndex = GPTVectorStoreIndex.from_documents(documents=docs, service_context=service_context)
        vectorIndex.storage_context.persist('./idk')
        return vectorIndex

    vectorIndex = createVectorIndex('Knowledge')

    def answerMe(input_text):


        openai.api_key = ""
        storage_context = StorageContext.from_defaults(persist_dir="./idk")
        index = load_index_from_storage(storage_context)

        query_engine = index.as_query_engine()
        response = query_engine.query(input_text)
        return response.response
