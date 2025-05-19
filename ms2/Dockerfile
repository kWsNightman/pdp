FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ms2 /ms2/

# Install the application dependencies.
WORKDIR /ms2/
ENV PATH="/ms2/.venv/bin:$PATH"
RUN uv sync --locked

# Run the application.
CMD ["uv", "run", "consumer.py"]

