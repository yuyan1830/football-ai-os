import importlib.util
import sys


# 加入项目根目录
sys.path.insert(
    0,
    r"E:\football_v"
)


adapter_path = r"E:\football_v\12_API_LAYER\ADAPTER\ai_runtime_adapter.py"


spec = importlib.util.spec_from_file_location(
    "ai_runtime_adapter",
    adapter_path
)


adapter = importlib.util.module_from_spec(spec)

sys.modules["ai_runtime_adapter"] = adapter

spec.loader.exec_module(adapter)


result = adapter.run_ai_runtime(
    {
        "home":"Manchester City",
        "away":"Liverpool"
    }
)


print("==============================")
print("AI RUNTIME ADAPTER TEST")
print("==============================")


print(result)

