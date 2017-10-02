from pathlib import Path
import io

example_source = Path.cwd().parent / "AtomicKotlinExamples" / "Examples"

processed = io.StringIO()

for line in Path("ResistingKotlin.md").read_text().splitlines():
    if line.strip().startswith("{{"):
        print("```kotlin", file=processed)
        code = example_source / line[line.find("{{") + 2 : line.find("}}")]
        print(f"{code.read_text().strip()}", file=processed)
        print("```", file=processed)
    else:
        print(line, file=processed)

Path("ResistingKotlin-processed.md").write_text(processed.getvalue())
