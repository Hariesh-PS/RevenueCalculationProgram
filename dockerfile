FROM python:3.9-slim-buster

# Create a directory to store data
RUN mkdir /data
RUN pip install pytest

# Copy main code, test code, and data to the container

COPY revenue.py .
COPY orders.csv .
COPY test_revenue.py .

CMD ["pytest", "-v", "test_revenue.py"]
