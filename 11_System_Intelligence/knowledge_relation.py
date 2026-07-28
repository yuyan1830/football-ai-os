
class KnowledgeRelation:


    def __init__(self):

        self.links=[]


    def add(self,a,b,relation):

        self.links.append(

            {

            "from":a,

            "to":b,

            "relation":relation

            }

        )


    def get(self):

        return self.links
