# procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth and returns the time taken to download the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) whereas file size is given in
# megabytes (MB).

def units(unit):
    if (unit=='kb' or unit=='KB' or unit=='kB'):
        if unit=='kb':
            f_unit=2.0**10.0
        else:
            f_unit=2.0**10.0*8.0
    elif (unit=='Mb' or unit=='MB'):
             if unit=='Mb': 
                f_unit=2.0**20.0
             else:
                f_unit=2.0**20.0*8.0
    elif (unit=='Gb' or unit=='GB'):
            if unit=='Gb': 
                f_unit=2.0**30.0
            else:
                f_unit=2.0**30.0*8.0
    elif (unit=='Tb' or unit=='TB'):
            if unit=='Tb': 
                f_unit=2.0**40.0
            else:
                f_unit=2.0**40.0*8.0
    return f_unit


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
                
                temp='%f'% seconds    
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
     
    

def download_time(size,file_unit,bandwidth,bandwidth_unit):
    f_unit=units(file_unit)
    b_unit=units(bandwidth_unit)
    size=f_unit*size #in bits
    bandwidth=bandwidth*b_unit
    seconds=size/bandwidth
    time=convert_seconds(seconds)
    return time
    
    
    



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(5.56,'GB',1,'MB')
# "1 hour, 34 minutes, 53.44 seconds"



