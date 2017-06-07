# Checkio-Python-projects
1. Pawn Brotherhood

This was a tough one for me. I hadn't encoutered sets yet and wasn't sure how to iterate through them. I spent a long time trying to split the coordinates into separate entities but finally realized I could iterate through them and use the index to get to the coordinate I needed.

There are much easier and more elegant ways of doing what I did, from the other solutions I've seen but they all use concepts I don't know yet. So yeah, lots to learn!

2. Median

This was a lot simpler. The idea is to find the median in a list of numbers. 

3. DaysBetween

So this function calculates the number of days between two dates. I first tried to solve it by actually trying to count the number of days myself. First by converting dates to a number of days and substracting the values, then by substracting the two dates and converting to days. After searching a bit, I came across the datetime library which made solving this problem a lot easier. The only difficulty I had was figuring out how to convert the data I was given (two tuples) into a usable datetime object.

4. NumberBase

I really felt stupid after seeing the other answers to this problem. The object is to build a function that accepts a number as a string and the radix of the numerical system use and output the integer, while refusing any number that doesn't fit with that numerical system. I finally came up with this solution, only to find that Python has a built-in function that does this: it's called int(). I've been using it to convert floating point numbers, but hadn't realized I could also input a base other than 10. Live and learn!
