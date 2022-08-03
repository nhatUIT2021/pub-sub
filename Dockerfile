
# Install Imagemagick into the container image.
# For more on system packages review the system packages tutorial.
# https://cloud.google.com/run/docs/tutorials/system-packages#dockerfile
RUN set -ex; \
  apt-get -y update; \
  apt-get -y install imagemagick; \
  rm -rf /var/lib/apt/lists/*
