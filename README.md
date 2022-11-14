# 一个将txt文件转换为日程的简单脚本

### v 0.0.1

​	对于读取的txt文件，每一件单独的日程应该按照：

```
{{:日程名称;:时间(如202211128.40~9.50);:描述;}}
```

​	的格式列出来，两件日程间可用任意字符分隔，如：

```
{{...}},{{...}},{{...}}
或
{{...}}\{{...}}\{{...}}\
或
{{...}} {{...}} {{...}}
```

​	需要注意的是日程的属性必须以英文的冒号为起始，以英文的分号为结束，在当前版本仅支持名称、时间和描述三个属性。

#### 名称

​	可以是任意语言或任意字符，对最终的结果不会产生影响。

#### 时间

​	在当前版本支持全数字的八位日期+起始时间+'~'或'-'（英文字符）+截止时间的时间格式。

​	也支持明天/后天+时间的自然语言格式，如：

```
{{:...;:2022111111.11-12.28;:...;}}
表示一件2022年11月11日11点11分开始的截止到12.28分的事件
{{:...;:明天8.30~10.30;:...;}}
表示一件从明天早上八点半开始到十点半截止的事件
```

​	时间的输入必须为（24时制）小时.分钟，如`10.00, 18.00`等。

#### 描述

​	同名称的使用。