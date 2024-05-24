FROM node:21.7.3

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

EXPOSE 3000
#CMD [ "node", "--snapshot-blob", "snapshot.blob", "index.js" ]
CMD ["bash"]

