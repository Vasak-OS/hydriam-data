import Lynx.Menu
import json

menu = Lynx.Menu.Get().items()
print(f"{json.dumps(menu)}")