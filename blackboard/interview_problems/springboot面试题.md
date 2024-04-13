## springboot打成的jar包与普通jar包有什么区别

Spring Boot 打包的 JAR 文件与普通 Java JAR 文件有几个主要区别：  
可执行性：Spring Boot 打包的 JAR 文件是可执行的，这意味着您可以直接运行它而无需使用外部应用服务器。您只需在命令行中使用以下命令即可启动 Spring Boot 应用程序：  

```
java -jar your-spring-boot-app.jar  
```

这是因为 Spring Boot JAR 文件包含了一个嵌入式的 servlet 容器（通常是 Tomcat、Jetty 或 Undertow），用于运行应用程序。  
目录结构：Spring Boot JAR 文件的目录结构与普通 JAR 文件略有不同。它包含一个特殊的 `BOOT-INF` 目录，其中包含了应用程序的类和依赖库。这种目录结构允许 Spring Boot 将应用程序的依赖项与应用程序代码分离，从而避免了类加载器级别的冲突。  

以下是 Spring Boot JAR 文件的典型目录结构：  

```scss
your-spring-boot-app.jar  
|- META-INF  
|  |- MANIFEST.MF  
|- org  
|  |- springframework  
|     |- boot  
|        |- loader  
|           |- (Spring Boot Loader classes)  
|- BOOT-INF  
   |- classes   |  |- (your application's compiled classes)   |- lib      |- (your application's dependency JARs)```  

启动器：Spring Boot JAR 文件的 `META-INF/MANIFEST.MF` 文件中包含一个 `Main-Class` 属性，该属性指向 Spring Boot 启动器类（通常是 `org.springframework.boot.loader.JarLauncher`）。这使得 JAR 文件具有可执行性，允许 JVM 知道从哪个类开始执行。  

总之，Spring Boot JAR 文件与普通 JAR 文件的主要区别在于其可执行性、目录结构和启动器。Spring Boot JAR 文件旨在简化应用程序的部署和运行，无需依赖外部应用服务器。
```
