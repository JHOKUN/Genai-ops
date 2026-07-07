FROM postgres:18
WORKDIR /Genai-ops/
COPY . .
RUN yarn install --production
CMD ["", ""]
