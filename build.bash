#!/bin/bash
set -euo pipefail
IMAGE_SPEC="yuvipanda/k8s-nfs-mounter:$(git log -n1 --pretty=format:%h)"
docker build -t ${IMAGE_SPEC} .
docker push ${IMAGE_SPEC}
echo "Pushed ${IMAGE_SPEC}"