FROM node:6.0.0-slim
MAINTAINER pyprism

# Prepare app directory
RUN mkdir -p /src/
ADD . /src/

# Install dependencies
WORKDIR /src/
RUN npm install

# Build the app
# RUN npm build

# Expose the app port
EXPOSE 8000

# Start the app
CMD npm start
