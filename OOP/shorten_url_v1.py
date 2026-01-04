import hashlib
import string

BASE62 = string.digits + string.ascii_uppercase + string.ascii_lowercase

def base62_encode(num: int) -> str:
    if num == 0:
        return BASE62[0]
    res = []
    while num > 0:
        num, rem = divmod(num, 62)
        res.append(BASE62[rem])
    return ''.join(reversed(res))

def hash_url(url: str, length: int = 8) -> str:
    # 使用 MD5 生成 hash
    md5_hash = hashlib.md5(url.encode()).hexdigest()
    # 取前 8 個 hex 字元 -> 32 bit
    num = int(md5_hash[:8], 16)
    # Base62 編碼
    short_code = base62_encode(num)
    # 取前 length 個字符
    return short_code[:length]

# 範例
url = "https://example.com/articles/12345"
short_code = hash_url(url)
print("短碼:", short_code)
