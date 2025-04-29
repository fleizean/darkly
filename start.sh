#!/bin/bash

if ! command -v qemu-system-x86_64 &> /dev/null
then
    echo "QEMU bulunamadı, yükleniyor..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null
        then
            echo "Homebrew bulunamadı, lütfen Homebrew'u yükleyin ve tekrar deneyin."
            exit 1
        fi
        brew install qemu
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update
        sudo apt-get install -y qemu
    else
        echo "Bu işletim sistemi desteklenmiyor."
        exit 1
    fi
fi

qemu-system-x86_64 -drive file=Darkly_i386.iso,format=raw -m 4G -nic hostfwd=tcp:127.0.0.1:8080-:80
