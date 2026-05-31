# Agent Instructions

## App Shape

- This is a small Flask marketing site. The app entrypoint is `app.py`; routes are `/`, `/services`, and `/contact`.
- Templates live in `templates/`: `base.html` is the shared layout, and `index.html`, `services.html`, `contact.html` map to the three routes.
- Static styling is centralized in `static/style.css`; there is no frontend build step or package manifest.
- The contact form only flashes a thank-you message on POST; it does not send email or persist submissions.
- `hello.py` is a standalone hello-world script, not part of the Flask app.

## Commands

- Create the local venv if needed: `python3 -m venv .venv`.
- Install dependencies: `.venv/bin/pip install -r requirements.txt`.
- Run the app: `.venv/bin/python app.py`; Flask starts in debug mode at `http://127.0.0.1:5000`.
- There is no configured test, lint, format, typecheck, codegen, or CI command. Do not invent one.

## Verification

- For template or CSS changes, run the Flask app and verify the affected routes in a browser; HTTP 200 alone is not enough for visual changes.
- `browser-use` is available in this workspace and works well for headless or headed route checks against the local app.
- If using browser tooling, close browser sessions and stop the Flask server when done unless the user asks to keep them open.

## Repo Notes

- `.venv/` is ignored by `.gitignore`; do not commit it.
- `opencode-reviews/` is also ignored; treat it as local agent output if present.
- No `README*`, lockfile, GitHub Actions workflow, pre-commit config, or repo-local OpenCode config was present when this file was updated.
- Prefer executable sources such as `requirements.txt`, `app.py`, and future config files over stale prose.
