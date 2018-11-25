# git使用说明

[TOC]



## 常用使用流程

1. 设置ssh: 

   `ssh-keygen -t rsa -C "787560120@qq.com"`

2. github上添加ssh地址：

   将`id_rsa.pub`文件中的内容复制到github ssh设置中的`Key`输入框中

   `Title`输入适当的ssh密匙名称

3. 设置邮件和用户名：

   `git config --global user.name "gengmr"`

   `git config --global user.email "787560120@qq.com"`

4. 初始化仓库

   `git init`

5. 设置.gitignore文件, 防止将无用的文件添加进来



## 常用命令

+ 将文件加入到暂存区：

  `git add a.txt`

+ 将文件放入仓库：

  `git commit`

  `git comit -m 'first add a.txt' `

+ 提交：

  `git push`

+ 从远程仓库中克隆：

  `git clone url`

+ 查看当前状态：

  `git status`

  `git status -s` # 简短信息

+ 查看提交状态：

  `git log`

+ 需要运行大文件：

  安装`git LFS`










