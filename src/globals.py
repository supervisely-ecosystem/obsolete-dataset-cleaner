import os
from distutils.util import strtobool

from dotenv import load_dotenv

import supervisely as sly

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

task_id = api.task_id
age = int(os.environ.get("modal.state.age"))
all_workspaces = bool(strtobool(os.environ.get("modal.state.allWorkspaces")))
workspace_id = int(os.environ.get("modal.state.workspaceId"))
sleep_days = int(os.environ.get("modal.state.sleep"))
sleep_time = sleep_days * 86400
stop = bool(strtobool(os.environ.get("modal.state.stop")))
