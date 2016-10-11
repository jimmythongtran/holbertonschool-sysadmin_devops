Zero. The code didn't work, I think I am missing one thing (-p). Maybe it has to do with disabling the alias (+ core command), I know I am missing something. Hmmm.<br>
One. Knowing desired output helped me figure this out. echo print displays whatever follows, in this case we want the string "hello [whoami]". To print "whoami" - we use "$USER"<br>
Two. I added the whole path with $PATH amended onto it, but it doesn't work.<br>
Three. I am unsure of this one.<br>
Four. printenv prints all the environmental variables.<br>
Five. Skipping this for now.<br>
Six. I might be missing one thing, but don't know how to test this.<br>
Seven. The global (environmental) variable doesn't differ in format from local, does it?<br>
Eight. The code outputs but not as an integer.<br>
Nine. The exported global variable values are storing, but it is doesn't printf into singular number. Strange.<br> 
Ten. The exported global variable values are storing, but it doesn't printf into singular number too.<br>
Fifteen. Published on medium.com<br> 
