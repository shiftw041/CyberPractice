import gmpy2
import random
import hashlib
from ecdsa import ecdsa as ec

p = 6277101735386680763835789423207666416083908700390324961279
q = 6277101735386680763835789423176059013767194773182842284081
str1 = "3209671899590734816296511360854418081217797094395123781087, 2517488718134876409697521369714915389507516913171950578408, 114621686706028309788454858023640433236"
str2 = "3209671899590734816296511360854418081217797094395123781087, 464026447385423297425255249909152738649950317614934894659, 30274709465434473722327453979837508451"
msg = "23:04:48:get_flag"
r1, s1, m1 = (int(k) for k in str1.split(", "))
r2, s2, m2 = (int(k) for k in str2.split(", "))
r = r1
ds = s2 - s1
dm = m2 - m1
# 使用扩展欧几里得算法求模逆
k = gmpy2.mul(dm, gmpy2.invert(ds, q))
k = gmpy2.f_mod(k, q)
# 计算秘密数 X
tmp = gmpy2.mul(k, s1) - m1
x = tmp * gmpy2.invert(r, q)
X = gmpy2.f_mod(x, q)
# 使用随机数生成器
RNG = random.Random()
# 使用192位的椭圆曲线参数
g = ec.generator_192  
N = g.order()
# 私钥和公钥
secret = X
PUBKEY = ec.Public_key(g, g * secret)
PRIVKEY = ec.Private_key(PUBKEY, secret)
# 计算哈希值
hash = int(hashlib.md5(msg.encode()).hexdigest(), 16)
# 生成随机数 nonce
nonce = RNG.randrange(1, N)
# 签名
signature = PRIVKEY.sign(hash, nonce)
print(f"{signature.r}, {signature.s}")


