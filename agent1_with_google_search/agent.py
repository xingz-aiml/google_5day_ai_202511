"""Agent with Google Search capability - run with: adk run agent1_with_google_search"""

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

# Retry configuration for handling rate limits
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# Define the root agent (ADK looks for this variable)
root_agent = Agent(
    name="search_assistant",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config,
    ),
    description="An assistant that can search Google for current information.",
    instruction="""You are a helpful assistant with access to Google Search.
    
Use Google Search when:
- The user asks about current events, news, or real-time information
- You need up-to-date facts or data
- You're unsure about something and want to verify

Always provide clear, accurate responses based on search results.""",
    tools=[google_search],
)
