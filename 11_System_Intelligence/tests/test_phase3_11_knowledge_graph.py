
from knowledge_node import KnowledgeNode
from knowledge_relation import KnowledgeRelation
from knowledge_embedding import KnowledgeEmbedding
from knowledge_query_engine import KnowledgeQueryEngine


def test_knowledge_graph():


    node=KnowledgeNode(
        "Manchester City",
        "team"
    )


    node.add_attribute(
        "attack",
        95
    )


    assert node.export()["attributes"]["attack"]==95



def test_relation():


    r=KnowledgeRelation()


    r.add(
        "team",
        "player",
        "has"
    )


    assert len(r.get())==1



def test_embedding():


    e=KnowledgeEmbedding()


    x=e.encode(
        "football"
    )


    assert x["vector"][0]==8



def test_query():


    q=KnowledgeQueryEngine()


    x=q.query(
        "team"
    )


    assert x["result"]=="knowledge found"

