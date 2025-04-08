from crewai_tools import ScrapeWebsiteTool

# Initializing the tool with the website URL, 
# so the agent can only scrap the content of the specified website

docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://www.coursera.org/?gad_source=1"
)                      