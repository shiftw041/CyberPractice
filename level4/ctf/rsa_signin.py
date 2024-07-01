from Crypto.Util.number import bytes_to_long

flag = "vmc{***************************}".encode()
m = bytes_to_long(flag)

e = 65537
p = 7861284553623919323985859832007323477428670056827930254749054233285002288342251190742960221895692365421571559655657906508077200676209583363642503410091987
q = 12190036856294802286447270376342375357864587534233715766210874702670724440751066267168907565322961270655972226761426182258587581206888580394726683112820379
n = p * q
print(n)
# 解密c
c = pow(m, e, n)
print('c=', c)
print("p=", p)
print("q=", q)
"""
c = 82847779812851057890043530756832889487859832046106654912667214872414017036311911272053848097280235944007447512360040509400105818809700630697569934731411705662409382305951636397690516111461818016905840116265739235873533920070957680510890443904586797027770509200983712548635748894266511224103615999307792279118
p = 7861284553623919323985859832007323477428670056827930254749054233285002288342251190742960221895692365421571559655657906508077200676209583363642503410091987
q = 12190036856294802286447270376342375357864587534233715766210874702670724440751066267168907565322961270655972226761426182258587581206888580394726683112820379
"""

