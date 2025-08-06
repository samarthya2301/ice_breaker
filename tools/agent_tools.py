from langchain_tavily import TavilySearch

# Tavily API provides a way to connect to internet and get the information we want
# Tavily crawls the internet and get the info, specialized for gen ai applications
def get_profile_url_tavily(name: str):
	"""Searches for LinkedIn or Twitter Profile Page."""

	# Comment this code for now, otherwise credits will be wasted
	# search = TavilySearch()
	# response = search.run(f"{name}")
	# return response

	# Hardcoding one response for Samarthya Bararia LinkedIn
	return "{'query': 'Samarthya Bararia', 'follow_up_questions': None, 'answer': None, 'images': [], 'results': [{'url': 'https://www.zoominfo.com/p/Samarthya-Bararia/10124419770', 'title': 'Contact Samarthya Bararia, Email: ****@capgemini.com & Phone ...', 'content': 'Samarthya Bararia is a Senior Software Engineer at Capgemini based in Paris, Ile-de-France. Previously, Samarthya was a Senior Software Engineer at Capgemini.', 'score': 0.89324445, 'raw_content': None}, {'url': 'https://stackexchange.com/users/21839718/samarthya-bararia', 'title': 'User Samarthya Bararia - Stack Exchange', 'content': 'Samarthya Bararia. Dehradun, Uttarakhand, India. top accounts reputation activity subscriptions. Top Questions. No questions with score of 5 or more. Top', 'score': 0.6742441, 'raw_content': None}, {'url': 'https://in.linkedin.com/in/samarthyabararia', 'title': 'Samarthya Bararia - Senior Software Engineer @ Capgemini', 'content': 'Senior Software Engineer @ Capgemini · Experience: Capgemini · Education: Graphic Era Hill University · Location: Pune · 438 connections on LinkedIn.', 'score': 0.6052631, 'raw_content': None}, {'url': 'https://github.com/samarthya2301', 'title': 'Samarthya Bararia samarthya2301 - GitHub', 'content': 'Interested in Android Development, RDBMS, Data Structures and Algorithms. Dehradun, India; https://www.linkedin.com/in/samarthyabararia/. Block or Report', 'score': 0.59655124, 'raw_content': None}, {'url': 'https://www.facebook.com/samarthya.bararia', 'title': 'Samarthya Bararia - Facebook', 'content': 'From Dehra Dun, India. \U000f16b7. Single. Photos. \U000f160b. Photos. See more from Samarthya Bararia. Log in to see posts from this account and find other people you may', 'score': 0.52948296, 'raw_content': None}], 'response_time': 1.31}"