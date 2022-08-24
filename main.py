import flet
from flet import Page, Text

def main(page: Page):
    text = Text(value="Todo")
    page.add(text)

flet.app(target=main)