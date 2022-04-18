# flask_app

challanges:
- macos compatibility

materials:
https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/
https://phoenixnap.com/kb/install-minikube-on-ubuntu
https://www.youtube.com/watch?v=R8_veQiYBjI&t=2s



minikube , ubuntu 18:
minikube start --extra-config=apiserver.service-node-port-range=1-65535 --driver=docker --alsologtostderr
