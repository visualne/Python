import ansible.runner

class ansibleWrap():

    '''The below function runs a command and returns the results from stdout'''
    def runCommand(self,cmd):
    #Creating runner object that will be used to speak to and hold commands from the host we are talking to.
        runner = ansible.runner.Runner(
        module_name='shell',
        module_args=cmd,
        pattern='all'
    )
        datastructure = runner.run()

        return datastructure