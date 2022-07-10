FROM python:3.9.4-slim as base

ARG GIT_BRANCH
ARG GIT_COMMIT_ID
ARG GIT_BUILD_TIME
ARG GITHUB_RUN_NUMBER
ARG GITHUB_RUN_ID
ARG PROJECT_URL

LABEL git.branch=${GIT_BRANCH}
LABEL git.commit.id=${GIT_COMMIT_ID}
LABEL git.build.time=${GIT_BUILD_TIME}
LABEL git.run.number=${GITHUB_RUN_NUMBER}
LABEL git.run.id=${GITHUB_RUN_ID}
LABEL org.opencontainers.image.authors="support@sixsq.com"
LABEL org.opencontainers.image.created=${GIT_BUILD_TIME}
LABEL org.opencontainers.image.url=${PROJECT_URL}
LABEL org.opencontainers.image.vendor="SixSq SA"
LABEL org.opencontainers.image.title="MQTT Fiware Base Bridge"
LABEL org.opencontainers.image.description="Base component for the ingestion and FIWARE validation of MQTT messages"


COPY code/ LICENSE /opt/nuvlabox/

WORKDIR /opt/nuvlabox/

RUN pip install .

ONBUILD RUN ./license.sh

ENTRYPOINT ["./main.py"]


FROM base as mqtt-to-mqtt

LABEL org.opencontainers.image.title="MQTT to MQTT Bridge"
LABEL org.opencontainers.image.description="Consumes MQTT messages from one broker and published to another"

COPY output_connectors/mqtt-to-mqtt/ ./

ENTRYPOINT ["./main.py"]
