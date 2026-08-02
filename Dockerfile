FROM python:3.11-slim

WORKDIR /app

# Build arguments
ARG MONGO_URI
ARG DATABASE_NAME
ARG OLLAMA_MODEL
ARG SECRET_KEY

# Make them available at runtime
ENV MONGO_URI=${MONGO_URI}
ENV DATABASE_NAME=${DATABASE_NAME}
ENV OLLAMA_MODEL=${OLLAMA_MODEL}
ENV SECRET_KEY=${SECRET_KEY}

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]