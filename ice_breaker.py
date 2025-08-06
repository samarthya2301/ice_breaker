from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrap_linkedin_profile
from agents.linkedin_lookup_agent import linkedin_lookup_agent
from output_parsers import Summary, summary_parser_json

load_dotenv()

def get_linkedin_data(name: str):

	# Query about the linkedin profile from the agent
	linkedin_url = linkedin_lookup_agent(name=name)

	# Agent will return a linkedin profile url, pass that on
	linkedin_data = scrap_linkedin_profile(linkedin_url, mock=True)

	return linkedin_data

def get_prompt_template():

	template = """
	Given the LinkedIn information in a JSON format, delimited by 3 backtics about a person. \
	Create the following \
	1. A short summary about the person of 30-40 words
	2. Two facts about the person of 15-20 words each

	The above stated requests must be only from the information provided \

	Information: ```{information}``` \
	
	\n{format_instructions}
	"""

	return PromptTemplate(
		input_variables="information",
		template=template,
		partial_variables={
			"format_instructions": summary_parser_json.get_format_instructions
		}
	)

def ice_break_with(name: str) -> Summary:

	linkedin_data = get_linkedin_data(name)
	prompt_template = get_prompt_template()

	llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
	chain = prompt_template | llm | summary_parser_json

	response: Summary = chain.invoke(
		input={
			"information": linkedin_data,
		}
	)
	return response

if __name__ == '__main__':

	print("Hello, LangChain!\n***** ICE BREAKER *****")
	response: Summary = ice_break_with("Samarthya Bararia")
	print(response.model_dump_json())