# iDoulist
# 爱豆列
~ idoulist
## 简述
- 我们观察到在豆瓣进行图书豆列管理时的一些问题:
  1. 不能实现在指定豆列中找书,当豆列很长(如开智书单)时尤其麻烦
  2. 无法比较几个豆列是否重叠
  3. 无法导出豆列(及书籍信息)到文件永久保存
- 我们认为这些问题都可以通过人工重复劳动来解决,但繁琐并耗时,不是长久之计.对于开智群友更是时间的巨大浪费.
- 所以idoulist可以来解决豆列的这些问题,把豆瓣的大量书籍信息用得更方便.

## 成员

- [Frank Hu](https://github.com/Frank-the-Obscure), [教程](https://www.gitbook.com/book/frank-the-obscure/pythoncamp0/details)
- [zshaolin](https://github.com/zshaolin), [教程](https://github.com/zshaolin/pythoncamp0)
- [Iris Lee](https://github.com/nicetag), [教程](?)

## 目标
作品功能说明:

- 功能0: 导出豆列内容
    + input: 豆列链接
    + process:
    + output: 豆列中内容(txt, etc) 
      - 加强版可以深度挖取书籍内容页面等, 导出 ISBN, tag 等信息.
- 功能1: 对比两个/多个豆列内容
    + 输入: 两个豆列链接 A B
    + 输出: AB的交/并,(A-B)等
    + 其它
- 功能2: 导入内容到豆列
    - 输入: 功能0导出的数据格式+目标豆列链接
    - 输出: 添加内容后的豆列内容
    - 注解:
      - 原则上可以实现，最坏情况下要模拟重复性的鼠标键盘操作，这个坑比较大。 
      - 稍好情况则是发现豆瓣添加新内容的接口，简化程序输出内容，如果能简化为一个链接即添加，那么输出只要十行代码就可以了。
      - 因此，如何输出，还需要依赖对网站(豆瓣) 架构的理解，可能需要呼叫支援。
      - 不过我对此比较乐观，猜想可以google到类似问题的解决方案。
- 功能3: 豆列内容去重
- 功能4: 豆列内容

## 计划
~ ~~五周~~4周半(=.=)规划, 通过日报持续增补

### Week0
~ 技术验证

- 目标:
    - 完成功能0初探:功能0是本项目核心
- 困难:
    - 技术困难0:
      - 抓取信息到 process 模块
      - 对策:查阅相关库,优先用已有轮子完成
    - 技术困难1:
      - 多页豆列抓取
      - 对策: unknown
    - ...
- 规划:
    - 周日: 过了..
    - 周一: 过了..
    - 周二: 马上也过了..
    - 周三: 用最基本网页测试 input 模块; output 假定已抓好,解决输出到文件.
    - 周四: input 模块用实际单页豆列测试QC; 如未解决全组共同尝试; process 开始
    - 周五: input/process/output 完善
    - 周六: 本周测试总结 QC;确定下周目标是否可以拓展到功能1,2,n...

### Week1
~ 原型开发

- 目标:
    - 完成功能0;
    - 完成功能1, 以及两个功能的共同使用;
    - 发布 MVP(minimal valuable product) v1.0, 功能0/1的最基本版本
- 困难:
    - 技术困难0:...对策...
    - 技术困难1:...对策...
    - ...
- 规划:
    - 周日: 进行..
    - 周一: 进行..
    - ...

### Week2
~ 功能填充

- 目标:
    - 探索功能2(导入到豆列), 周三晚质控决定功能2是否需要调整
    - 完成功能1的一些延伸; 如有余时间, 考虑添加 GUI
    - 发布 MVP(minimal valuable product)更新, 主要包括功能0/1

### Week3
~ 测试调整

- 目标:
    - 根据 week2 结果进行功能2的实现
    - 完成功能0/1的一些延伸; 
    - 初步测试已有功能
    - 考虑直接把某些可用功能整合内置于产品
    - 发布 MVP(minimal valuable product)更新, 主要包括功能0/1, 加入功能2基本版本
    
### Week4
~ 演示筹备

- 目标:
    - 优化各个功能细节, UI 等
    - 进行中等规模产品测试
    - 准备演示

## 资源
- [日报入口](https://github.com/Frank-the-Obscure/iDoulist/wiki/Daily-report)
- [仓库入口](https://github.com/Frank-the-Obscure/iDoulist)
- 参考:
    - [文档链接](https://github.com/Frank-the-Obscure/iDoulist/blob/master/README.md)
    - ....
