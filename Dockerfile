FROM python:3.9.5-slim-buster as base

# Set up venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip && pip install pip-tools
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.9.5-slim-buster as runtime
COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Switch to non-root user
RUN groupadd -r user && useradd -r -g user user
USER user

# Run application
ENTRYPOINT ["python", "-m", "src.updater"]
