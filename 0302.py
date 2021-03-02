
import jieba
str = "道路千万条,安全第一条;行车不规范,亲人两行泪"
print("原句:\n" + str)

seg_list = jieba.cut(str)
print("分词:\n" +"/".join(seg_list))