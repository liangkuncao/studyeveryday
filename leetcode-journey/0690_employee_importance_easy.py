"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {e.id: e for e in employees}

        def helper(employees: Set['Employee'], id) -> int:
            employee = employees[id]
            importance = employee.importance
            for e_id in employee.subordinates:
                importance += helper(employees, e_id)
            return importance

        return helper(employees, id)
