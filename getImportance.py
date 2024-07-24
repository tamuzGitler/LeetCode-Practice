"""
# Definition for Employee.
"""


class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        importanceSum = 0
        employeesMap = dict()
        for i, employee in enumerate(employees):
            employeesMap[employee.id] = i
        return self.dfs(employees, id, employeesMap)

    def dfs(self, employees, id, employeesMap):

        importanceSum = employees[employeesMap[id]].importance
        for subordianteId in employees[employeesMap[id]].subordinates:
            importanceSum += self.dfs(employees, subordianteId)
        return importanceSum
