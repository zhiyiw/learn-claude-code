#!/bin/bash
# 启动 LiteLLM 代理，将 Anthropic API 格式请求转发给 LM Studio
#
# 使用前：确认 LM Studio 已启动并加载了 Qwen3.5 27B 模型
# LM Studio 默认地址: http://localhost:1234
#
# 用法：./start_litellm.sh [LM_STUDIO_MODEL_ID]
# 
# LM_STUDIO_MODEL_ID: 在 LM Studio > 已加载模型 里查看的完整模型名
# 例如: qwen3_5-27b-q4_k_m 或 qwen/qwen3.5-27b-instruct

MODEL_ID="${1:-qwen3.5-27b}"
LM_STUDIO_URL="http://localhost:1234/v1"
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
