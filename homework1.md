#梯子：Across The GFW#
* 翻墙:本人使用付费的vpn进行科学上网
* GFW的工作机制：
>dns拦截（但能够通过hosts文件的修改能够破解）<br>
ip拦截（现在使用的技术）<br>

* 如何绕开GFW：由于GFW不屏蔽陌生的第三方地址，所以本质上都是通过中介地址的传输来进行科学上网 
* 代理和实现方法：利用加密代理协议，寻找外网的可用节点，再通过一些技术（各式各样的代理软件）来架起两者间的联系，让资源通过外网机器进入电脑![](https://img-blog.csdnimg.cn/20190103212337264.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2p1aTEyMTMxNA==,size_16,color_FFFFFF,t_70)
* VPN和代理的区别：
>**技术****:**大同小异，都是在您的计算机和Internet之间放置了一个中间人<br>
>**匿名性与安全性****:**主要区别在于VPN需要隧道过程，该过程建立了到您和VPN服务器的直接且不可穿透的连接。代理只是一个开放的端口，你可以连接，没有隧道，也不是不能通过的。代理只是一个可以访问的IP，而vpn需要身份验证，安全性更高。
#搭建基本编程环境
* 二面时由于多语言的使用配置了vscode
![](https://s3.bmp.ovh/imgs/2021/10/a8c276e12213207f.png)
* 命令行格式的git
![](https://s3.bmp.ovh/imgs/2021/10/2eaba6ef8229cb78.png)
* windows terminal及相关 [我看的这篇文章，还不错](https://zhuanlan.zhihu.com/p/272082726)
#git：版本控制工具#
* *如果不借助 git，即没有这一样工具，只使用您常用的即时通信工具来进行代码协作，您认为会遇到哪些困难？*
>不使用git我认为最大的困难是无法追踪版本的变化，从而难以有效的“备份”之前的代码和合并当前的改动和现在的代码。<br>
>同时不使用git很难进行一些项目的研发，无法通过fork来产生衍生的版本，并且需要管理员的权限才能够开通代码的共享，这往往需要高昂的时间成本，而且没有命令行的简洁操作，这是从前的在线聊天软件难以做到的。

* 
