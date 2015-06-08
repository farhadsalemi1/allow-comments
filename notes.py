# -*- coding: utf-8 -*-

lesson1 = [ 
[
'The basics',
'''In this lesson we learned the Basics of <b>HTML</b> programming. 
HTML stands for <em><b>H</b>yper <b>T</b>ext <b>M</b>arkup <b>L</b>anguage</em>.
We learned about The Web, HTML, URL. HTTP, and Web applications.'''
],
[
'HTML Vs HTTP',
'HTML is the Document and is the plain text, and HTTP is the protocol. '
],
[
'Tags',
'''We learned Tags and Elements. We also learned about <b>Inline and block concept</b>.
Some of the tags we have learned are:
&#60;b&#62;, &#60;em&#62;, &#60;a&#62;, &#60;img&#62;, &#60;br&#62;, &#60;p&#62;, &#60;div&#62;. <br>
Tags can be void which means there wouldn’t be any closing tag fro them.
Tags can have attributes. '''
],
[
'Global Attributes',
'Some of the attributes are global which means they can be uses in any tags.'
],
[
'Coding Applications',
'We also learned about <em>Scratchpad, Codepen and Github </em> applications. '
]
]

lesson2 = [
[
'Tree Structure',
'''In this lesson we learned about the <b>tree structure </b> of a HTML page,
which means we have tags and we have texts and tags inside those tags.<br>
<b>DOM:</b> Document Object Model, the tree-like structure of a page.'''
],
[
'HTML Vs CSS',
'''HTML and CSS are both Languages.
HTML controls the structure of a web page.
CSS controls the style of a page (how it looks).'''
],
[
'Boxes, boxes everywhere.',
'''In HTML every area of the page we are making, belongs to a box. so the whole page can be divided into multiple boxes.
We define these boxes with the &#60;div&#62;  tag.
We use class=attribute to give the boxes different styles.'''
],
[
'Sublime',
'''We use <b>Sublime </b> Code editor for writing our codes.'''
]
]

lesson3 = [
[
'CSS: Cascading Styling Sheet',
'''CSS is code written to control the "style" of HTML elements.<br>
"Cascading" means that rules are applied not only to the elements they directly match, but also to all of those elements' child elements. However, if a child element has multiple, overlapping rules defined for it, the more specific rule takes effect.<br>
There are two ways to include CSS Styling in a web page:<br>
1: write CSS in the "head" of your HTML<br>
2: Link your HTML to a separate CSS file<br>'''
],
[
'Avoiding Repetition',
'''The main advantage of CSS is avoiding repetition. Avoiding repetition is important for a variety of reasons.When programmers don't avoid repetition, they will often have to do the same thing over and over. This may mean copy and pasting certain style attributes into many HTML elements or rewriting the same code (sometimes with minor differences) many times. This can lead to errors when the programmer decides to make a change to something. If they don't diligently make that same change everywhere the repeated code appears, problems will arise.'''
],
[
'Inheritance',
'''Inheritance is a key feature in CSS, it relies on the ancestor-descendant relationship to operate. Inheritance is the mechanism by which properties are applied not only to a specified element, but also to its descendants. Inheritance relies on the document tree, which is the hierarchy of HTML elements in a page based on nesting. Descendant elements may inherit CSS property values from any ancestor element enclosing them. In general, descendant elements inherit text-related properties, but box-related properties are not inherited. Properties that can be inherited are color, font, letter-spacing, line-height, list-style, text-align, text-indent, text-transform, visibility, white-space and word-spacing. Properties that cannot be inherited are background, border, display, float and clear, height and width, margin, min- and max-height and -width, outline, overflow, padding, position, text-decoration, vertical-align and z-index.<br>
Inheritance prevents certain properties from being declared over and over again in a style sheet, allowing the software developers to write less CSS. It enhances faster-loading of web pages by users and enables the clients to save money on bandwidth and development costs.'''
],
[
'Selector Concpt',
'''Perhaps the biggest key to understanding CSS is understanding selectors. Selectors are what allows you to target specific HTML elements and apply style to them. We define Selectors in CSS. The Sectors can be defined in one of the following ways:<br>
ID Selector,<br>
Class Selector,<br>
Tag Selector,<br>
Attribute Selector,<br>
Positional Selectors,<br>
Pseudo Selectors.<br>'''
],
[
'Code Comments',
'''Comments are lines of text that the computer ignores. They are just there so that programmers can leave concept for other people (or themselves) to read.<br>
In HTML, code comments begin with &#60;!-- and end with --&#62;. Everything in between is ignored.<br>
In CSS, code comments begin with /* and end with */.'''
],
[
'Box Positioning',
'''Divs are block elements (as opposed to inline), so by default they take up the entire width of a page.
Adding the rule display: flex; to the appropriate CSS will override this behavior and let divs appear next to each other.'''
],
[
'Verifying HTML and CSS',
'''To verify HTML:<b> <a href="http://validator.w3.org/#validate_by_input"> http://validator.w3.org/#validate_by_input </a></b> <br>
To verify CSS:<b> <a href="http://jigsaw.w3.org/css-validator/#validate_by_input"> http://jigsaw.w3.org/css-validator/#validate_by_input </a></b>'''
]
]

lesson4 = [
[
'Programming Language',
'A programming language is what programmers use to tell a computer what to do. Python is one example of a programming language.'
],
[
'Python',
'Python is a programming language. When you write Python code and Run it, a Python Interpreter converts the code you wrote as a set of instructions that the computer itself can understand and execute.'
],
[
'Variables and Strings',
'Variables give programmers a way to give names to values and numbers. A string is just a sequence of characters surrounded by quotes.'
],
[
'Functions',
'A function is something that takes input, does something to that input, and then produces output. For example, a function named square might take a number as input and produce the square of that number as output. The main advantage of functions is avoiding repetition.'
],
[
'If and While Statements',
'If statement is used for making decisions to control which code gets executed when. while loop is used to make code that performs the same task (body of the loop) many times.'
],
[
'Lists and For Loops',
'A list is a structured object to store data.  in a list the elements can be anything you want such as characters, strings, numbers or even other lists! A for Loop is used to iterate over structured data. The For Loop goes through each element of the list in turn,  and evaluating a series of command using that element. Using the for loop, we can use less code than we needed using the while loop.'
]
]

lesson5 = [
[
'Abstraction',
'''In programming, Abstraction is a technique for managing complexity of codes. It works by establishing a level of complexity on which a person interacts with the system, suppressing the more complex details below the current level. The programmer works with an idealized interface (usually well defined) and can add additional levels of functionality from other modules that would otherwise be too complex to handle. For example, a programmer writing code that involves numerical operations may not be interested in the way numbers are represented in the underlying hardware (e.g. whether they're 16 bit or 32 bit integers), and where those details have been suppressed. It can be said that they were abstracted away, leaving simply numbers with which the programmer can work. By using different layers of complexity that have been created to abstract away the functioning details, programming layout is much more manageable.
In Python, using the existing functions from Python Standard library is an example of abstraction.'''
],
[
'Object Oriented Programming',
'''Object-oriented programming (OOP) is a programming methodology based on the concept of "objects", which are data structures that contain data (<b>attributes</b>); and code, in the form of procedures (<b>methods</b>). This is in contrast to traditional programing where a program was a procedure that takes input data, processes it, and produces output data. Here we really care about the objects we want to manipulate rather than the procedure required to manipulate them. A distinguishing feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated. In OOP, programs are designed by making them out of objects that interact with one another. In OOP, objects are instances of <b>Classes</b>, which are the building structure of our data. Classes will be defined during my notes further below.<br>
OOP can be very useful in the design of databases, where we define the structure of the records in a Class format and then every records of the database would be an instance of the class.<br>
Here are some benefits of OOP:<br>
<ol>
1. Improved software-development productivity: This is due to the fact that OOP is modular and extensible and objects can also be reused.<br>
2. Improved software maintainability: We can update different modules of a program separately.<br>
3. Faster development: The code developed during projects is reusable in future projects.<br>
4. Lower cost of development: The reuse of software also lowers the cost of development.<br>
5. Higher-quality software: We have more time for the verification of our software.<br>
</ol>'''
],
[
'Modules and import statement in Python',
'''Module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.<br>
Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.
You can use any Python source file as a module by executing an import statement in some other Python source file.
When the interpreter encounters an import statement, it imports the module if the module is present in the search path. A search path is a list of directories that the interpreter searches before importing a module.<br>
A module is loaded only once, regardless of the number of times it is imported. This prevents the module execution from happening over and over again if multiple imports occur.
Python‘s <b>"from"</b> statement lets you import specific attributes from a module into the current name space.<br>
Here are some modules we learned in this lesson:<br>
Module <b>Webbrowser</b> has useful functions dealing with Internet websites.<br>
Module <b>Time</b> has useful functions dealing with time.<br>
Module <b>OS</b> has useful functions for handling file systems.<br>
<b>Urllib</b> is a module dealing with getting information from the Internet.'''
],
[
'Python Standard Library',
'''Distributed with every copy of Python, the Standard Library contains hundreds of modules that provide tools for interacting with the operating system, interpreter, and Internet. All of them tested and ready to be used to jump-start the development of any applications.
Pythons standard library is very extensive, offering a wide range of facilities. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.
The Python installers for Windows platform usually include the entire standard library and often also include many additional components.'''
],
[
'Python External Package',
'''In addition to the Python Standard Library, there are a lot of external python methods that are not included withing Python Library. They are written by external resources and have to be downloaded if we need to use them.
Twilio is an external python package which is used for sending text messages to cell phones.'''
],
[
'Built-in Functions',
'''The Python interpreter has a number of functions built into it that are always available. When we are calling these functions, we do not have to import their module.
Open() is a built in function which opens a file and return an object type file.'''
],
[
'Class and Instance',
'''A class in Python is a building blueprint that just contains structure – it defines how something should be laid out or structured, but doesnt actually fill in the content. Classes give us the ability to create more complicated data structures that contain arbitrary content.
The class is a fundamental building block, it is a logical grouping of data and functions (method).<br>
In order to use class, we have to create an object or instance of this class.
An instance is a specific copy of the class that does contain all of the content. For example, Lets say that the government has a particular tax form that it requires everybody to fill out. Everybody has to fill out the same type of form, but the content that people put into the form differs from person to person. A class is like the form: it specifies what content should exist. Your copy of the form with your specific information is like an instance of the class: it specifies what the content actually is.<br>
When we create an instance of a class, we are actually calling a function which is defined in the class by the name of <b>__init__ (Constructor)</b>. This function then will create an space in the PC memory for this instance. So Classes do not occupy any space in the memory, the instances are the one which get some space in memory.<br>
In the class definition we can have both variables and methods (functions) defined.<br>
<b>Turtle</b> is a class in Python Standard Library which we use for drawing geometric shapes an move the cursor.'''
],
[
'Self Argument',
'''The first argument of every class method, including __init__, is always a reference to the current instance of the class. By convention, this argument is always named <b>self</b>. In the __init__ method, "self" refers to the newly created object; in other class methods, it refers to the instance whose method was called.<br>Although you need to specify "self" explicitly when defining the method, you do not specify it when calling the method; Python will add it for you automatically.'''
],
[
'Instance Variables',
'''These Variables are defined inside the __init__ function inside a class and when they are used by any instance of the class,they will be associated to that specific instance.'''
],
[
'Instance Methods',
'''These functions are defined inside a class and they have the first argument as self. When they are used by any instance of the class, they will be associated to that specific instance.'''
],
[
'Class Variables',
'''These variables are defined outside the __init__ function inside a class and they are associated with the class itself. They are the same for all the instances.'''
],
[
'Predefined Attributes',
'''There a few class variables predefined for all classes in python. Here are some of these variables:<br>
<ol>
1. __doc__  Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods. An objects docsting is defined by including a string constant as the first statement in the objects definition.<br>
2. __name__  This predefined attribute contains the name of the class as a string.<br>
3. __module__ Module name in which the class is defined in string format. This attribute is __main__ in interactive mode.<br>
</ol>'''
],
[
'Inheritance',
'''Inheritance in the subject of Object Oriented Programming means we can transfer the characteristics of a base class to other classes that are derived from it. The base class is called parent class and the derived class is called child class. Inheritance will save us from repeating codes in similar classes. We can reuse the codes written in the parent class inside child class. A child class also inherits the functions written in the parent class. However a child class can override a method that it has inherited from a parent class (<b>Method Overriding</b>).'''
],
[
'HTML/CSS and OOP',
'''CSS can be viewed as an OOP language. The same way that we have objects and classes in OOP, in CSS you also have a standard "object" (an HTML structure) and then you have CSS classes that you apply to objects, which define the design and style of the object. From this aspect, the classes in CSS are similar to classes in OOP. We define the style in the CSS class and all the HTML Tags created with that class, will inherit the same style. This inheritance in CSS class also applies to all the nested elements defined under the original HTML element, and similar to Method Overriding in OOP we can change these style definition in the CSS sub-classes.<br>
This feature will give us the advantage of avoiding the repetition in both CSS and OOP.<br>
Similar to OOP which segregates the actual object from the class, in CSS we are separating the  the actual HTML from its style. This allows flexibility and reusability.'''
]
]

lesson6 = [
[
'Server',
'''What is a "server?" A server is a computer that interacts with a request we make to the computer. For example, whenever we type in "http://www.google.com", we are sending a request to Google's servers to return a website.'''
],
[
'User Input Validation',
'''Any program input – such as a user typing at a keyboard or a network connection – can potentially be the source of security vulnerabilities and disastrous bugs. All input should be treated as potentially dangerous. Determined attackers can use carefully crafted input to cause programs to run unauthorized commands. This technique can be used to delete or damage data, run malicious programs, or obtain sensitive information. All program inputs are a potential source of problems. If external data is not validated to ensure that it contains the right type of information, the right amount of information, and the right structure of information, it can cause problems.
A robust program will respond to invalid input in a manner that is appropriate, correct, and secure. When your program runs across invalid input, it should recover as much as possible, and then repeat the request, or otherwise continue on. Arbitrary decisions such as truncating or otherwise reformatting data to “make it fit” should be avoided.'''
],
[
'HTML Templates',
'''Templates are libraries to build complicated string in Python. It can be any string, but in the context of Web Application, the templates are used to build HTML.
The main advantages of using templates are: 
It keeps your Python code clean by separating the python code from HTML.
It makes more readable code, better organized code is more readable.
It makes more secure web site b\y using a simple Autoescape parameter for escaping.
IT makes our HTML data to be easier to modify since we are modifying them in HTML editor and not Python.
and finally it help us avoid repetition with use of variables and statements in HTML file you can create a lot of similar tags with a few commands, and that in turn will help avoid making mistake in your programming.'''
]
]

my_notes = [
["Lesson 1: The Basics of the Web and HTML", lesson1],
["Lesson 2: Creating a Structured Document with HTML", lesson2],
["Lesson 3: Adding CSS style to HTML Structure", lesson3],
['Lesson 4: Automate Your Page', lesson4],
['Lesson 5: Add Videos to Your Page', lesson5],
['Lesson 6: Allow Comments', lesson6]
]
