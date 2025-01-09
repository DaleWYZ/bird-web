# 基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

# 复制应用程序文件
COPY . .

# 创建必要的目录
RUN mkdir -p static/images

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["python", "app.py"] 