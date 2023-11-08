from fastapi.templating import Jinja2Templates

TEMPLATES_PATH = "view/static/templates"

templates = Jinja2Templates(directory=TEMPLATES_PATH)
