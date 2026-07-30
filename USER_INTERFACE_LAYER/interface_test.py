import sys

sys.path.insert(
    0,
    r"E:\football_v\USER_INTERFACE_LAYER"
)


from chat_runtime import process



result = process(
    "分析 Manchester City Liverpool"
)


print("==============================")
print("USER INTERFACE TEST")
print("==============================")


print(result)

