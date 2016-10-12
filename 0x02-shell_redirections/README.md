# describe what each script is doing
0: "echo" is the linux command that will print [display]. "Hello world" is the string that needs to be printed.<br>
1: ~Between grep and echo, not sure yet so I will have to revisit as I keep getting "unexpected EOF"~ Quotation marks and a backslash was all I needed.<br>
2: "cat" is the linux command that prints out the content of the file, followed by the name of the file you want to display.<br>
3: "cat" is the linux command that prints out the content of the file, followed by the name of the file you want to display. In this case, we want to display two of them, so we write out both of them.<br>
4: Dora's tip was most helpful (also helped me know I was on the right track for the previous "display text" exercises). "tail" is the linux command that prints out the last 10 lines of the file.<br>
5: "head" is the linux command that prints out the first 10 lines of the file we want to display.<br>
6: "head" outputs the first part of the file, with the third line specified with "-n 3". "tail -n 1" specifies that only one line should print out to display.<br>
7:~This has to do with 1, which I am not sure about but I think my Synopsis is in the right direction.~ I used manual backslash entry.<br>
8: "ls -la" will take the contents of its own output and append it to the file "ls_cwd_content". Since the file doesn't even exist, it will be created (unsure if you can use ">" to do this as well).<br>
9: We want to duplicate the last line, so we need to use "tail". Being it's the last line (we want to duplicate), we need to use "-n 1". Lastly, we need to name the file we want this script to execute on (to duplicate the last line). I didn't append it into the file iacta. Now I did.<br>
10: "find" is the command. I'm not sure what ~ does. "-type f" classifies it as a regular file. '-name "*JPG"' specifies the name of the files we are looking for, with the wildcard+JPG enclosed in quotations to prevent pathname expansion by the shell. '-delete' deletes.<br>
11: ~I am in the right direction but keep getting an error message on the "wc -1" format.~ Should have been wc -l, as in the script displays the long format.<br>
12: ~I get this error message right now: sort: option requires an argument -- 't'.~ I used ls insteadwith the flag: field seperator, and pipelined it with the head (filter).<br>
13: "uniq" finds the unique words, with the option -u that only prints the unique lines. I also did not sort to alphabetize the list.<br>
14: "grep" prints out the line when it matches with its designated pattern.<br>
15: "grep -c" prints out the number of lines that contain a particular designated pattern.<br>
16: ~I have the synopsis down but my code test doesn't output anything.~ I removed the quotation marks from "root." The -A flag appends 3 lines after displaying the lines in the pattern for context.i<br>
17: The invert option (-v) option is needed to do the opposite of what would otherwise be a run of the mill grep script.<br>
18: I used my error to fix the syntax of my synopsis, but I still get no output.<br>
19: I believe grep and tr should be used together with a pipeline, but I can't figure out how that code would play out according to syntax.<br>
20: Used tr with the flag -d (for delete) with the characters I want to delete in quotation marks.<br>
21: Like most of the challenges, I initially overthought this. Then, I looked at the commands we should be most concerned with today and found my rev, which I guessed to be the command I needed, as I have gotten into the habit of thinking commands from the perspective of the creator.<br>
22:<br>
