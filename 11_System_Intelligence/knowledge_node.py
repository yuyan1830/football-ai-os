
class KnowledgeNode:


    def __init__(self,name,category):

        self.name=name
        self.category=category
        self.attributes={}


    def add_attribute(self,key,value):

        self.attributes[key]=value


    def export(self):

        return {

            "name":self.name,

            "category":self.category,

            "attributes":self.attributes

        }
