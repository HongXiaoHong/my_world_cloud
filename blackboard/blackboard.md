## 常用注解

Mockito框架常用注解包括：

1. @Mock：用于创建被mock的对象实例。
2. @Spy：用于创建被spy的对象实例，即保留原对象的行为。
3. @InjectMocks：用于创建需要注入被mock对象的类的实例。
4. @Captor：用于捕获方法调用的参数，方便进行进一步的断言和校验。
5. @MockBean：用于创建Spring Bean的Mock对象，主要用于集成测试。
6. @MockitoSettings：用于设置Mockito框架的全局设置。

这些注解能够帮助开发者简化Mockito框架的使用，提高测试效率

## 扩展一下

以下是这些Mockito框架常用注解的使用方法：

@Mock：用于创建被mock的对象实例。在单元测试中，可以使用@Mock注解创建需要进行模拟的对象实例，以方便进行测试。例如：

```java
@Mock
private UserDao userDao;

```

@Spy：用于创建被spy的对象实例，即保留原对象的行为。与@Mock注解不同的是，@Spy注解会保留原对象的行为，除了被特别标记的方法，其他方法都会执行原有的代码。例如：

```java
@Spy
private UserUtils userUtils;

```

@InjectMocks：用于创建需要注入被mock对象的类的实例。在进行单元测试时，有时需要测试一个类的方法，但是该类中需要调用另一个被mock的对象的方法。这时可以使用@InjectMocks注解，将需要被mock的对象注入到该类中。例如：

```java
@InjectMocks
private UserServiceImpl userService;

```

@Captor：用于捕获方法调用的参数，方便进行进一步的断言和校验。在进行单元测试时，有时需要校验某个方法的参数是否符合预期。这时可以使用@Captor注解来捕获方法调用的参数，并进行进一步的断言和校验。例如：

```java
@Captor
private ArgumentCaptor<User> userCaptor;

```

@MockBean：用于创建Spring Bean的Mock对象，主要用于集成测试。在进行集成测试时，有时需要使用Spring容器中的Bean进行测试，但是又不希望与其他服务产生依赖关系。这时可以使用@MockBean注解，创建一个Spring Bean的Mock对象。例如：

```java
@MockBean
private UserService userService;

```

@MockitoSettings：用于设置Mockito框架的全局设置。在进行单元测试时，有时需要设置Mockito框架的一些全局设置，例如默认的返回值等。这时可以使用@MockitoSettings注解来设置这些全局配置。例如：

```java
@MockitoSettings(strictness = Strictness.LENIENT)
public class UserServiceTest {
    // ...
}

```

### @Captor

`@Captor`是Mockito框架提供的一个注解，用于捕获方法调用的参数并将其保存在参数所定义的变量中。通常用于在单元测试中进行进一步的断言和校验。

使用`@Captor`注解需要先声明一个Captor对象，例如：

```java
@Captor
private ArgumentCaptor<User> userCaptor;

```

在执行方法时，将该Captor对象传入Mockito的verify方法中，Mockito将捕获到该方法的参数，并将其保存在userCaptor中。例如：

```java
verify(userService).createUser(userCaptor.capture());
User capturedUser = userCaptor.getValue();

```

这里的`verify`方法表示验证方法是否被调用，`userCaptor.capture()`表示捕获方法的参数，`userCaptor.getValue()`则表示获取捕获的参数。

通过`@Captor`注解捕获参数后，可以对捕获到的参数进行进一步的断言和校验，以确保方法调用的正确性。

### @MockBean

`@MockBean` 是 Spring Boot 提供的一个注解，用于在集成测试中创建一个 Spring Bean 的 Mock 对象。

它的作用与 Mockito 中的 `@Mock` 注解类似，都是用于创建一个被 mock 的对象实例。但是 `@MockBean` 更加适用于集成测试，因为它可以方便地将 mock 对象注入到 Spring 容器中，以供被测试对象使用。

在使用 `@MockBean` 注解时，需要注意以下几点：

1. `@MockBean` 只能用于创建 Spring Bean 的 Mock 对象，不能用于创建普通的 Java 对象的 Mock。

2. 使用 `@MockBean` 创建的 Mock 对象只存在于 Spring 的应用上下文中，与 Mockito 创建的 Mock 对象并不一样。这意味着，如果需要在不同的测试方法中使用同一个 Mock 对象，需要将它定义为一个类级别的字段，而不能在方法中创建。

3. 在使用 `@MockBean` 创建 Mock 对象时，Spring Boot 会自动将这些对象注入到应用上下文中，而且如果被注入的对象已经在上下文中存在，那么原来的对象将会被替换成 Mock 对象。这一点需要特别注意，如果不想替换原来的对象，需要使用 `@SpyBean` 注解。

下面是一个使用 `@MockBean` 创建 Mock 对象的例子：

```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserServiceTest {

    @Autowired
    private UserService userService;

    @MockBean
    private UserDao userDao;

    @Test
    public void testFindUserById() {
        User user = new User(1L, "Alice");
        Mockito.when(userDao.getUserById(1L)).thenReturn(user);
        User result = userService.findUserById(1L);
        Assert.assertEquals(user.getName(), result.getName());
    }
}

```

在这个例子中，`UserDao` 是一个数据访问对象，在 `UserService` 中被使用。为了测试 `UserService`，需要 mock `UserDao` 对象，以便测试 `UserService` 的方法。

使用 `@MockBean` 注解可以方便地创建 `UserDao` 的 Mock 对象，并将它注入到 Spring 容器中，以供 `UserService` 使用。在测试方法中，使用 Mockito 的 `when` 方法设置 `UserDao` 的返回值，以便测试 `UserService` 的方法

## @MockitoSettings

`@MockitoSettings` 是一个注解，用于设置 Mockito 框架的全局配置，可以在整个测试类中使用。它有多个属性，可以配置各种全局设置。

以下是一些常见的属性：

- `verboseLogging`：默认为 false，可以设置为 true 来打印更详细的日志信息。
- `strictness`：默认为 `Strictness.LENIENT`，可以设置为 `Strictness.STRICT_STUBS` 或 `Strictness.WARN` 来使 Mockito 在执行时更加严格。
- `mocksOnSpies`：默认为 false，可以设置为 true 来在 spy 对象上使用 Mockito 的 stubbing 和 verification。
- `reporting`：默认为 `Reporting.ASSERT`，可以设置为 `Reporting.LOGBACK` 或 `Reporting.STDOUT` 来更改报告的方式。

使用示例：

```java
@MockitoSettings(strictness = Strictness.STRICT_STUBS)
public class MyTest {
    // ...
}

```

此示例将全局 Mockito 设置更改为 `Strictness.STRICT_STUBS`，在测试类中将更严格地对 stub 进行校验。

总的来说，`@MockitoSettings` 可以帮助测试人员全局配置 Mockito 框架，使测试更加严谨和可靠。
