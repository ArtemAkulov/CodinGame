###################################
#                                 #
#  CodinGame  Code Golf Problems  #
#          Don't Panic            #
#                                 #
###################################

p=input;g=str.split;t=int;r=print;e={};q=g(p());e[q[3]]=q[4];e['-1']=0;w='BLOCK';exec('a,b=g(p());e[a]=b;'*t(q[7]))
while 1:f,c,d=g(p());u=t(e[f]);r((w,'WAIT')[(u<=t(c)and'L'in d)|(u>=t(c)and'R'in d)or'N'in d])