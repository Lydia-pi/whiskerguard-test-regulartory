from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import time

MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

PROMPT_TEMPLATE = """
你是一个资深软件测试专家。
根据下面的功能需求，帮我拆解出简短的测试用例和对应的 Selenium+Pytest 脚本模板。
需求描述：
\"\"\"
{requirement}
\"\"\"

请输出：
1. 测试用例列表（测试点与预期结果）
2. 对应的 Python 脚本模板
"""

def generate_test_artifacts(requirement_text: str) -> str:
    prompt = PROMPT_TEMPLATE.format(requirement=requirement_text)
    print("🔄 开始生成……")
    start = time.time()
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=256)
    outputs = model.generate(**inputs, max_new_tokens=200)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"✅ 生成完成，用时 {time.time() - start:.1f}s")
    return result

# if __name__ == "__main__":
#     sample_req = "登录页面：正确用户名密码跳转，错误提示出现"
#     print(generate_test_artifacts(sample_req))
if __name__ == "__main__":
    sample_req = "登录页面：正确用户名密码跳转，错误提示出现"
    result = generate_test_artifacts(sample_req)
    # 打印完整 repr，查看它是不是空字符串
    print("🔍 raw result repr:", repr(result))
    print("🔢 result 长度:", len(result))
    print("📄 result 内容:\n", result)
