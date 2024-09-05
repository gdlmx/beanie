import logging
import json
from beanie.odm.utils.init import Initializer
from typing import List
from pydantic import Field
from beanie import Document, Link, BackLink

class Task(Document):
    detail: str
    owner:  Link["User"] | None = None

class User(Document):
    name: str
    tasks: List[BackLink["Task"]] = Field(json_schema_extra={"original_field": "owner"})


def test_json_schema():
    json_schema = User.model_json_schema()
    # logging.info("task schema: %s", json_schema)
    assert json_schema['properties']['tasks']['items']['type'] == 'object'
    