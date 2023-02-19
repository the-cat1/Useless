import sys
import time

def main(argv):
    print("-"*10, "完全数查找器", "-"*10)

    # 参数判断
    output = "-output" in argv
    other = "-other" in argv


    # 获取查找的范围
    try:
        srange = int(input("请输入要查找的范围(1~?)：")) + 1
    except ValueError:
        print("请输入正确的数字！")
        return

    goodnums = set()
    mullongnum = set()
    mullonglen = -1
    starttime = time.time()
    
    for x in range(1, srange):
        # 寻找因数
        muls = set()
        for d in range(1, x + 1):
            if x % d == 0:
                muls.add(d)
                muls.add(int(x / d))

        # 判断是否为完全数
        # 等于除了它自身以外的全部因数之和的数，叫完全数。
        if sum(muls) - x == x:
            goodnums.add(x)

        # 输出
        if output:
            p = int(x / srange * 100)
            print(f"    进度：[{'#'*p}{' '*(100-p)}] {p}%", end="\r")

        # 其他统计
        if other:
            mullen = len(muls)
            if mullen > mullonglen:
                mullongnum.clear()
                mullongnum.add(x)
                mullonglen = mullen
            elif mullen == mullonglen:
                mullongnum.add(x)
    if output:
        print(" "*120, end="\r")

    print()
    print("-"*10, "结果--完全数", "-"*10)
    for goodnum in goodnums:
        print(goodnum, end=", ")
    print()

    if other:
        print()
        print("-"*10, "结果----其他", "-"*10)
        print("因数最多的数字：")
        print("    数字：", mullongnum)
        print("    因数长度：", mullonglen)
        print("计算使用时间：", time.time() - starttime)


if __name__ == "__main__":
    main(sys.argv)
