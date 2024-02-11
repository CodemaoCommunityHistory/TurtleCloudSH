import subprocess
import time
print('Welcome To TurtleCloudSH!\n'
      'Because to Codemao official server restrictions, you may not be able to do some of the things you want to do. Please switch to "Python cloud mode" before use\n'
      'For more information, please go to: https://github.com/CodemaoCommunityHistory/\n'
      'To exit please enter ".exit"\n'
     'Type Command... \n')
    
def execute_bash_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()
  
while(1):
    bash_command = input('')
    if bash_command == '.exit' :
        print('Exit')
        exit()     
    start_time = time.time()
    print('[Please wait, the command is being executed]')
    output, error = execute_bash_command(bash_command)
    end_time = time.time()
    run_time = end_time - start_time
    print(f'=====Running time:{run_time}s=====')
    if len(error) != 0 :
        print('Error:' , error)
    else:
        print(output)
    print('==========')
