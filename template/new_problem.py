import os
from os import path
from mako.template import Template


def main():
    base_dir = path.dirname(path.dirname(path.abspath(__file__)))
    context = {
        "number": max([int(f.split(".")[0][2:]) for f in os.listdir(path.join(base_dir, "src")) if not f.startswith("__")]) + 1,
        "title": input("Enter problem title: ").strip(),
        "descriptions": input("Enter problem description: ").strip().splitlines(),
    }
    temp = Template(filename=path.join(path.dirname(path.abspath(__file__)), "template.py.mako"))
    with open(path.join(base_dir, "src", f"PE{context['number']:04}.py"), "w") as f:
        f.write(temp.render(**context))


if __name__ == "__main__":
    main()
