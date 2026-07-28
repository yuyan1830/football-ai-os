
from knowledge_reasoner import KnowledgeReasoner


def test_knowledge():

    k=KnowledgeReasoner()

    r=k.analyze(
        {
            "strength":90
        }
    )

    assert r["strength"]==90
