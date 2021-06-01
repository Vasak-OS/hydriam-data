import Lynx.Menu
import json

menu = Lynx.Menu.Get().items()
print(f"Lynx.menu = {json.dumps(menu)}")