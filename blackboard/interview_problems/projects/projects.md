# 项目

## 克拉玛依水厂项目

系统架构:

参考 [北控水务BECloudTM智慧水务云平台 (aii-alliance.org)](https://www.aii-alliance.org/resource/c334/n1385.html)

![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/msedge_taqRI9ORkc.png)

### 大屏

水务大屏参考

![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/%25E6%2599%25BA%25E6%2585%25A7%25E6%25B0%25B4%25E5%258A%25A1%25E7%25AE%25A1%25E7%2590%2586%25E5%25A4%25A7%25E5%25B1%258F-4.gif)

经营大屏参考

![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/%25E6%25B0%25B4%25E5%258E%2582%25E7%25BB%258F%25E8%2590%25A5%25E7%25AE%25A1%25E7%2590%2586%25E5%25A4%25A7%25E5%25B1%258F.gif)

水厂收集数据, 数据通过什么协议进行传递

MQTT

[使用Mqtt C++客户端发送和接收MQTT消息-技术开发者的日常 (lanffy.github.io)](https://lanffy.github.io/2020/05/18/SentReceiveMQTTMessageInC++)

可以使用 MQTT 客户端发送消息到 MQTT 代理

```c
#include <iostream>
#include <cstdlib>
#include <string>
#include <map>
#include <vector>
#include <cstring>
#include "mqtt/client.h"

const std::string SERVER_ADDRESS("tcp://broker.hivemq.com:1883");
const std::string CLIENT_ID("33f1c750-01a6-4a26-9057-6a5adf0f80f5");
const std::string TOPIC("lanffy/test");
const int QOS = 1;
```

定义动作监听器，链接成功，消息发送成功后，都会回调相应的动作：

```c
class user_callback : public virtual mqtt::callback
{
void connection_lost(const std::string& cause) override {
std::cout << "\nConnection lost" << std::endl;
if (!cause.empty())
std::cout << "\tcause: " << cause << std::endl;
}

void delivery_complete(mqtt::delivery_token_ptr tok) override {
std::cout << "\n\t[Delivery complete for token: "
<< (tok ? tok->get_message_id() : -1) << "]" << std::endl;
}

public:
};
```

链接Mqtt Server并发送消息：    

```c
int main(int argc, char* argv[])
{
std::cout << "Initialzing..." << std::endl;
mqtt::client client(SERVER_ADDRESS, CLIENT_ID);

user_callback cb;
client.set_callback(cb);

mqtt::connect_options connOpts;
connOpts.set_keep_alive_interval(20);
connOpts.set_clean_session(true);
std::cout << "...OK" << std::endl;

try {
std::cout << "\nConnecting..." << std::endl;
client.connect(connOpts);
std::cout << "...OK" << std::endl;

// First use a message pointer.

std::cout << "\nSending message..." << std::endl;
auto pubmsg = mqtt::make_message(TOPIC, "Hello World,This is a message...");
pubmsg->set_qos(QOS);
client.publish(pubmsg);
std::cout << "...OK" << std::endl;

// Disconnect
std::cout << "\nDisconnecting..." << std::endl;
client.disconnect();
std::cout << "...OK" << std::endl;
}
catch (const mqtt::persistence_exception& exc) {
std::cerr << "Persistence Error: " << exc.what() << " ["
<< exc.get_reason_code() << "]" << std::endl;
return 1;
}
catch (const mqtt::exception& exc) {
std::cerr << exc.what() << std::endl;
return 1;
}

std::cout << "\nExiting" << std::endl;
return 0;
}
```

[MQTT 入门 + springboot + rabbitmq 智能家居示例](https://mp.weixin.qq.com/s/udFE6k9pPetIWsa6KeErrA?utm_source=pocket_saves)

![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/msedge_DzqL9E90sB.png)

rabbit mq 就支持 mqtt 协议

只要安装一个插件就可以了

```bash
rabbitmq-plugins enable rabbitmq_mqtt
```

#### 问题集锦

- 卡拉玛依 水厂分布 使用散点图进行展示  
  - ![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/msedge_NZ6OvrICCF.png)  
  - 地图标识示例 https://juejin.cn/post/6844903989427847181    
    ![d3 与 echarts 的区别](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/5avjCw6l3G.png)  

echarts 新版本提到 也可以使用 svg 进行渲染了  
https://echarts.apache.org/handbook/zh/best-practices/canvas-vs-svg/  
![svg 进行渲染](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/msedge_UuqX4nrrR3.png)

##### 解决了什么问题

参考: [迎接智能化浪潮，传统水厂数字化势在必行 | Mendix](https://www.mendix.com/zh-hans/customer-stories/%E8%BF%8E%E6%8E%A5%E6%99%BA%E8%83%BD%E5%8C%96%E6%B5%AA%E6%BD%AE%EF%BC%8C%E4%BC%A0%E7%BB%9F%E6%B0%B4%E5%8E%82%E6%95%B0%E5%AD%97%E5%8C%96%E5%8A%BF%E5%9C%A8%E5%BF%85%E8%A1%8C/)

- 用户痛点：传统水厂业务离散，无法实现数据实时同步，为收集和分析处理数据并辅助决策带来障碍。需要智能化管理系统帮助水厂提升管理效率，优化管理流程，实现数字化、智能化的目标。
- 解决方案：开发了智慧水务综合管理平台，帮助客户实现水厂管理的数字化转型，全面实现了“人、机、物”的协同。
- 实施效果：项目开发周期缩短50%，相应的人力资源节省50%以上；项目上线后为水厂客户实现碳减排每月0.58吨，实现药耗节约25%以上。

##### 如何对不同屏幕进行适配

[前端大屏可视化项目之--大屏适配 - 掘金 (juejin.cn)](https://juejin.cn/post/7241554408960704549#heading-10)

我使用 flex 进行适配

这样容器的各个部分的布局已经设定好了

##### 设计稿完成开发后，发现在大屏上页面有被拉伸或者压缩的情况，怎么补救？

当然是使用 transform 属性进行缩放啦

[【Design】大屏数据可视化设计指南-阿里云开发者社区 (aliyun.com)](https://developer.aliyun.com/article/940561#slide-22)

### 参考

[北控水务BECloudTM智慧水务云平台-important](https://www.aii-alliance.org/resource/c334/n1385.html)

[可视化智慧水务大屏_智慧污水处理厂_水厂数字孪生-帆软 (fanruan.com)](https://www.fanruan.com/bw/dzdkd)

[MQTT 入门 + springboot + rabbitmq 智能家居示例](https://mp.weixin.qq.com/s/udFE6k9pPetIWsa6KeErrA?utm_source=pocket_saves)

[数据可视化大屏的应用与落地实践 - 志恒说数据 - 博客园 - 设计大屏入门 = 各个图标的作用](https://www.cnblogs.com/luozhiheng/p/15649421.html)

[前端大屏可视化项目之--大屏适配 - 掘金 (juejin.cn)](https://juejin.cn/post/7241554408960704549#heading-10)

[【Design】大屏数据可视化设计指南-阿里云开发者社区 (aliyun.com)](https://developer.aliyun.com/article/940561#slide-22)
