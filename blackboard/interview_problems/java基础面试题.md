基础知识复习:

[Java教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1252599548343744)

## 序列化/反序列化

### Hessian2序列化java某个pojo类, pojo类需不需要填写 serialVersionUID, 继承 Serializable?

 Hessian2 序列化实际上不依赖于 Java 的内置 `Serializable` 接口。因此，您在使用 Hessian2 对 POJO 进行序列化时，不需要让 POJO 类实现 `Serializable` 接口，也不需要为其定义 `serialVersionUID`。  

Hessian2 是一个独立的二进制序列化协议，与 Java 原生的序列化机制不同。它不仅可以用于 Java，还可以用于其他语言。Hessian2 的序列化过程不需要 POJO 类实现 `Serializable` 接口，也不会检查 `serialVersionUID`。  

然而，在某些情况下，为了代码的清晰和兼容性，您可能仍然希望为 POJO 类添加 `Serializable` 接口和 `serialVersionUID`。这样，如果您决定在未来切换到 Java 原生的序列化机制，这些类就已经为此做好了准备。但是请注意，这不是使用 Hessian2 序列化所必需的。

## 代理

### 动态代理

```java
import java.lang.reflect.InvocationHandler;  
  import java.lang.reflect.Method;  import java.lang.reflect.Proxy;  
public class JdkProxyHandler implements InvocationHandler {  
private Object target;  

    public JdkProxyHandler(Object target) {        this.target = target;    }  
    @SuppressWarnings("unchecked")    public <T> T getProxyInstance() {        return (T) Proxy.newProxyInstance(target.getClass().getClassLoader(),                target.getClass().getInterfaces(),                this);    }  
    @Override    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {        System.out.println("JDK Proxy - Before method execution");        Object result = method.invoke(target, args);        System.out.println("JDK Proxy - After method execution");        return result;    }}  
```

上面是创建动态代理一段有关的类和方法  

> 创建invoke方法返回的result是否要与原来的被代理的类方法类型相同吗?不同会报错吗?  

`invoke` 方法返回的 `result` 应该与被代理类方法的返回类型相同。当您使用动态代理调用方法时，实际上是调用 `InvocationHandler` 的 `invoke` 方法，它返回的结果将作为代理方法的返回值。  

如果 `invoke` 方法返回的结果与被代理类方法的返回类型不同，那么在运行时会抛出 `ClassCastException`。因为代理方法期望返回与被代理类方法相同的类型，而实际返回了一个不同类型的对象，这将导致类型转换异常。  

因此，在实现 `invoke` 方法时，请确保返回的结果与被代理类方法的返回类型一致。通常情况下，您可以直接将原始方法的调用结果（通过 `method.invoke(target, args)`）返回，以确保返回类型的正确性。

## 多线程

### synchronized

synchronized底层如何实现？什么是锁的升级、降级？

#### synchronized底层如何实现？

synchronized是Java内建的同步机制，所以也被称为Intrinsic Locking，它提供了互斥的语义和可见性，当一个线程已经获取当前锁时，其他试图获取的线程时只能等待或者阻塞在那里。Java5之前，synchronized是唯一的同步方式。synchronized关键字既可以用来修饰方法，也可以使用在特定的代码块儿上，本质上synchronized方法相当于把方法全部语句用synchronized 代码包起来。

synchronized是基于一对 monitorenter／monitorexit 指令实现的，Monitor对象是同步的基本实现单元，无论是显示同步，还是隐 式同步都是如此。区别是同步代码块是通过明确的monitorenter和monitorexit 指令实现，而同步方法通过ACC＿SYNCHRONIZED 标志来隐式实现。

### 没有多线程，高并发开发经验 如何回答

[(47 封私信 / 80 条消息) 我没有高并发项目经验，但是面试的时候经常被问到高并发、性能调优方面的问题，有什么办法可以解决吗？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/421237964)
