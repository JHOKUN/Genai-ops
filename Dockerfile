FROM node:22-alpine
WORKDIR /Genai-ops
COPY ..
RUN yarn install --production
CMD ["node", "./src/index.js"]
