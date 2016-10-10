0. The code didn't work, I think I am missing one thing (-p). Maybe it has to do with disabling the alias (+ core command), I know I am missing something. Hmmm.<br>
1. Knowing desired output helped me figure this out. echo print displays whatever follows, in this case we want the string "hello [whoami]". To print "whoami" - we use "$USER"<br>
2. I added the whole path with $PATH amended onto it, but it doesn't work.<br>
3. I am unsure of this one.<br>
4. printenv prints all the environmental variables.<br>
5. Skipping this for now.
6. I might be missing one thing, but don't know how to test this.<br>
15. Published on medium.com<br> 
