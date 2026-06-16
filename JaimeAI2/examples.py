# Project Maker
from main import ask
from printing import slow

typeProject = input('Choose a project type: html, txt, or md > ')

slow("\n" + ask(f"make a project {typeProject}"))