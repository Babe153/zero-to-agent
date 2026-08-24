from __future__ import annotations

def get_weather(city: str) -> str:
    weather = {
        "Beijing": "晴天，25度",
        "Shanghai": "多云，28度",
        "Hangzhou": "小雨，22度",
    }
    return f"{city} 的天气是：{weather.get(city, '未知天气')}"

