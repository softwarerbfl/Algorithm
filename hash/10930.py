#SHA-256 해시값 출력
from hashlib import sha256
n= str(input())
encoded=n.encode()
result=sha256(encoded).hexdigest()
print(result)