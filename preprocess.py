from pathlib import Path
import re
import io

example_source = Path.cwd().parent / "AtomicKotlinExamples" / "Examples"


def insert_referenced_files(source_file):
    result = io.StringIO()
    def add(str): print(str, file=result)
    for line in Path(source_file).read_text().splitlines():
        if line.strip().startswith("{{"):
            add("```kotlin")
            code = example_source / line[line.find("{{") + 2 : line.find("}}")]
            add(f"{code.read_text().strip()}")
            add("```")
        else:
            add(line)
    return result.getvalue()


def strip_unnecessary(match):
    lines = match.group(0).splitlines()
    def remove(str):
        while lines[1].startswith(str) or lines[1].strip() == "":
            del lines[1]
    remove("//")
    remove("package")
    remove("import atomictest")
    return "\n".join(lines)


if __name__ == '__main__':
    with_examples = insert_referenced_files("KotlinOverviewSource.md")
    kotlin_examples = re.compile("```kotlin.*?```", re.DOTALL)
    stripped = kotlin_examples.sub(strip_unnecessary, with_examples)
    Path("KotlinOverview.md").write_text(stripped)
