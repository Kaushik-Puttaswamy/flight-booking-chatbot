FROM rasa/rasa:3.1.2-full

USER root

# Install backend dependencies
RUN apt-get update && apt-get install -y python3-pip
COPY backend/ /app/backend/
RUN pip install -r /app/backend/requirements.txt

# Copy action server
COPY chatbot/actions /app/actions

WORKDIR /app

CMD ["run", "actions", "--actions", "actions"]