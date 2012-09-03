# procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3


def convert_seconds(seconds):
    input_seconds=seconds
    hrs=0
    mins=0
    f_seconds=int(seconds)
    
    
    if f_seconds>=3600:
        hrs=f_seconds/3600
        seconds=seconds%3600
        f_seconds=f_seconds%3600
        if hrs>1:
            str_hr=str(hrs)+' hours, '
        else:
            str_hr=str(hrs)+' hour, '
        if seconds==0.0 or f_seconds==0:
            return (str_hr+'0 minutes, 0 seconds')
    if f_seconds>=60 and f_seconds<3600:
            if input_seconds<3600:
                str_hr='0 hours, '
            mins=f_seconds/60
            seconds=seconds%60.0
            f_seconds=f_seconds%60
            if mins>1:
                    str_min=str(mins)+' minutes, '
            else:
                    str_min=str(mins)+' minute, '
           
            
            if seconds==0.0 or f_seconds==0:
                time=str_hr+str_min+'0 seconds'
                return time
            if seconds>f_seconds:
                
                temp='%.1f'% seconds    
                if seconds>1 or seconds==0.0:
                    str_sec=temp+' seconds'
                else:
                    str_sec=temp+' second'    
                
                time=str_hr+str_min+str_sec
                return time
            else:
                
                if f_seconds>1 or f_seconds==0:
                    str_sec=str(f_seconds)+' seconds'
                else:
                    str_sec=str(f_seconds)+' second'
           
              
                time=str_hr+str_min+str_sec
                return time
                
    if seconds<60:
                if seconds==1:
                    time='0 hours, 0 minutes, '+str(seconds)+' second'
                else:
                    time='0 hours, 0 minutes, '+str(seconds)+' seconds'
                  
                return time
     
              
               
                
        
    
    


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
