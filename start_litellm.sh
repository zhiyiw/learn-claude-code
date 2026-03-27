#!/bin/bash
# 启动 LiteLLM 代理，将 Anthropic API 格式请求转发给 LM Studio
#
# 用法：./start_litellm.sh [MODEL_ID] [LM_STUDIO_URL]
#
# MODEL_ID:      LM Studio 中加载的模型名（默认: qwen3.5-27b）
# LM_STUDIO_URL: LM Studio 的地址（默认: http://localhost:1234/v1）
#
# 示例:
#   本地:   ./start_litellm.sh
#   远程PC: ./start_litellm.sh qwen/qwen3.5-35b-a3b http://100.115.246.121:1234/v1

MODEL_ID="${1:-qwen/qwen3.5-35b-a3b}"
LM_STUDIO_URL="${2:-http://100.115.246.121:1234/v1}"
# 本地备用: ./start_litellm.sh qwen3.5-27b http://localhost:1234/v1
LITELLM_PORT=4000

echo "==================================="
echo "  LiteLLM 代理启动"
echo "  LM Studio 地址: $LM_STUDIO_URL"
echo "  模型: $MODEL_ID"
echo "  代理监听: http://localhost:$LITELLM_PORT"
echo "==================================="
echo ""
echo "⚠️  请先在 LM Studio 中确认模型已加载且服务已启动"
echo "⚠️  如果模型名不对，请运行: curl http://localhost:1234/v1/models"
echo ""

OPENAI_API_KEY="lm-studio" .venv/bin/litellm \
  --model "openai/$MODEL_ID" \
  --api_base "$LM_STUDIO_URL" \
  --port $LITELLM_PORT
