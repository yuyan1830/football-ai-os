

# -*- coding:utf-8 -*-



class KnowledgeGraphBuilder:



    def __init__(self):


        self.nodes=[]




    def add_node(

        self,

        node_type,

        value

    ):


        node={


            "type":

            node_type,


            "value":

            value



        }


        self.nodes.append(node)


        return node




    def graph(self):


        return {


            "nodes":

            self.nodes



        }



