#FROM python:3.12-slim
#
#RUN pip install uv
#
#WORKDIR /ms1/
#COPY pyproject.toml uv.lock ms1 /ms1/
#RUN uv sync
#RUN pip install uvicorn["standard"]
#
#CMD ["uv", "run", "uvicorn", "producer:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ms1 /ms1/

# Install the application dependencies.
WORKDIR /ms1/
ENV PATH="/ms1/.venv/bin:$PATH"
RUN uv add uvicorn["standard"]
RUN uv sync --locked

# Run the application.
CMD ["uv", "run", "uvicorn", "producer:app", "--port", "8000", "--host", "0.0.0.0"]

