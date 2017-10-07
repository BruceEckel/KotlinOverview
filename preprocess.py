from pathlib import Path
import re
import io

example_source = Path.cwd().parent / "AtomicKotlinExamples" / "Examples"


def insert_referenced_files(source_file):
    result = io.StringIO()
    for line in Path(source_file).read_text().splitlines():
        if line.strip().startswith("{{"):
            print("```kotlin", file=result)
            code = example_source / line[line.find("{{") + 2 : line.find("}}")]
            print(f"{code.read_text().strip()}", file=result)
            print("```", file=result)
        else:
            print(line, file=result)
    return result.getvalue()


def strip_unnecessary(match):
    lines = match.group(0).splitlines()
    assert lines[0].startswith("```kotlin")
    while lines[1].startswith("//"):
        del lines[1]
    while lines[1].startswith("package") or lines[1].strip() == "":
        del lines[1]
    return "\n".join(lines)


# def strip_unnecessary(match):
#     filter_unnecessary(match.group(0).splitlines())
#     return example


if __name__ == '__main__':
    with_examples = insert_referenced_files("KotlinOverviewSource.md")
    kotlin_examples = re.compile("```kotlin.*?```", re.DOTALL)
    stripped = kotlin_examples.sub(strip_unnecessary, with_examples)
    Path("KotlinOverview.md").write_text(stripped)
