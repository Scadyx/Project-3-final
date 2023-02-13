FROM alpine:3.9

ENV HELM_VERSION v3.11.0

RUN apk --update --no-cache add \
  bash \
  ca-certificates \
  curl \
  jq \
  git \
  openssh-client \
  python3 \
  tar \
  wget \
  openssl

RUN pip3 install --upgrade pip
RUN pip3 install awscli

# Install helm
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 && chmod 700 get_helm.sh && ./get_helm.sh
  

# Install latest kubectl
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl_latest \
  && chmod +x /usr/local/bin/kubectl_latest

WORKDIR /work

CMD ["helm", "version"]
