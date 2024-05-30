# 使用官方的Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录
COPY . .

# 安装依赖包
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口5002
EXPOSE 5002

# 运行Flask应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5002", "app:app"]