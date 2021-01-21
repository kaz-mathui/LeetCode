# class Solution:
#     def interpret(self, command: str) -> str:
#         command = command.replace('()','o').replace('(al)','al')
#         return command


class Solution:
    def interpret(self, command: str) -> str:
        final_str = ''
        for i in range(0,len(command)):
            if command[i] == 'G':
                final_str+='G'
            elif command[i] == '(' and command[i+1] == ')':
                final_str+='o'
                i+=1
            elif command[i] == '(' and command[i+3] == ')':
                final_str+='al'
                i+=3
        return final_str