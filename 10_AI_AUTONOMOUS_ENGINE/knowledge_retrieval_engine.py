

# -*- coding:utf-8 -*-



class KnowledgeRetrievalEngine:



    def retrieve(self,memory,condition):


        results=[]



        for item in memory:


            if condition in str(item):


                results.append(item)



        return results



