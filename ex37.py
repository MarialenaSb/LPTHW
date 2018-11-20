
     ****KEYWORDS****

• and
• del # the del statement/  ex: del list_item[4,] I could use the following: list_item[4]=None (I assign none to it)
      # Deletion is recursively defined very similar to the way assignment is defined. Deletion of a target list recursively deletes each target, from left to right. Deletion of a name removes the binding of that name from the local or global namespace, depending on whether the name occurs in a "global" statement in the same code block.

• from # the import statement
• not # boolean operation. The operator "not" yields "True" if its argument is false, "False" otherwise.

• while #the while statement is used for repeated execution as long as an expression is true.
        #while_stmt ::= "while" expression ":" suite
                   #      ["else" ":" suite]

• as # the as keyword is used to creat an alias.
     #      ex:  import calendar as c
     #           print(c.month_name[1]) --> January

• elif # it says to python that if the previous conditions were Fault then try this one.
• global # global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.The global keyword is the way that you tell python that a particular variable in your function is defined at the global (module-level) scope.
    #[ex1:]
         #myvariable = 5
         #def func():
         #    myvariable = 6     --> creates a new "local" variable.  Doesn't affect the global version
         #    print(myvariable)  --> prints 6

         #func()
         #print(myvariable)     --> prints 5

    #[ex2:]
         #myvariable = 5
         #def func():
         #    global myvariable
         #    myvariable = 6    --> changes `myvariable` at the global scope
         #    print(myvariable) --> prints 6

         #func()
         #print(myvariable)  --> prints 6 now because we were able to modify the reference in the function

• or # The expression "x or y" first evaluates *x*; if *x* is true, its value
• with # The 'with' statement clarifies code that previously would use try - except -finally blocks to ensure that clean-up code is executed. The advantage of using a with statement is that it is guaranteed to close the file no matter how the nested block exits.
       #If an exception occurs before the end of the block, it will close the file before the exception is caught by an outer exception handler. If the nested block were to contain a return statement, or a continue or break statement, the with statement would automatically close the file in those cases, too.
    #ex:
       #with open('output.txt', 'w') as f:
       #    f.write('Hi there!') --> The above with statement will automatically close the file after the nested block of code.

# ***Assertions are statements that assert or state a fact confidently in your program.
#For example, while writing a division function, you're confident the divisor shouldn't be zero, you assert divisor is not equal to zero.
#Assertions are simply boolean expressions that checks if the conditions return true or not. If it is true, the program does nothing and move to the next line of code.
# However, if it's false, the program stops and throws an error.***

• assert # It helps detect problems early in your program, where the cause is clear, rather than later as a side-effect of some other operation. Assert statement has a condition or expression which is supposed to be always true.
         # If the condition is false assert halts the program and gives an AssertionError./ assert <condition>


• else #The else keyword catches anything which isn't caught by the preceding conditions.
• if # We use the if statement to test some logical conditions. When one condition is True that suite is executed (and no other part of the "if" statement is executed or evaluated).
• pass #"pass" is a null operation --- when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed.
       # ex  def f(arg): pass   --> a function that does nothing (yet)
       #It is also useful in places where your code will eventually go, but has not been written yet i.e. in stubs:
#for letter in 'Python':
#  if letter == 'h':
#      pass
#      print ('This is pass block')
 #  print ('Current Letter :', letter)

• yield # The yield statement can be used to omit the parentheses that would otherwise be required in the equivalent yield expression statement.
• break # It terminates the nearest enclosing loop, skipping the optional "else" clause if the loop has one.
        # It may only occur syntactically nested in a "for" or "while"loop, but not nested in a function or class definition within that loop.

• try - except - finally # try-except-finally: The try block lets you test a block of code for errors - The except block lets you handle the error. - The finally block lets you execute code, regardless of the result of the try- and except blocks.
                        # When an error occurs, or exception as we call it, Python will normally stop and generate an error message. These exceptions can be handled using the try statement:
#ex: https://www.w3schools.com/python/python_try_except.asp
# common exception errors: https://www.pythonforbeginners.com/error-handling/python-try-and-except

• import # We use the import module in order to import modules.
• print # Prints the values to a stream, or to sys.stdout by default.
• class # Creates a class (A Class is like an object constructor, or a "blueprint" for creating objects.)
• exec # Execute the given source in the context of globals and locals. The exec() doesn't return any value, it returns None
• in # The operators "in" and "not in" test for membership.  "x in s" evaluates to true if *x* is a member of *s*, and false otherwise. For container types such as list, tuple, set, frozenset, dict, or collections.deque, the
     #expression "x in y" is equivalent to "any(x is e or x == e for e in y)". For the string and bytes types, "x in y" is true if and only if *x* is a substring of *y*.  An equivalent test is "y.find(x) != -1".  Empty
     #strings are always considered to be a substring of any other string, so """ in "abc"" will return "True".

• raise # 1. It's used for raising your own errors, 2. it reraises the current exception in an exception handler, so that it can be handled further up the call stack.
                                                    # If no exception is active in the current scope, a "RuntimeError" exception is raised indicating that this is an error.
        # https://stackoverflow.com/questions/13957829/how-to-use-raise-keyword-in-python/13957849#13957849

• continue # "continue" may only occur syntactically nested in a "for" or "while" loop, but not nested in a function or class definition or "finally" clause within that loop. It continues with the next cycle of the nearest enclosing loop.
           # When "continue" passes control out of a "try" statement with a "finally" clause, that "finally" clause is executed before really starting the next loop cycle.

• is # The is operator compares identities.
     # ATTENTION: The == operator compares by checking for equality!If we suppose that we have two twins as python objects and we’d compare them with the == operator, we’d get “both people are equal” as an answer.
     # If we compared these people with the is operator, we’d get “these are two different people” as an answer.
     # a==b --> True means that the two list objects look the same. a is b means that both variables are in fact pointing to one list object.

• return # "return" may only occur syntactically nested in a function definition, not within a nested class definition.
• def # defines a user-defined function object
• for # The "for" loop is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object.
      # https://www.w3schools.com/python/python_for_loops.asp

• # lambda: Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. A lambda function can take any number of arguments, but can only have one expression.
 #x = lambda a: a + 10
 #print(x(5)) --> 15

# lambda functions are useful when we use them as an anonymous function inside another function.

#def myfunc(n):
 # return lambda a : a * n
#mydoubler = myfunc(2)
#print(mydoubler(11)) -->22




   ****DATA TYPES****

• True: ex27 I get this when an expression is true
• False: ex27 I get this when an expression is false
• None:  If we get to the end of any function and we have not explicitly executed any return statement, Python automatically returns the value None (t has to return something, because every Python function does).
• strings:  We can create them by enclosing characters in quotes ("Hello world")
• numbers: 1,2,3,4,5.6,-21 etc
• floats: a number, positive or negative, containing one or more decimals. x = 3.45 y= -1.42
• lists: A list is a collection which is ordered and changeable. in order to create a list we use the list() constructor.# ex: thislist = list(("apple", "banana", "cherry"))




    ****STRING FORMATS****

• %d #Integers
• %i #Signed integer decimal.
• %o #Signed octal value.( Requires integer)
• %u #Obsolete type – it is identical to 'd'.
• %x #Hex format. Outputs the number in base 16, using lower- case letters for the digits above 9.(Requires integer)
• %X #Hex format. Outputs the number in base 16, using upper- case letters for the digits above 9.( Requires integer)
• %e #Floating point exponential format (lowercase). (Requires a real number)
• %E #Floating point exponential format (uppercase).
• %f #Floating point numbers
• %F #Floating point decimal format.
• %g #Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. (Requires a real number)
• %G #Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. (Requires a real number)
• %c #Character. Converts the integer to the corresponding unicode character before printing. (requires int or char).
• %r # everything
• %s # String (or any object with a string representation, like numbers)
• %% #No argument is converted, results in a '%' character in the result.


     ****OPERATORS****
#https://realpython.com/python-operators-expressions/

• +   # adds
• -   # subtracts
• *   # multiplies
• **  # calculate powers --> x**y (x to the power y)
• /   # divides.. always returns a float
• //  # Does floor division (Mathematical division that rounds down to nearest integer.) and get an integer result (discarding any fractional result)
• %   # calculate the remainder
• <   # less-than. True if left operand is less than the right
• >   # greater-than. True if left operand is greater than the right
• <=  # less- than -equal.  True if left operand is less than or equal to the right
• >=  # greater- than - equal. True if left operand is greater than or equal to the right
• ==  # is equal to. True if both operands are equal
• !=  # does not equal. True if operands are not equal
• <>  #  not equals --> x < y, x <= y, x >= y, x > y, x = y, x <> y, 0 <= d < 10
• ( ) # 1. call functions or methods, 2. group expressions: print(3*(4+5)), 3. construct (or deconstruct) tuples: a = (3,4)
• [   # 1. index specific items in a tuple or list (or in general, any sequence): print(a[1]), 2. construct/deconstruct lists: b = [3,4] or a_list = ['one', 'two', 3, 4]
• { } #  defines an empty dict --> a_dict = { one: 1, two: 2 }
• @   # An @ symbol at the beginning of a line is used for class, function and method decorators.
• ,   # separates strings from variables
• :   # Tells python we are going to create a new block of code followed by a new line with 4 inoented spaces and then code. for example it defines things in functions.
• .   # we can call functions on variables or string connect multiple functions.
• =   # assigns value to a variable or function.
• ;   # we can separate multiple lines of code on one line.
• +=  # adds another value with the variable's value and assigns the new value to the variable. x =3 and x+=2 then print x gives 5
• - = # subtracts a value from variable, setting the variable to the result
• *=  # multiplies the variable and a value, making the outcome the variable
• /=  # divides the variable by the value, making the outcome the variable
• //= # divides the variable by the value and rounds down to nearest integer, making the outcome variable
• %=  # performs modulus on the variable, with the variable then being set to the result of it
• **= # calculates the variable to the power of the value and the outcome becomes the variable.
