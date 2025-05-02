FROM debian:bullseye-slim

# Install QEMU and required dependencies
RUN apt-get update && apt-get install -y \
    qemu-system-x86 \
    qemu-utils \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create directory for ISO
WORKDIR /qemu

# Copy only if you have the ISO locally, otherwise you'll need to mount it
# COPY Darkly_i386.iso /qemu/

# Expose port 8080 which will be mapped to port 80 of the VM
EXPOSE 8080

# Command to run QEMU with proper networking
CMD ["qemu-system-x86_64", "-nographic", "-drive", "file=/qemu/Darkly_i386.iso,format=raw", "-m", "4G", "-nic", "user,hostfwd=tcp::8080-:80"]