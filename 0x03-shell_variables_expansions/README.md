0. The code didn't work, I think I am missing one thing (-p). Maybe it has to do with disabling the alias (+ core command), I know I am missing something. Hmmm.<br>
1. Knowing desired output helped me figure this out. echo print displays whatever follows, in this case we want the string "hello [whoami]". To print "whoami" - we use "$USER"<br> 
