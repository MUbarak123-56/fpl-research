from st_pages import Page, add_page_title, show_pages

show_pages(
    [
        Page("app.py", name="Home",icon= "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("pages/business_intelligence.py",name= "Business Intelligence", icon="📰"),
        # The pages appear in the order you pass them
        Page("pages/fpl_analyst.py", name="FPL Analyst", icon="🤖"),
    ]
)


add_page_title()

from st_pages import show_pages_from_config

show_pages_from_config()
