FROM python:3.7-slim
RUN pip3 install japronto jinja2 redis panoramisk
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["japronto"]
