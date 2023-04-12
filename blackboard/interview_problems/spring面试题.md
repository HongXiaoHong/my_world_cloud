## spring基础

### Spring是如何简化开发的

Spring是一个开源框架，它为Java开发提供了许多便利。它采用了依赖注入和面向切面编程等现代编程技术，使得Java开发变得更加简单和快速。

下面是Spring简化Java开发的几个方面：

1. 依赖注入（DI）：通过依赖注入，开发人员可以更容易地管理应用程序的依赖关系。相比之下，手动管理对象的依赖关系通常需要更多的代码和更多的时间。Spring框架的DI功能可以通过自动装配将对象的依赖关系自动注入到需要它们的组件中，从而简化了Java应用程序的开发。

2. 面向切面编程（AOP）：面向切面编程可以将应用程序的核心逻辑与横切关注点（例如日志记录、事务管理等）分离开来。Spring框架的AOP功能可以通过声明式事务管理等方式来帮助开发人员轻松地实现横切关注点。

3. 模板化：Spring框架为开发人员提供了许多用于不同数据访问技术的模板。这些模板可以让开发人员轻松地使用Hibernate、JDBC等数据访问技术，从而减少了编写样板代码的工作量。

4. 统一的异常处理：Spring框架提供了一个全局异常处理器，可以捕获和处理应用程序中的异常。这样，开发人员就不需要在每个地方单独处理异常了。

综上所述，Spring框架可以帮助开发人员更轻松地管理Java应用程序的依赖关系、实现横切关注点、访问数据和处理异常。这些功能都可以减少开发人员的工作量，使他们能够更专注于应用程序的核心业务逻辑。

## spring IOC 的理解

Spring的IOC（Inversion of Control，控制反转）是一种软件设计模式，它的核心思想是将对象的创建和依赖关系的管理从应用程序代码中抽离出来，并由容器来完成。

在传统的Java应用程序中，对象的创建和依赖关系的管理通常由应用程序代码直接完成。这样做会导致代码的复杂性和耦合性增加，使得应用程序难以维护和扩展。

而使用Spring的IOC容器，我们只需要将对象的定义和依赖关系的管理交给容器，容器会在应用程序启动时自动完成对象的创建和依赖关系的管理。这样可以大大降低代码的复杂性和耦合性，提高代码的可读性、可维护性和可扩展性。

在Spring中，IOC容器的实现主要是通过依赖注入（Dependency Injection，DI）和控制反转（Inversion of Control，IOC）来实现的。依赖注入是指将对象所需要的依赖关系通过构造函数参数、属性或方法参数等方式注入到对象中；而控制反转则是指将对象的创建和依赖关系的管理交给容器。

总之，Spring的IOC容器可以帮助我们将对象的创建和依赖关系的管理从应用程序代码中解耦出来，从而提高代码的可维护性和可扩展性。

### SpringBoot 启动流程

SpringBoot启动流程如下：

1. 加载配置文件：在启动时，Spring Boot会加载`application.properties`或`application.yml`配置文件，这些文件通常位于项目的`src/main/resources`目录下。这些配置文件包含了应用程序的各种配置，如数据库连接、端口号、日志级别等。

2. 创建SpringApplication对象：当执行`main`方法时，首先会创建一个`SpringApplication`对象。这个对象包含了应用程序的基本信息和配置，如应用程序的类型（Web应用或非Web应用）、应用程序的资源和类加载器等。

3. 运行SpringApplication对象：通过调用`SpringApplication`对象的`run`方法，开始启动应用程序。在此过程中，Spring Boot会执行以下步骤：
   
   a. 注册监听器：Spring Boot会注册一些预定义的监听器，如`LoggingApplicationListener`（用于配置日志系统）和`ConfigFileApplicationListener`（用于加载配置文件）等。
   
   b. 准备环境：根据配置文件和命令行参数等信息，创建一个`Environment`对象。这个对象包含了应用程序的环境变量、系统属性和配置属性等信息。
   
   c. 创建上下文：根据应用程序的类型（Web应用或非Web应用），创建一个合适的`ApplicationContext`实例，如`AnnotationConfigServletWebServerApplicationContext`或`AnnotationConfigApplicationContext`。
   
   d. 准备上下文：将`Environment`对象设置到`ApplicationContext`中，并注册一些预定义的Bean，如`PropertySourcesPlaceholderConfigurer`（用于处理占位符）和`AutowiredAnnotationBeanPostProcessor`（用于处理@Autowired注解）等。
   
   e. 加载应用程序的Bean：扫描应用程序的包路径，查找并注册带有`@Configuration`、`@Component`、`@Service`、`@Repository`等注解的类，将这些类作为Bean注册到`ApplicationContext`中。
   
   f. 初始化应用程序的Bean：对所有已注册的Bean进行实例化和依赖注入，并调用`@PostConstruct`注解的方法。
   
   g. 刷新上下文：完成Bean的初始化，并触发`ApplicationReadyEvent`事件，表示应用程序已经准备好接受请求。
   
   h. 启动内嵌容器：如果应用程序是一个Web应用，Spring Boot会启动一个内嵌的Servlet容器（如Tomcat、Jetty或Undertow）来处理HTTP请求。

4. 应用程序启动完成：在完成以上步骤后，应用程序已经启动并准备好接受请求。如果是一个Web应用，可以通过浏览器访问相应的URL来测试应用程序。

整个启动流程中，Spring Boot通过自动化配置和约定优于配置的原则，使得开发者可以

### SpringBoot 自动装配原理

SpringBoot的自动装配是通过条件化配置（Condition）和Spring Framework的组件扫描机制实现的。当需要某个类或接口的实现时，SpringBoot会根据条件判断，选择是否自动装配。

自动装配的条件判断主要通过实现Condition接口来实现，Condition接口中的matches()方法返回一个boolean类型的值，用来表示当前自动装配条件是否满足。SpringBoot通过扫描类路径中的META-INF/spring.factories文件来获取所有的条件化配置，并将其存储在一个名为AutoConfigurationMetadata的数据结构中，这个数据结构描述了所有自动配置类和它们所需要的条件。

在自动装配的过程中，SpringBoot会扫描应用程序中的所有Bean，并将它们注册到IOC容器中。同时，SpringBoot会按照一定的顺序执行所有自动配置类的configure()方法，根据条件判断，自动装配需要的Bean。

### SpringBoot中BeanFactory/ApplicationContext区别

BeanFactory和ApplicationContext都是Spring Framework中的核心接口，它们的主要区别在于BeanFactory是Spring Framework的基础设施，而ApplicationContext是BeanFactory的扩展，提供了更多的功能。

具体来说，BeanFactory是Spring Framework的核心接口，提供了依赖注入和基本的Bean生命周期管理等基础功能。它是一个工厂类，负责创建和管理Bean。在应用程序启动时，BeanFactory会加载并解析Bean的定义信息，但在获取Bean实例时才会实例化Bean。

ApplicationContext则是BeanFactory的扩展，提供了更多的功能，例如国际化、资源访问、事件发布、AOP等。同时，ApplicationContext在应用程序启动时会预先实例化所有的单例Bean，从而提高应用程序的启动速度。

### Spring中的设计模式

Spring中使用的设计模式包括：

1. 依赖注入模式（Dependency Injection）：通过依赖注入，实现对象之间的松耦合，从而提高代码的可维护性和可测试性。

2. 面向切面编程（Aspect-Oriented Programming）：通过将应用程序的核心逻辑和横切关注点分离开来，提高代码的可重用性、可维护性和可扩展性。

3. 模板方法模式（Template Method）：Spring Framework提供了许多模板类，例如JdbcTemplate、HibernateTemplate等，通过模板方法模式来封装重复性的代码逻辑，从而提高开发效率。

4. 单例模式（Singleton）：在Spring Framework中，Bean默认是单例模式的，这可以提高应用程序的性能和效率。

5. 工厂模式（Factory）：在Spring Framework中，BeanFactory就是工厂模式的一个实现，负责创建和管理Bean。

6. 观察者模式（Observer）：Spring Framework中的事件机制就是一个观察者模式的实现，它允许对象在状态发生变化时通知其他对象。
   
   总之，Spring Framework中的设计模式有助于实现松耦合、重复性代码的封装和提高代码的可重用性、可维护性和可扩展性等目标。
