from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

web_search_agent=Agent(
    name="web search agent",
    role="search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tools-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include the sources"],
    show_tool_calls=True,
    markdown=True
)

# Financial Agent

finance_agent = Agent(
    name="Finance_ai_ahent",
    model=Groq(id="llama3-groq-70b-8192-tools-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instruction=["Use Tables to display data"],
    show_tool_calls=True,
    markdown=True
)


multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include the sources", "Use Tables to display data"],

)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news about NVDA",stream=True)