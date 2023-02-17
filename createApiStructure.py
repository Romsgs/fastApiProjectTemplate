import os
import sys
routes_content = """
from fastapi import FastAPI
from decouple import config
from app.api.controllers.controller import controller
api = FastAPI()

@api.get("/exemple/{year}")
def funtion_to_execute(year: int):
    response = controller(year)
    return response
"""
controller_content = """
def controller(year):
    return f"The year is {year}"
"""
main_content = """
from fastapi import FastAPI
import uvicorn
from app.api.routes.router import api


def start_api(api):

    app=FastAPI(
        title="balance-income-report",
        description="Balance Income Report API",
        version="1"
    )
    app.include_router(api)

    uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    start_api(api)
             
             """
current_folder = os.getcwd()
new_folder_name = str(sys.argv[1])

base_path = os.path.join(current_folder, new_folder_name)
print(current_folder)
print(new_folder_name)
print(base_path)
os.makedirs(base_path)
os.makedirs(os.path.join(base_path, 'app'))
with open(os.path.join(base_path, 'app/__init__.py'), 'w') as file:
    file.write('')
with open(os.path.join(base_path, 'main.py'), 'w') as file:
    file.write(main_content)
os.makedirs(os.path.join(base_path, 'app/api'))
with open(os.path.join(base_path, 'app/api/__init__.py'), 'w') as file:
    file.write('')
os.makedirs(os.path.join(base_path, 'app/api/routes'))
with open(os.path.join(base_path, 'app/api/routes/__init__.py'), 'w') as file:
    file.write('')
with open(os.path.join(base_path, 'app/api/routes/router.py'), 'w') as file:
    file.write(routes_content)
os.makedirs(os.path.join(base_path, 'app/api/controllers'))
with open(os.path.join(base_path, 'app/api/controllers/__init__.py'), 'w') as file:
    file.write('')
with open(os.path.join(base_path, 'app/api/controllers/controller.py'), 'w') as file:
    file.write(controller_content)
os.makedirs(os.path.join(base_path, 'app/api/services'))
with open(os.path.join(base_path, 'app/api/services/__init__.py'), 'w') as file:
    file.write('')
os.makedirs(os.path.join(base_path, 'app/repository'))
with open(os.path.join(base_path, 'app/repository/__init__.py'), 'w') as file:
    file.write('')
