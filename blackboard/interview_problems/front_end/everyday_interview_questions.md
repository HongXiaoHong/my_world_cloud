[fe-interview/category/history.md at master · haizlin/fe-interview · GitHub --- FE-interview/category/history.md at Master ·海兹林/FE-采访 ·GitHub](https://github.com/haizlin/fe-interview/blob/master/category/history.md)

### day 2

#### html

> html的元素有哪些（包含H5）？

##### 行内元素：

- a
- b
- span
- strong
- i
- em
- button
- input
- label
- br
- textarea
- select

##### 块元素

- div
- p
- h1-h6
- ol
- ul
- li
- table
- tbody
- td
- tr
- thead
- dl
- dt
- dd

##### H5新增元素

- section
- article
- audio
- video
- hearder
- footer
- small

#### css

> CSS3有哪些新增的特性？

CSS3 对 CSS2 的很多方面进行了扩展和增强，引入了很多新的特性和模块。以下是一些主要的 CSS3 新增特性：

1. **选择器**：CSS3 引入了一系列新的选择器，例如属性选择器（`[attr^=value]`、`[attr$=value]`、`[attr*=value]`）、结构伪类选择器（`:root`、`:nth-child()`、`:nth-last-child()`、`:nth-of-type()`、`:nth-last-of-type()`、`:last-child`、`:first-of-type`、`:last-of-type`、`:only-child`、`:only-of-type`、`:empty`）、否定伪类选择器（`:not()`）等，大大增强了选择器的功能。

2. **颜色和透明度**：CSS3 支持 RGBA、HSL 和 HSLA 颜色模型，它们分别是 RGB 和 HSL 颜色模型的透明度版本。此外，还引入了 `opacity` 属性，用于设置元素及其内容的透明度。

3. **背景**：CSS3 的背景模块增加了很多新的属性，例如 `background-size`、`background-origin`、`background-clip`，还允许对同一个元素设置多个背景图像。

4. **边框**：CSS3 引入了圆角边框（`border-radius`）、边框图片（`border-image`）、边框颜色（`border-color`）、边框样式（`border-style`）等新的边框特性。

5. **盒模型**：CSS3 引入了 `box-sizing` 属性，使得可以更灵活地控制盒模型的大小计算方式。

6. **文本效果和排版特性**：如文本阴影（`text-shadow`）、文本溢出（`text-overflow`）、文本描边（`text-stroke`）、自定义字体（`@font-face`）等。

7. **2D 转换和 3D 转换**：`transform` 属性可以对元素进行旋转、缩放、倾斜和移动等 2D 或 3D 转换。

8. **过渡和动画**：`transition` 和 `animation` 属性允许对元素的某些属性进行动画效果的控制。

9. **多列布局**：`columns`、`column-width`、`column-count` 等属性允许对元素进行多列布局。

10. **弹性布局（Flexbox）**：CSS3 引入了弹性布局模型，通过 `display: flex` 可以使得元素具有弹性布局的特性，大大简化了复杂布局的实现。

以上只是 CSS3 中的部分新特性，实际上 CSS3 还包含了更多的模块和特性，例如 Grid 布局

、媒体查询、阴影效果、过滤器效果等。

#### JavaScript

> 写一个方法去掉字符串中的空格

```javascript
const str = '  s t  r  '

const POSITION = Object.freeze({
  left: Symbol(),
  right: Symbol(),
  both: Symbol(),
  center: Symbol(),
  all: Symbol(),
})

function trim(str, position) {
  if (!POSITION[position]) throw new Error('unexpected position value')

  switch(position) {
      case(POSITION.left):
        str = str.replace(/^\s+/, '')
        break;
      case(POSITION.right):
        str = str.replace(/\s+$/, '')
        break;
      case(POSITION.both):
        str = str.replace(/^\s+/, '').replace(/\s+$/, '')
        break;
      case(POSITION.center):
        while (str.match(/\w\s+\w/)) {
          str = str.replace(/(\w)(\s+)(\w)/, `$1$3`)
        }
        break;
      case(POSITION.all):
        str = str.replace(/\s/g, '')
        break;
      default: 
  }

  return str
}

const result = trim(str)

console.log(`|${result}|`) //  |s t  r| 
```

---

```javascript

const POSITION = Object.freeze({
  left: Symbol(),
  right: Symbol(),
  both: Symbol(),
  center: Symbol(),
  all: Symbo
```

这段代码中的 `Object.freeze()` 和 `Symbol()` 是 ES6（也被称为 ECMAScript 2015）的特性。

**`Object.freeze()`** 是一个函数，可以冻结一个对象，使其无法再被修改。这意味着你不能添加新的属性，不能修改其已有属性的值，不能删除已有属性，以及不能修改其已有属性的可枚举性、可配置性、可写性。此外，冻结的对象也不能被设为原型。这个方法返回和传入的参数相同的对象。

在你的代码中，`Object.freeze()` 被用来创建一个被冻结的对象 `POSITION`。因为这个对象被冻结，所以任何尝试修改它的操作都将失败。

**`Symbol()`** 是一个新的原始数据类型，用于创建一个独一无二的值。`Symbol()` 函数会返回一个 symbol 类型的值，每次调用都会返回一个全新的、独一无二的值。

在你的代码中，`Symbol()` 被用来为 `POSITION` 对象的每个属性创建一个独一无二的值。由于每个 symbol 都是独一无二的，所以你可以确保 `POSITION` 对象的每个属性值都不会和任何其他值冲突。

总的来说，这段代码中的 `Object.freeze()` 和 `Symbol()` 的用法是典型的 ES6 特性的应用。

---

### day3

#### html

> HTML全局属性(global attribute)有哪些（包含H5）？

- id
- class
- style
- title
- data

#### css

> 在页面上隐藏元素的方法有哪些？

- display: none
- opacity: 0
- visibility: hidden
- z-index: -9999999999999
- transform: scale(0)
- margin-left: -100%
- position: relative; left: -100%
- width: 0; height: 0;

##### transform 变换

`transform` CSS 属性允许您旋转、缩放、倾斜或平移元素。它修改 CSS 视觉对象格式模型的坐标空间。

```css
transform: scale(0.5) translate(-100%, -100%);
```

![](https://raw.githubusercontent.com/HongXiaoHong/images/main/db/msedge_Nyj03qWXvl.png)

##### JavaScript

> 去除字符串中最后一个指定的字符

##### 截取下标

```javascript
function delLast (str,del) {
if (tpeof str !== 'string') {
alert('请确认要删除的对象为字符串！');
retrun false;
} else {
let index = str.lastIndexOf(del);
str.substring(0,index ) + str.substring(index+1,str.length);
}
}
```

##### 正则

```javascript
function delLast(str,target) {
  let reg =new RegExp(`${target}(?=([^${target}]*)$)`)
  return str.replace(reg,'')
}
// abcabcdef0

console.log(delLast("abcabcabdef0", "ab"));
```

### day4

#### html

>  HTML5的文件离线储存怎么使用，工作原理是什么？

HTML5 的离线存储  
[HTML5 存储方式](https://segmentfault.com/a/1190000011516871)  
[HTML5 离线存储原理](https://segmentfault.com/a/1190000006984353)

离线存储是在 HTML 5 中创建 `cache manifest` 文件来实现 Web 应用的离线版本的。

离线存储有这么几个好处：**没有网络时可以浏览**、**加快资源的加载速度**、**减少服务器负载**

离线存储的相关配置在 `.appcache` 文件中。  
通过配置 `CACHE MANIFEST`, `NETWORK`, `FALLBACK` 来控制需要被缓存的文件。  
JavaScript 也暴露了 `applicationCache` API 让我们手动进行缓存的刷新。

除了我们的storge，记得在毕业的时候，遇到了一个刁难的面试官问我，如何用h5的新特性操作一个100mb的存储和读写；

#### css

>  CSS选择器有哪些？哪些属性可以继承？

##### 选择器

- 通配符
- id 编号
- class .class
- 标签
- 后代选择器
- 子选择器
- 兄弟选择器
- 属性选择器
- 伪类选择器
- 伪元素选择器

##### 可以继承的属性

- font-size 字体大小
- font-weight 字体粗细
- font-style 字体样式
- font-family 字体系列
- color 颜色

#### javascript

> 写一个方法把下划线命名转成大驼峰命名

```javascript
function toCamel(str) {
  str = str.replace(/_(\w)/g, (match, $1) => `${$1.toUpperCase()}`);
  return str.charAt(0).toUpperCase() + str.slice(1);
}

console.log(toCamel('a_c_def')); // ACDef

```

### 5

#### html

> 简述超链接target属性的取值和作用
> 1._self 在自身所处的框架（包括iframe）中打开
> 2._blank 在新窗口打开（就算在iframe里面也是）
> 3._parent 在父框架中打开（比如你在页面中嵌套一个iframe1，再在iframe1里面嵌套一个iframe2，那么iframe2里的超链接就会在iframe1打开，并且会覆盖iframe1的所有内容）
> 4._top 不管嵌套多少层iframe，都会在最顶层打开
> 5.‘任意字符’ 与_blank一致，只是如果打开，就只会刷新已打开的窗口

#### css

> CSS3新增伪类有哪些并简要描述

CSS3 中规定伪类使用一个 `:` 来表示；伪元素则使用 `::` 来表示。

CSS3 中新增的伪元素有以下这些:

- `:first-child / :last-child` 表示子元素结构关系的
- `:nth-child() / nth-last-child()` 用来控制奇数、偶数行的（控制表单奇数、偶数行的样式）
- `:first-of-type / :last-of-type` 表示一组兄弟元素中其类型的第一个元素 [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:first-of-type)
- `:nth-of-type() / :nth-last-of-type()` 这个选择器匹配那些在相同兄弟节点中的位置与模式 an+b 匹配的相同元素` [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-of-type)
- `:root` html 根元素
- `:not()` 否定选择器，用的比较多
- `:only-child` 只有一个子元素时才会生效
- `:empty` 选择连空格都没有的元素

#### js

> 写一个把字符串大小写切换的方法

```javascript
function caseConvert(str) {
        return str.replace(/([a-z]*)([A-Z]*)/g, (m, s1, s2) => {
            return `${s1.toUpperCase()}${s2.toLowerCase()}`
        })
    }
    console.log(caseConvert('AsA33322A2aa')) //aSa33322a2AA
```

### 6

#### html

> label都有哪些作用？并举相应的例子说明

- label通常用来关联一个表单控件

```html
<label for="hobby">爱好</label>
<input id="hobby" type="checkbox"  value="0">
```

1. 利用`label`"模拟"`button`来解决不同浏览器原生`button`样式不同的问题

```html
<input type="button" id="btn">
<label for="btn">Button</label>

<style>
input[type='button'] {  display: none;}

label {  display: inline-block;  padding: 10px 20px;  background: #456;  color: #fff;  cursor: pointer;  box-shadow: 2px 2px 4px 0 rgba(0,0,0,.3);  border-radius: 2px;}
</style>
```

2. 结合`checkbox`、`radio`表单元素实现纯CSS状态切换，这样的实例就太多了。比如控制CSS动画播放和停止。下面是一部分代码。[详细实例地址](https://codepen.io/mts123/pen/EzqdbM)

```html
<input type="checkbox" id="controller">
<label class="icon" for="controller">
  <div class="play"></div>
  <div class="pause"></div>
</label>
<div class="animation"></div>

<style>
...
#controller:checked ~ .animation {  animation-play-state: paused;}...
</style>
```

还有一个基于 `radio` 的实例：[摩斯密码键盘](https://codepen.io/mts123/pen/vqpQvR)

3. `input`的`focus`事件会触发锚点定位，我们可以利用`label`当触发器实现选项卡切换效果。下面代码选自张鑫旭《CSS世界》。[实际效果链接](https://demo.cssworld.cn/6/4-3.php)

```html
<div class="box">
  <div class="list"><input id="one" readonly>1</div>
  <div class="list"><input id="two" readonly>2</div>
  <div class="list"><input id="three" readonly>3</div>
  <div class="list"><input id="four" readonly>4</div>
</div>
<div class="link">
  <label class="click" for="one">1</label>
  <label class="click" for="two">2</label>
  <label class="click" for="three">3</label>
  <label class="click" for="four">4</label>
</div>

<style>
.box {  width: 20em;  height: 10em;  border: 1px solid #ddd;  overflow: hidden;}.list {  height: 100%;  background: #ddd;  text-align: center;  position: relative;}.list > input {   position: absolute; top:0;   height: 100%; width: 1px;  border:0; padding: 0; margin: 0;  clip: rect(0 0 0 0);}
</style>
```

#### css

> 用css创建一个三角形，并简述原理

宽高设置一定数值，就明白了，就像木匠做相框，连接处都会锯成45度角，

[CSS绘制三角形—border法 - 简书 (jianshu.com)](https://www.jianshu.com/p/9a463d50e441)

```css
            width: 0;
            height: 0;
            margin: 100px auto;
            border-top: 50px solid transparent;
            border-left: 50px solid transparent;
            border-right: 50px solid transparent;
            border-bottom: 50px solid red;
```

#### js

> 写一个去除制表符和换行符的方法

```javascript
/**
 * \f  匹配换页字符。
 * \n  匹配换行字符。
 * \r  匹配回车符字符。
 * \t  匹配制表字符。
 * \v  匹配垂直制表符。
 * @param str
 * @returns {void | string}
 */
 const removeEmpty = (str) => str.replace(/[\t\n\v\r\f]/g, "");

console.log(removeEmpty(`|


|`)) // |     |
```
