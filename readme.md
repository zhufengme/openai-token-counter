# OpenAI Token Counter

`openai-token-counter` 是一个基于Flask的RESTful API，用于计算给定字符串在不同OpenAI模型中消耗的token数量。这个项目使用 `tiktoken` 库进行token计数，并通过Docker进行容器化。

## 项目简介

这个API接收一个包含多个模型名称和一段字符串的请求，并返回每个模型消耗的token数量。

## 功能特性

- 计算多个OpenAI模型的token数量
- 通过RESTful API提供服务
- 使用Docker进行容器化，便于部署

## 安装与运行

### 从Docker Hub拉取并运行

你可以直接从Docker Hub拉取并运行已经构建好的镜像：

```bash
docker run -d -p 5002:5002 --name openai-token-counter --restart=always andiezhu/openai-token-counter
```

### 构建本地Docker镜像

1. 克隆项目：

    ```bash
    git clone https://github.com/zhufengme/openai-token-counter.git
    cd openai-token-counter
    ```

2. 构建Docker镜像：

    ```bash
    docker build -t openai-token-counter .
    ```

3. 运行Docker容器：

    ```bash
    docker run -d -p 5002:5002 openai-token-counter
    ```

## 使用方法

你可以使用 `curl` 或Postman等工具发送POST请求到API。

### 示例请求

```bash
curl -X POST http://127.0.0.1:5002/ -H "Content-Type: application/json" -d '{"models": "gpt-3.5-turbo, gpt-4o", "text": "Hello, world!"}'
```

### 示例响应

```json
{
    "gpt-3.5-turbo": 3,
    "gpt-4o": 4
}
```

## API说明

### POST /

计算给定字符串在不同模型中消耗的token数量。

#### 请求体

- `models` (字符串): 以逗号分隔的模型名称列表。
- `text` (字符串): 要计算token数量的字符串。

#### 响应

- 成功: 返回每个模型消耗的token数量。
- 失败: 返回错误信息。

#### 示例

请求体:

```json
{
    "models": "gpt-3.5-turbo, gpt-4o",
    "text": "Hello, world!"
}
```

响应体:

```json
{
    "gpt-3.5-turbo": 3,
    "gpt-4o": 4
}
```
