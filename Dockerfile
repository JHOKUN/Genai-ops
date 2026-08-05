FROM postgres:18
WORKDIR /Genai-ops/
COPY . .
RUN npm install --only=production
CMD ["", ""]
