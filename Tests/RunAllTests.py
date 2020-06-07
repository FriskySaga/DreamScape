"""
Run all tests
"""

import os

TESTS_FOLDER = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(os.path.join(TESTS_FOLDER, "UnitTests")):
  for fileName in files:
    if not fileName.endswith(".py"):
      continue

    if fileName != "__init__.py":
      print(f"Running {fileName}...")
      os.system(f"python {os.path.join(root, fileName)}")

for root, dirs, files in os.walk(os.path.join(TESTS_FOLDER, "ScenarioTests")):
  for fileName in files:
    if not fileName.endswith(".py"):
      continue

    if fileName != "__init__.py":
      print(f"Running {fileName}...")
      os.system(f"python {os.path.join(root, fileName)}")