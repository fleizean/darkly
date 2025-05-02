#!/bin/bash

# Build the Docker image
docker build -t darkly-qemu .

# Run the container with volume mount for the ISO
# Assuming the ISO is in the current directory
docker run -it --rm \
  -v "$(pwd)/Darkly_i386.iso:/qemu/Darkly_i386.iso" \
  -p 8080:8080 \
  darkly-qemu

# After running this, you should be able to access the VM's web server at:
# http://localhost:8080j