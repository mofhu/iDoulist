# iDoulist
# 爱豆列
~ iDoulist
## 简述
- 我们观察到在豆瓣进行图书豆列管理时的一些问题:
  1. 不能实现在指定豆列中找书,当豆列很长(如开智书单)时尤其麻烦
  2. 无法比较几个豆列是否重叠
  3. 无法导出豆列(及书籍信息)到文件永久保存
- 我们认为这些问题都可以通过人工重复劳动来解决,但繁琐并耗时,不是长久之计.对于开智群友更是时间的巨大浪费.
- 所以iDoulist可以来解决豆列的这些问题,把豆瓣的大量书籍信息用得更方便.

## 成员
- [Frank Hu](https://github.com/Frank-the-Obscure), [教程](https://www.gitbook.com/book/frank-the-obscure/pythoncamp0/details)
- [zshaolin](https://github.com/zshaolin), [教程](https://github.com/zshaolin/pythoncamp0)
- [Iris Lee](https://github.com/nicetag), [教程?](?)
- [huhu zhu](https://github.com/huhu8), [教程](https://github.com/huhu8/pythoncamp0)

## 作品功能说明:
- 功能0: 导出豆列内容
    - input: 豆列链接
    - output: 豆列中内容(.md/CLI feedback) 
- 功能1: 对比两个/多个豆列内容
    - 应用场景: `开智群的哪些书我没有看过?`
    - 输入: 两个豆列链接 A B
    - 输出: AB的交/并,(A-B)等
- 功能2: 导入内容到豆列
    - 输入: 功能0导出的数据格式 + 目标豆列链接
    - 输出: 添加内容后的豆列内容
- 功能n ...

## 如何安装使用: 
- 在 OS X 10.10.4 测试
- Python 2.7.9
- 下载整个文件夹后, 运行 function0_MVP.py 即可实现功能0