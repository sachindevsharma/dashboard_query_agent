from dotenv import load_dotenv
from dataclasses import dataclass
from langchain_groq import ChatGroq

load_dotenv()


@dataclass
class ChatBot:
    llm_model_name: str = "llama-3.1-8b-instant"
    system_message: str = "You are an assistant."

    def invoke(self, query):
        messages = [
            ("system", self.system_message),
            ("human", query)
        ]
        output = self.LLM_MODEL.invoke(messages).content
        return output
    
    @property
    def LLM_MODEL(self):
        
        llm = ChatGroq(
            model=self.llm_model_name,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        return llm