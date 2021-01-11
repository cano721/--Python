data = """What is Python?
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development."""


count = {}; #'a' : 10, 'b': 120, 'c':90
for c in data:
    if c.isalpha() == False:
        continue
    c =c.lower();
    if c not in count:
        count[c] =1; #ex) {'c' = 1}
    else:
        count[c] +=1;
print(count.items());
result = sorted(count.items(), key= lambda x:x[1], reverse=True);
print(result[0:5]);
