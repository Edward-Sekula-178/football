ARG DOCKER_BASE
FROM $DOCKER_BASE
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get --no-install-recommends install -yq git cmake build-essential \
  libgl1-mesa-dev libsdl2-dev \
  libsdl2-image-dev libsdl2-ttf-dev libsdl2-gfx-dev libboost-all-dev \
  libdirectfb-dev libst-dev mesa-utils xvfb x11vnc \
  python3-pip
# Fix setuptools version to be compatible with gym==0.21.0
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install setuptools==65.5.0 wheel
RUN python3 -m pip install psutil six
COPY . /gfootball
RUN cd /gfootball && python3 -m pip install . --no-cache-dir
WORKDIR '/gfootball'