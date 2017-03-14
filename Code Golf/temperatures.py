###################################
#                                 #
#  CodinGame  Code Golf Problems  #
#          Temperatures           #
#                                 #
###################################

input();j=input()or'0';print(min(map(int,j.split()),key=lambda _:(abs(_),-_)))