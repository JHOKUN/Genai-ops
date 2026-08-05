FROM postgres:18
WORKDIR /Genai-ops/
RUN apt-get update && apt-get install -y curl nodejs npm && npm install -g yarn
WORKDIR /Genai-ops
COPY . .
RUN yarn install --production
