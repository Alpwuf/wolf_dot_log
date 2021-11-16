# wolf_dot_log
A simple package that allows you to save inputs & outputs as .log files

## |Instructions|
### [Importing The Module]  
import wolf_dot_log as log 
  
### [Configuration]
log.backup = True  ***[Set True if a duplicated backup is needed, the default is False]***  
  
log.backup_path = "/Users/Alpwuf/Desktop/"  ***[Set path to save backup file]***  
  
log.path = "/Users/Alpwuf/Desktop/"  ***[Set path to save main log file]***  
  
**Basic logging**  
  
log.log("Text")  
log.log_io("Input", "Output")  
  
**One file/day**  
  
log.daily_log("Text")  
log.daily_log_io("Input", "Output")  
  
**One file/month**
  
log.monthly_log("Text")  
log.monthly_log_io("Input", "Output")  
