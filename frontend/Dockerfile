FROM node:22.6-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install --production

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]