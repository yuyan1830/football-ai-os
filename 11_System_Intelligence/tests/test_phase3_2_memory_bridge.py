
from knowledge_memory_bridge import KnowledgeMemoryBridge
from memory_adapter import MemoryAdapter
from feedback_memory import FeedbackMemory


def test_memory_bridge():

    bridge = KnowledgeMemoryBridge()

    result = bridge.store_memory(
        {
            "match":"test",
            "win":True
        }
    )

    assert result["status"]=="stored"


def test_memory_adapter():

    adapter=MemoryAdapter()

    r=adapter.adapt(
        "home_win",
        "correct"
    )

    assert r["updated"]==True


def test_feedback_memory():

    memory=FeedbackMemory()

    memory.add(
        {
            "error":0.1
        }
    )

    assert memory.count()==1
