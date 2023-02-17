# ChatGptApi
通过api操作chatgpt网页版的功能，chatgpt地址： https://chat.openai.com/chat

注：chromedrive需要配置为全局变量

​		chatgpt需要提前打开并登录

| 功能                   | url                | 请求方式 | json                   |
| ---------------------- | ------------------ | -------- | ---------------------- |
| 发送消息               | /api/message       | post     | {"message":""}         |
| 获取当前聊天的全部回复 | /api/getallreplies | get      |                        |
| 获取正在回复的消息     | /api/repling       | get      |                        |
| 获取最后一条回复       | /api/getlastreply  | get      |                        |
| 获取获取全部聊天记录   | /api/getallchat    | get      |                        |
| 选这聊天记录           | /api/choosechat    | post     | {"ref":聊天记录的编号} |
| 删除当前聊天记录       | /api/deletechat    | get      |                        |
| 当前聊天记录命名       | /api/renamechat    | post     | {"name":""}            |
| 打开新的聊天记录       | /api/newchat       | get      |                        |
| 刷新网页               | /api/reload        | get      |                        |

使用方法：

需要chrome和chromedrive

chromedrive下载地址： https://chromedriver.storage.googleapis.com/index.html

chrome配置：

1. 创建新的快捷方式

2. 鼠标右键点开快捷方式的属性

3. 将目标的内容修改这串字符:

   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\Public\ChromeData"

![](\image\chrome.png)

启动：

- 可以直接运行已经打包好的代码，打包好的文件路径\ChatGptAPI3.0\ChatGptApi\dist\__init__，双击运行 \_\_init\_\_.exe

- 也可以编译源代码自己调试



具体运行效果:

出现一下界面说明你运行成功了

![](\image\效果图1.png)

测试接口

1.创建新的聊天记录

![](\image\效果图2.png)

2.发送一条消息

![](\image\效果图4.png)

3.接收最后一条回复

![](\image\效果图5.png)

4.chatgpt页面结果

![](\image\效果图6.png)



