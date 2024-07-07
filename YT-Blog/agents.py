from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()

from langchain.llms import Ollama

os.environ["OPENAI_API_KEY"] = "NA"

llm = Ollama(
    model = "llama2",
    base_url = "http://localhost:11434")

blog_re = Agent(
    role= 'Blog research specialist for YOUTUBE Video content',
    goal='get the most important content of the video content for the topic{topic} from the YouTube Channel',
    verbose=True,
    memory=True,
    backstory=(
        "An experienced expert in understanding any youtube videos in the domain of Machine Learning, Data Science, Artificial Intelligence, Generative AI, Deep Learning and related domains"
    ),
    llm= llm,
    tools=[yt_tool],
    allow_delegation= True
)

# senior blog writer agent

blog_wr = Agent(
    role='Experienced Blog writer',
    goal='Narrate brilliant tech stories often in innovative way to attract more people to tech domain about any YouTube video {topic} ',
    verbose=True,
    memory=True,
    backstory = (
    "You possess a unique talent for distilling intricate concepts into simple, relatable terms. "
    "Your compelling narratives not only captivate and educate but also inspire curiosity and wonder, "
    "making even the most complex discoveries feel accessible and exciting. "
    "Through your storytelling, you illuminate new ideas and insights, transforming them into engaging "
    "and memorable experiences for your audience."
    ),
    llm= llm,
    tools=[yt_tool],
    allow_delegation=False
     )