from __future__ import annotations

def get_weather(city: str) -> str:
    """假工具:获取指定城市的天气"""
    weather = {
        "Beijing": "晴天，25度",
        "Shanghai": "多云，28度",
        "Hangzhou": "小雨，22度",
    }
    return f"{city} 的天气是：{weather.get(city, '未知天气')}"

def parse_model_output(text:str) -> tuple[str, dict]:
    """解析模型输出"""
    tool_name, city = text.split(":", maxsplit=1)
    """text.split(":", maxsplit=1)将字符串以：分隔成两部分，第一部分是工具名称，第二部分是城市名称。分别赋值给tool_name和city变量。"""
    """然后使用strip()方法去除两部分的前后空格，并返回一个元组，包含工具名称和一个字典，字典中包含城市名称。"""
    return tool_name.strip(), {"city": city.strip()}

def main() -> None:
    """主函数"""
    print("=== 01. 字符串协议版 ToolCall ===")

    model_output = "get_weather: Beijing"

    print("\n假设模型输出：")
    print(model_output)

    tool_name, tool_args = parse_model_output(model_output)

    print("\n解析后的工具请求：")
    print(f"工具名称 = {tool_name}")
    print(f"工具参数 = {tool_args}")

    if tool_name == "get_weather":
        result = get_weather(**tool_args)
    # **tool_args是将字典tool_args中的键值对作为关键字参数传递给get_weather函数。
    # 假设tool_args = {"city": "Beijing"}，那么get_weather(**tool_args)等价于get_weather(city="Beijing")。
    else:
        result = f"未知工具：{tool_name}"

    print("\n工具调用结果：")
    print(result)

if __name__ == "__main__":
    main()