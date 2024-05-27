from flask import Flask, request, jsonify
import tiktoken
import logging

app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def count_tokens(model_name, text):
    try:
        # 使用tiktoken获取模型的编码器
        encoding = tiktoken.encoding_for_model(model_name)
        # 将文本编码为tokens
        tokens = encoding.encode(text)
        return len(tokens)
    except Exception as e:
        logger.error(f"Error counting tokens for model {model_name}: {e}")
        return str(e)

@app.route('/', methods=['POST'])
def token_count():
    try:
        data = request.json
        if not data:
            raise ValueError("Invalid JSON format.")
        
        models = data.get('models')
        text = data.get('text')
        
        if not models or not text:
            raise ValueError("Please provide both 'models' and 'text' fields.")
        
        if not isinstance(models, str) or not isinstance(text, str):
            raise ValueError("'models' and 'text' fields must be strings.")
        
        if not text.strip():
            raise ValueError("The 'text' field cannot be empty or whitespace.")
        
        model_list = models.split(',')
        result = {}
        
        for model in model_list:
            model = model.strip()
            result[model] = count_tokens(model, text)
        
        return jsonify(result)
    
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)