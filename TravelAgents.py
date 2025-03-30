import os
from crewai import Agent
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from TravelTools import search_web_tool
from crewai import LLM
# from langchain_ollama.llms import OllamaLLM

load_dotenv()
os.getenv("GEMINI_API_KEY")
api_key=os.getenv("GEMINI_API_KEY")

url_base = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY"
provider_name = "google"

# Initialize LLM
gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    api_key= api_key
)

# Agents
guide_expert = Agent(
    role="City Local Guide Expert",
    goal="Provides information on things to do in the city based on user interests.",
    backstory="A local expert passionate about sharing city experiences.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=gemini_llm,
    allow_delegation=False,
)

location_expert = Agent(
    role="Travel Trip Expert",
    goal="Provides travel logistics and essential information under the budget which is in dollars.",
    backstory="A seasoned traveler who knows everything about different cities.",
    tools=[search_web_tool],  
    verbose=True,
    max_iter=5,
    llm= gemini_llm,   # ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    allow_delegation=False,
)

planner_expert = Agent(
    role="Travel Planning Expert",
    goal="Compiles all gathered information to create a travel plan under the budget which is in dollars.",
    backstory="An expert in planning seamless travel itineraries.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=gemini_llm,
    allow_delegation=False,
)