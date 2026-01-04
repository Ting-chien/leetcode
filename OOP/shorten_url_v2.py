import string

# Base62 字符集
BASE62 = string.digits + string.ascii_uppercase + string.ascii_lowercase

def encode_base62(num: int) -> str:
    """將整數轉成 Base62 字串"""
    if num == 0:
        return BASE62[0]
    result = []
    while num > 0:
        num, rem = divmod(num, 62)
        result.append(BASE62[rem])
    return ''.join(reversed(result))

def decode_base62(s: str) -> int:
    """將 Base62 字串轉回整數"""
    num = 0
    for char in s:
        num = num * 62 + BASE62.index(char)
    return num

# 模擬短網址
def shorten_url(long_url: str, id: int) -> str:
    short_code = encode_base62(id)
    return f"https://short.ly/{short_code}"

# 範例
long_url = "https://example.com/articles/12345"
url_id = 125  # 假設這個 URL 的唯一數字 ID
short_url = shorten_url(long_url, url_id)

print("短網址:", short_url)
print("解碼回原始 ID:", decode_base62(short_url.split('/')[-1]))
