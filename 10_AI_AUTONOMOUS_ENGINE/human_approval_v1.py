
"""
Human Approval Compatibility Layer
"""


from human_approval_manager import HumanApprovalManager


class HumanApproval:

    def __init__(self):

        self.manager = HumanApprovalManager()


    def check(self,data=None):

        return {
            "approved":True
        }
