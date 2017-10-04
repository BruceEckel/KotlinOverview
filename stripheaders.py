# Not finished, but working so far
from pathlib import Path
import re

kotlin_examples = re.compile("```kotlin.*?```", re.DOTALL)

def f(match):
    example = match.group(0)
    lines = example.splitlines()
    print(lines[0])
    print(lines[1])
    return example

stripped = kotlin_examples.sub(f, Path("KotlinOverview.md").read_text())
print(stripped)
