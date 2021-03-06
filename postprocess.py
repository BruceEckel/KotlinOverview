from pathlib import Path
html = Path("KotlinOverview.html")

if __name__ == '__main__':
    result = []
    for line in html.read_text().splitlines():
        result.append(line)
        if line.startswith("td.lineNumbers"):
            result.append(".reveal pre code { font-size: 1.3em; line-height: 110%; }")
            result.append("body .reveal h1 { font-size: 3em; }")
    html.write_text("\n".join(result))
