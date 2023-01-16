**NOTA** is the correct answer.

t_mean.start()
t_stdv.start()

t_stdv.join()
t_mean.join()

`t_mean` and `t_stdv` are both started and run concurrently. Although `t_mean` starts split second before the `t_stdev` thread, both of them will execute for the same amount of time. In such concurrent executions, the process scheduling algorithm plays a very important role in determining which one will finish first. 

Since these are very simple functions, almost always mean thread will finish first because it got spun split-second before stdv thread. You could view the output.txt file in the attached github link to have a look at 100 simulations of the above program and the corresponding results.

Had the joins been interleaved between starts, then the case would've been different eg.

t_mean.start()
t_mean.join()

t_stdv.start()
t_stdv.join()

This would deterministically cause the `t_mean` thread to be executed before `t_stdv` because t_mean gets joined with main thread and blocks it from proceeding any further in it's execution until `t_mean` executes entirely. So there will be a time difference of ~5 seconds between mean and standard deviation print statements in the above problem.

https://github.com/ElisonSherton/thread-problem

## Data Science Motivation

Most data scientists use Jupyter Notebooks for brainstorming/ideating/executing/training/testing and now even deploying code. It has this beautiful property of mixing text and code and persists variables and functions and it's a very user-friendly python interpretor in some sense. 

One thing with Jupyter Notebooks is that it always executes cells sequentially, well I mean in the sequence in which the user ran the cells. 

There are cases when you'd like to run something but not wait till it completes execution to try and run some other code in another cell. This small trick can come in very handy in such cases. You could wrap the code that you want to run in a function and start a thread concurrently so that this work keeps happening in background while you're free to use your notebook to do your stuff, whatever it may be. I find this helpful in my day to day coding and hope you will to :) Happy coding!