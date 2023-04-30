FROM python
WORKDIR /app
COPY https.py .
RUN python -m pip install flask
ENTRYPOINT [ "python" ]
CMD ["https.py" ]
