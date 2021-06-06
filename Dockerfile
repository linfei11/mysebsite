## 选node作为基础镜像
FROM node:latest
##换源安装vuecli
RUN npm config set registry https://registry.npm.taobao.org 
RUN npm install -g npm
RUN npm install -g @vue/cli
## 创建一个目录
RUN mkdir /code
## 指定工作目录
WORKDIR /code


