Zero. ~The code didn't work, I think I am missing one thing (-p). Maybe it has to do with disabling the alias (+ core command), I know I am missing something. Hmmm.~ I removed -p and it works now. <br>
One. Knowing desired output helped me figure this out. echo print displays whatever follows, in this case we want the string "hello [whoami]". To print "whoami" - we use "$USER"<br>
Two. ~I added the whole path with $PATH amended onto it, but it doesn't work.~ I amended the path variable value with /action.<br>
Three. ~I am unsure of this one.~ I translated the colons to newlines and pipelined it through the wc to print out to display the number of lines.<br>
Four. printenv prints all the environmental variables.<br>
Five. ~Skipping this for now.~ I am set now.<br>
Six. I might be missing one thing, but don't know how to test this.<br>
Seven. The global (environmental) variable doesn't differ in format from local, does it?<br>
Eight. ~The code outputs but not as an integer.~ echo prints out the expression to display. The dollar sign grabs the value assigned globally.<br>
Nine. ~The exported global variable values are storing, but it is doesn't printf into singular number. Strange.~ echo prints out the expression to display. The dollar sign grabs the values assigned globally.<br> 
Ten. ~The exported global variable values are storing, but it doesn't printf into singular number too.~ echo prints out the expression to display. The dollar sign grabs the values assigned globally.<br>
Eleven. "To convert from a base-10 integer to its base-2 (binary) equivalent, the number is divided by 2." Hence, I thought I would get the number by multiplying by 2. No dice.<br>
Twelve. Skipping for now, too many requirements right now.<br>
Thirteen. printf is inherited from C. "%0.2f" prints out a floating point number with two decimal places. \n prints out a new line.<br>
Fifteen. Published on medium.com<br> 
