#!/bin/bash
kubectl apply -f ./k8s/resty-deployment.yaml
terraform -chdir=./k8s init
terraform -chdir=./k8s apply -auto-approve
