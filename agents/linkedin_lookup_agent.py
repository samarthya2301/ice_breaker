from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.agent_tools import get_profile_url_tavily

load_dotenv()

def linkedin_lookup_agent(name: str) -> str:

	# The LLM
	llm = ChatOpenAI(
		temperature=0,
		model="gpt-4o-mini"
	)

	# Template to give to LLM
	template = """
	Given the full name {name_of_person} of a person. \
	I want you to get me a link to their LinkedIn profile page. \
	Your answer should only contain a URL.
	"""

	# Instantiate the actual template
	prompt_template = PromptTemplate(
		template=template,
		input_variables=["name_of_person"]
	)

	# Will contain all the tools for the agent
	# A Tool will contain -
	# name - agent is going to refer to this tool, supplied to reasoning engine
	# func - pattern function
	# description - vvv.imp. llm determines to use this tool or not
	tools_for_agent = [
		Tool(
			name="Crawl Google 4 LinkedIn Profile Page",
			func=get_profile_url_tavily,
			description="Useful for when you need to get the LinkedIn Page URL"
		)
	]

	# Use a pre-made prompt in the langchain community
	# hwchase/react - ReAct agent
	react_prompt = hub.pull("hwchase17/react")

	# Instantiate the ReAct agent
	# LLM, Tools, ReAct Prompt
	agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

	# Create the runtime for the agent
	agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)

	# Execute the agent, with the prompt you created earlier
	response = agent_executor.invoke(
		input={
			"input": prompt_template.format_prompt(name_of_person=name)
		}
	)

	# Extract the output from response object
	linkedin_profile_url = response["output"]
	return linkedin_profile_url

if __name__ == "__main__":
	pass