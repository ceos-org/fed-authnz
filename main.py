import argparse
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
WHITEPAPER_DIR = BASE_DIR / "WhitePaper"
MERMAID_DIR = WHITEPAPER_DIR / "img"
OUTPUT_FILE = WHITEPAPER_DIR / "mermaid_diagrams.md"

TITLES = {
    "oauth.mermaid": "OAuth 2.0 Authorization Code Flow",
    "oidc.mermaid": "OpenID Connect Authorization Code Flow",
    "delegated_oauth.mermaid": "Delegated Authentication via Federated Identity Provider",
    "delegated_oidc.mermaid": "Delegated Authentication with OpenID Connect (Federated)",
}


def format_markdown(filename: str, content: str) -> str:
    title = TITLES.get(filename, filename.replace("_", " ").rsplit(".", 1)[0])
    return f"### {title}\n\n```mermaid\n{content.rstrip()}\n```\n\n"


def generate_mermaid_markdown() -> pathlib.Path:
    if not MERMAID_DIR.exists() or not MERMAID_DIR.is_dir():
        raise SystemExit(f"Mermaid directory not found: {MERMAID_DIR}")

    parts = [
        "# Generated Mermaid Diagrams\n\n",
        "This file is generated from Mermaid source files in `WhitePaper/img`.\n\n",
    ]

    for path in sorted(MERMAID_DIR.glob("*.mermaid")):
        content = path.read_text(encoding="utf-8")
        parts.append(format_markdown(path.name, content))

    OUTPUT_FILE.write_text("".join(parts), encoding="utf-8")
    return OUTPUT_FILE


def main() -> None:
    parser = argparse.ArgumentParser(description="FederatedAuth command-line utilities.")
    parser.add_argument(
        "--generate-mermaid",
        action="store_true",
        help="Generate WhitePaper Mermaid diagrams markdown from `WhitePaper/img`.",
    )
    args = parser.parse_args()

    if args.generate_mermaid:
        output_file = generate_mermaid_markdown()
        print(f"Generated markdown to {output_file}")
    else:
        print("Hello from federatedauth!")


if __name__ == "__main__":
    main()
