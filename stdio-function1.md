# stdio - function 1


- UI: 
  - i: 用户的命令行输入两个 url 给出适当的提示 如:`http://www.douban.com/doulist/38390646/, http://www.douban.com/doulist/4184864/`
  - p: 在用户回车确认输入之后, 新建两个字符串变量 `input_doulist1 = http://www.douban.com/doulist/38390646/, input_doulist2 = http://www.douban.com/doulist/4184864/`
  - o1: `input_doulist1/2`
  - o2: 程序运行后, 提示输出为 `iDoulist.md`/输出到命令行
  - 高阶版: 图形界面的输入框, 用按钮来完成确认输入功能
- input: 
  - i: 两个合法豆瓣豆列 url `input_doulist1/2`
  - p: **抓取**豆列中的书籍的 urls 
  - o: 输出书籍 urls 至两个列表对象 `list1/2`
- process: 
  - i: `list1/2`
  - p: 新建一个/多个列表对象 `combine_list = list1 + list2`
  - o: `combine_list` 
  - 高阶版: 可输出两个列表的交/并/差, 实现去重
- output:
  - i: `combine_list`等
  - p: 输出到命令行和/或本地文件: `iDoulist.md/txt`
  - o: `iDoulist.md` 可实现为`combine_list, cross_list, list1 - list2, list2 - list1`