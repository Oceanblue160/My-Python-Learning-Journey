data = input()
n = list(map(int, data.split()))    #将输入的字符串分割成整数列表
m = len(n)                          #用m来表示论文数量
h = 0
n.sort(reverse=True)                #sort函数将n里面的元素从大到小排序
for i in range(m):                  #循环m次（i从0开始，所以第一篇文章也是第0+1篇）
    if n[i] < i + 1:                #如果第(i+1)篇文章的引用次数小于(i+1)，则后面所有文章引用次数都小于(i+1)
        h = i                       #所以结果就是前面i篇引用次数大于i-1的文章。其实是简单的贪心算法。
        break                       #找到答案了，退出循环
print(h)                            #输出答案
