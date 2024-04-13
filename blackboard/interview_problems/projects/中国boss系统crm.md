## 

### 生产日志查询

在Linux环境下，查看文件内容时，很多时候需要查看指定关键字的前后几行，如查看日志文件时，如果日志文件太大，想直接在Linux 终端中查看，可以grep ‘partten’ filename 进行过滤，如果想查看匹配行的前后几行，可通过在grep后面添加参数来实现，具体如下： **grep -A 5**

[Linux grep根据关键字匹配前后几行 - HaimaBlog - 博客园 (cnblogs.com)](https://www.cnblogs.com/haima/p/15161542.html#:~:text=%E5%9C%A8Linux%E7%8E%AF%E5%A2%83%E4%B8%8B%EF%BC%8C%E6%9F%A5%E7%9C%8B%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9%E6%97%B6%EF%BC%8C%E5%BE%88%E5%A4%9A%E6%97%B6%E5%80%99%E9%9C%80%E8%A6%81%E6%9F%A5%E7%9C%8B%E6%8C%87%E5%AE%9A%E5%85%B3%E9%94%AE%E5%AD%97%E7%9A%84%E5%89%8D%E5%90%8E%E5%87%A0%E8%A1%8C%EF%BC%8C%E5%A6%82%E6%9F%A5%E7%9C%8B%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6%E6%97%B6%EF%BC%8C%E5%A6%82%E6%9E%9C%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6%E5%A4%AA%E5%A4%A7%EF%BC%8C%E6%83%B3%E7%9B%B4%E6%8E%A5%E5%9C%A8Linux%20%E7%BB%88%E7%AB%AF%E4%B8%AD%E6%9F%A5%E7%9C%8B%EF%BC%8C%E5%8F%AF%E4%BB%A5grep%20%E2%80%98partten%E2%80%99%20filename,%E8%BF%9B%E8%A1%8C%E8%BF%87%E6%BB%A4%EF%BC%8C%E5%A6%82%E6%9E%9C%E6%83%B3%E6%9F%A5%E7%9C%8B%E5%8C%B9%E9%85%8D%E8%A1%8C%E7%9A%84%E5%89%8D%E5%90%8E%E5%87%A0%E8%A1%8C%EF%BC%8C%E5%8F%AF%E9%80%9A%E8%BF%87%E5%9C%A8grep%E5%90%8E%E9%9D%A2%E6%B7%BB%E5%8A%A0%E5%8F%82%E6%95%B0%E6%9D%A5%E5%AE%9E%E7%8E%B0%EF%BC%8C%E5%85%B7%E4%BD%93%E5%A6%82%E4%B8%8B%EF%BC%9A%20grep%20-A%205)

## 携转中心

关于数据库请求方案 qps 的优化

一开始我是想着把全部数据都 load 到 redis 中

然后查询分页

后来发现 redis 不适合复杂的查询聚合操作

于是想选择 

[elasticsearch(ES)在SpringBoot中的复杂查询（多条件分页查询以及聚合查询)](https://blog.csdn.net/u012809308/article/details/106752955)

但是临近上线也不可能直接上线一套新的组件

所以就直接加载到 JVM , 也就是使用 hashmap

[不要太离谱，Java面试官居然问我了解QPS、TPS、RT、吞吐量、这些高并发性能指标吗？_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Su4y1R7rV/?spm_id_from=..search-card.all.click&vd_source=eabc2c22ae7849c2c4f31815da49f209)

[(49 封私信 / 80 条消息) 如何清楚易懂的解释“UV和PV＂的定义？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/20448467#:~:text=PV%E5%85%A8%E7%A7%B0Page%20View%EF%BC%8C%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91%E5%8D%B3%20%E9%A1%B5%E9%9D%A2%E6%B5%8F%E8%A7%88%20%E3%80%82,%E5%85%B6%E5%85%B7%E4%BD%93%E7%9A%84%E5%BA%A6%E9%87%8F%E6%96%B9%E6%B3%95%E6%98%AF%E4%BB%8E%E6%B5%8F%E8%A7%88%E5%99%A8%E5%8F%91%E5%87%BA%E4%B8%80%E4%B8%AA%E5%AF%B9%20%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8%20%E7%9A%84%E8%AF%B7%E6%B1%82%EF%BC%88Request%EF%BC%89%EF%BC%8C%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%8E%A5%E5%88%B0%E8%AF%A5%E8%AF%B7%E6%B1%82%E5%90%8E%EF%BC%8C%E4%BC%9A%E5%B0%86%E8%AF%B7%E6%B1%82%E5%AF%B9%E5%BA%94%E7%9A%84%E7%BD%91%E9%A1%B5%EF%BC%88Page%EF%BC%89%E5%8F%91%E9%80%81%E7%BB%99%E6%B5%8F%E8%A7%88%E5%99%A8%EF%BC%8C%E4%BB%8E%E8%80%8C%E4%BA%A7%E7%94%9F%E4%B8%80%E4%B8%AAPV%E3%80%82%20%E5%8F%AA%E8%A6%81%E6%98%AF%E8%AF%B7%E6%B1%82%E5%8F%91%E9%80%81%E7%BB%99%E4%BA%86%E6%B5%8F%E8%A7%88%E5%99%A8%EF%BC%8C%E6%97%A0%E8%AE%BA%E9%A1%B5%E9%9D%A2%E6%98%AF%E5%90%A6%E5%AE%8C%E5%85%A8%E6%89%93%E5%BC%80%EF%BC%88%E4%B8%8B%E8%BD%BD%E5%AE%8C%E6%88%90%EF%BC%89%EF%BC%8C%E9%83%BD%E8%AE%A1%E4%B8%BA1%E4%B8%AAPV%E3%80%82)

**UV（Unique visitor）**  
是指通过互联网访问、浏览这个网页的自然人。访问您网站的一台电脑客户端为一个访客。00:00-24:00内相同的客户端只被计算一次。

一天内同个访客多次访问仅计算一个UV。

**IP（Internet Protocol）**  
独立IP是指访问过某站点的IP总数，以用户的IP地址作为统计依据。00:00-24:00内相同IP地址之被计算一次。

**UV与IP区别：**  
如：你和你的家人用各自的账号在同一台电脑上登录新浪微博，则IP数+1，UV数+2。由于使用的是同一台电脑，所以IP不变，但使用的不同账号，所以UV+2

**PV（Page View）**  
即页面浏览量或点击量，用户每1次对网站中的每个网页访问均被记录1个PV。用户对同一页面的多次访问，访问量累计，用以衡量网站用户访问的网页数量。

**VV（Visit View）**  
用以统计所有访客1天内访问网站的次数。当访客完成所有浏览并最终关掉该网站的所有页面时便完成了一次访问，同一访客1天内可能有多次访问行为，访问次数累计。

**PV与VV区别：**  
如：你今天10点钟打开了百度，访问了它的三个页面；11点钟又打开了百度，访问了它的两个页面，则PV数+5，VV数+2.  
PV是指页面的浏览次数，VV是指你访问网站的次数。

二分查找

号段表

开始号段结束号段

treeset [使用TreeMap - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1252599548343744/1265117109276544) 

开始字段-结束字段

有号段的话就使用这个查询条件进行二分查找

没有就进行全局扫描了

二分查找

```java
    /**
     * 不使用递归的二分查找
     *title:commonBinarySearch
     *@param arr
     *@param key
     *@return 关键字位置
     */
    public static int commonBinarySearch(int[] arr,int key){
        int low = 0;
        int high = arr.length - 1;
        int middle = 0;            //定义middle

        if(key < arr[low] || key > arr[high] || low > high){
            return -1;                
        }

        while(low <= high){
            middle = (low + high) / 2;
            if(arr[middle] > key){
                //比关键字大则关键字在左区域
                high = middle - 1;
            }else if(arr[middle] < key){
                //比关键字小则关键字在右区域
                low = middle + 1;
            }else{
                return middle;
            }
        }

        return -1;        //最后仍然没有找到，则返回-1
    }
```

[java实现二分查找-两种方式_二分法的实现-CSDN博客](https://blog.csdn.net/maoyuanming0806/article/details/78176957)

## java 化

#### C++ 转 java

[使用 AI 将 C++ 转换为 Java (codeporting.app)](https://products.codeporting.app/zh/convert/ai/cpp-to-java#:~:text=%E4%BD%BF%E7%94%A8%20AI%20%E5%B0%86%20C%2B%2B%20%E8%BD%AC%E6%8D%A2%E4%B8%BA%20Java%20%E4%BB%8E%20C%2B%2B,C%2B%2B%20%E4%BB%A3%E7%A0%81%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%AD%89%E6%95%88%E7%9A%84%20Java%20%E4%BB%A3%E7%A0%81%EF%BC%8C%E4%BB%8E%E8%80%8C%E4%BF%83%E8%BF%9B%E4%BB%A3%E7%A0%81%E7%9A%84%E9%87%8D%E7%94%A8%E5%92%8C%E4%B8%8E%20Java%20%E7%8E%AF%E5%A2%83%E7%9A%84%E5%85%BC%E5%AE%B9%E6%80%A7%E3%80%82%20%E6%AD%A5%E9%AA%A4%E5%8C%85%E6%8B%AC%E8%A7%A3%E6%9E%90%E3%80%81AST%20%E8%BD%AC%E6%8D%A2%E3%80%81%E7%B1%BB%E5%9E%8B%E6%8E%A8%E6%96%AD%E3%80%81%E4%BB%A3%E7%A0%81%E7%94%9F%E6%88%90%E3%80%81%E5%A4%84%E7%90%86%E8%AF%AD%E8%A8%80%E5%B7%AE%E5%BC%82%E5%92%8C%E5%90%8E%E5%A4%84%E7%90%86)

提高效率

- 去掉 gc 相关的操作

- 指针相关的, 如果是 char* 会替换成 String, 如果是其他对象类型会直接替换成对应的对象

#### 定时任务

elastic-job 与 quartz 区别[详解当当网的分布式作业框架elastic-job_语言 & 开发_张亮_InfoQ精选文章](https://www.infoq.cn/article/dangdang-distributed-work-framework-elastic-job)

[【深入解析】定时任务：quartz、elastic-job和xxl-job的分析对比！_知其然亦知其所以然的技术博客_51CTO博客](https://blog.51cto.com/u_16237826/7915225#:~:text=%E5%A6%82%E6%9E%9C%E9%A1%B9%E7%9B%AE%E5%AF%B9%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%8A%9F%E8%83%BD%E9%9C%80%E6%B1%82%E6%AF%94%E8%BE%83%E5%A4%8D%E6%9D%82%EF%BC%8C%E5%B9%B6%E4%B8%94%E9%9C%80%E8%A6%81%E4%B8%B0%E5%AF%8C%E7%9A%84%E8%B0%83%E5%BA%A6%E6%A8%A1%E5%BC%8F%E5%92%8C%E5%BC%BA%E5%A4%A7%E7%9A%84%E5%8F%AF%E6%89%A9%E5%B1%95%E6%80%A7%EF%BC%8C%E5%8F%AF%E4%BB%A5%E9%80%89%E6%8B%A9Quartz%E4%BD%9C%E4%B8%BA%E4%B8%BB%E8%A6%81%E7%9A%84%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E6%A1%86%E6%9E%B6%E3%80%82,%E5%A6%82%E6%9E%9C%E9%A1%B9%E7%9B%AE%E6%B3%A8%E9%87%8D%E8%BD%BB%E9%87%8F%E7%BA%A7%E5%92%8C%E5%8F%AF%E6%89%A9%E5%B1%95%E6%80%A7%EF%BC%8C%E4%B8%94%E7%A8%B3%E5%AE%9A%E6%80%A7%E8%A6%81%E6%B1%82%E8%BE%83%E9%AB%98%EF%BC%8C%E5%8F%AF%E4%BB%A5%E9%80%89%E6%8B%A9Elastic-job%E3%80%82%20%E4%BD%86%E9%9C%80%E8%A6%81%E6%B3%A8%E6%84%8FZookeeper%E7%9A%84%E5%BC%95%E5%85%A5%E5%8F%AF%E8%83%BD%E4%BC%9A%E5%A2%9E%E5%8A%A0%E9%A2%9D%E5%A4%96%E7%9A%84%E5%A4%8D%E6%9D%82%E6%80%A7%E5%92%8C%E7%BB%B4%E6%8A%A4%E6%88%90%E6%9C%AC%E3%80%82)

[定时任务框架：quartz、elastic-job和xxl-job的分析对比。_quartz和xxl-job-CSDN博客](https://blog.csdn.net/en_joker/article/details/104407313)

quartz 可以分布式集群部署, 但是更注重任务

elastic-job 更注重数据, 分片来完成任务
