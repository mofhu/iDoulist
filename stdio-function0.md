# stdio - function 0



- UI: 
  - i: `http://www.douban.com/doulist/38390646/` 
  - o1: `input_doulist`
  - o2: 程序运行后, 提示输出为 `iDoulist.md`/输出到命令行
  - 高阶版: 
    - 检测豆列是否为合法输入
    - 图形界面的输入框, 用按钮来完成确认输入功能
      - 使用什么图形库?可能是坑
- input: 
  - i: `input_doulist = http://www.douban.com/doulist/38390646/`
  - p: **抓取**豆列中的书籍的 urls `http://book.douban.com/subject/1139336/, http://book.douban.com/subject/25724948/`
  - o: `list = ['http://www.douban.com/doulist/38390646/', 'http://book.douban.com/subject/25724948/']`
  - 预计这个坑最大, 最好使用一个体量适合 Frank Hu 42分钟水平的微型抓取库
  - 高阶版: 含多页内容的单个豆列 特殊豆列:已读/想读
- process: 
  - i: `list = ['http://www.douban.com/doulist/38390646/', 'http://book.douban.com/subject/25724948/']`
  - p: 新建一个列表对象 `new_list = list`
  - o: `new_list = ['http://www.douban.com/doulist/38390646/', 'http://book.douban.com/subject/25724948/']`
- output:
  - i: `new_list = ['http://www.douban.com/doulist/38390646/', 'http://book.douban.com/subject/25724948/']`
  - p: 输出到命令行和/或本地文件: `iDoulist.md/txt`
  - o: `iDoulist.md` 可实现为`http://www.douban.com/doulist/38390646/, http://book.douban.com/subject/25724948/`
  - 天才版: `输出为豆列`