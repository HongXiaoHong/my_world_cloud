## [阿里二面：如何快速定位线上OOM？上来就直接被问麻了。。_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1iH4y1o7PK/?spm_id_from=333.788&vd_source=eabc2c22ae7849c2c4f31815da49f209)

因为容量不足的关系, 无法及时释放资源

### 可能的原因包括

1. java 配置的内存太小, 无法容纳对应的程序
   
   只需要使用 jmap 指令查看对应的 jvm 的配置, 提高内存的容量

2. 一次性加载到 jvm 中的内容太大
   
   例如将数据库中的数据一次性 load 到我们的内存中

3. 开启过多的线程没有释放
   
   使用线程池充分利用线程, 配置对应的任务处理策略



### 如何定位

对于 oom 错误, 我们最好是通过 dump 文件 ＋ jvisualvm 分析我们的dump 文件进行解析

当然只是 java 配置的问题倒是很好解决, 只需要在用 java 启动 jar/war 程序的时候, 加大我们的内存, 一般是增加 堆最大以及初始化大小

dump 文件需要我们配置 java 启动的命令, 需要加上 dump...onMemoryError dump...Path

来配置 oom 错误的时候以及在 dump 存放路径


