JVM

- 内存泄漏
  
  - 如何解决

NIO netty

spring cloud gateway

oauth2

- oauth2 授权

rabbitmq

- 如何保证MQ消息不丢失

springboot ＋ vue

Spring Cloud Alibaba是一个基于Spring Cloud的微服务框架，它整合了Alibaba的一些开源组件，以提供云原生应用程序的基础设施。以下是Spring Cloud Alibaba的一些核心组件：

1. Nacos：一个易于使用的、功能强大的动态服务发现、配置和服务管理平台。Nacos可以替代Spring Cloud Eureka作为服务注册和发现中心，同时还提供了分布式配置管理功能，类似于Spring Cloud Config。

2. Sentinel：一个轻量级的流量控制、熔断和系统负载保护组件。Sentinel可以替代Spring Cloud Hystrix作为服务降级和熔断器实现，提供更细粒度的流量控制策略。

3. RocketMQ：一款高性能、可扩展的消息中间件。Spring Cloud Alibaba提供了与RocketMQ的整合，使得开发者可以方便地实现分布式事务和事件驱动架构。

4. Seata：一个分布式事务解决方案，支持AT、TCC、SAGA和XA模式。Spring Cloud Alibaba提供了Seata的整合，帮助开发者在微服务环境中实现分布式事务。

5. Dubbo：一个高性能的RPC通信框架。Spring Cloud Alibaba提供了与Dubbo的整合，使得开发者可以使用基于Dubbo的服务间通信，而不仅仅是基于HTTP的RESTful API。

6. Spring Cloud Alibaba OSS：一个与阿里云对象存储服务（OSS）的整合组件，提供了简单的API来与阿里云OSS进行交互，如上传、下载、删除等操作。

7. Spring Cloud Alibaba SMS：一个与阿里云短信服务（SMS）的整合组件，提供了发送短信的简便方法。

8. Spring Cloud Alibaba SchedulerX：一个与阿里巴巴SchedulerX定时任务调度中心的整合组件，提供了简单的API来创建、查询、更新和删除定时任务。

通过使用Spring Cloud Alibaba，开发者可以利用Alibaba的一些核心组件来构建云原生应用程序，同时仍然享有Spring Cloud所提供的抽象和简化。这些组件可以帮助解决分布式系统中的常见问题，如服务发现、配置管理、负载均衡、熔断和降级等。

---
