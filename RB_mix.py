import math
import random

from pycsp3 import *

k1, k2, n, alpha, r, p, l1, l2 = data
k = [k1, k2]
alpha = float(alpha)
r = float(r)
p = float(p)
l1 = float(l1)
l2 = float(l2)
l = [l1, l2]
m = r * n * math.log(n)  # 随机可重复挑选的约束总数
d = round(n ** alpha)  # 变量定义域的上限
m_list = [math.ceil(i * m) for i in l]  # 分组约束
q_list = [round(p * d ** ki) for ki in k]  # 分组不相容赋值集合的个数

x_sub = range(n)  # 变量角标
var_support = [list(product(range(1, d + 1), repeat=ki)) for ki in k]  # 约束变量可取值组合全排列
constraint_var_sub_group = list()  # 组成约束的变量角标集合
constraint_var_no_support_group = list()  # 其不协调值

for i, mi in enumerate(m_list):
    for constraint_n in range(mi):
        tmp_con_x = random.sample(x_sub, k[i])  # 随机抽取约束的变量组合
        constraint_var_sub_group.append(tmp_con_x)
        # 随机抽取约束的不协调组合
        tmp_con_x_no_support = random.sample(var_support[i], q_list[i])
        constraint_var_no_support_group.append(tmp_con_x_no_support)

x = VarArray(size=n, dom=range(1, d + 1))

satisfy(
    [x[con_var_i] for con_var_i in con_var] not in constraint_var_no_support_group[i] for i, con_var in
    enumerate(constraint_var_sub_group)
)
