class Tool:
    def execute(self, input_data: str) -> str:
        raise NotImplementedError
    
class CalculatorTool(Tool):
    def __init__(self, precision: int = 2):
        self.precision = precision

    def execute(self, input_data: str) -> str:
        result = eval(input_data)
        return str(round(result, self.precision))
    
    def run_tool(tool: Tool, input_data: str):
        return tool.execute(input_data)
    
tool = Tool()
calc = CalculatorTool(precision=3)
tool.execute("2+2")


# class Employee:
#     raise_amt=1.5
#     cnt=0
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+'.'+last+'@gmail.com'

#         Employee.cnt+=2

#     def fullName(self):
#         return '{} {}'.format(self.first,self.last)
    
#     def apply_raise(self):
#         return (self.pay*self.raise_amt)

# print(Employee.cnt)

# emp_1=Employee('Parth','Agrawal',129000000)
# emp_2=Employee('Harsh','Nigam',129000000)


# print(Employee.cnt)
# # print(emp_1.apply_raise())
# # emp_1.raise_amt=2
# # print(Employee.raise_amt)
# # print(emp_1.raise_amt)
# # print(emp_2.raise_amt)
# # print(emp_1.__dict__)

# # print(emp_1)
# # print(emp_2)

# # emp_1.first="Parth"
# # emp_1.last="Agrawal"
# # emp_1.email="parthagrawal4675@gmail.com"
# # emp_1.pay=12900000

# # emp_2.first="Harsh"
# # emp_2.last="Nigam"
# # emp_2.email="harshnigam4675@gmail.com"
# # emp_2.pay=12900000

# # print(emp_1.email)
# # print(emp_2.email)

# # print(emp_2.fullName())

# # emp_1.fullName()
# # print(Employee.fullName(emp_1))

