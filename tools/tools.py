from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(info: str):
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{info}")
    return res[0]["url"]
