
from evolution_memory import EvolutionMemory
from performance_tracker import PerformanceTracker
from rule_optimizer import RuleOptimizer
from strategy_mutator import StrategyMutator



class EvolutionEngine:


    def __init__(self):

        self.memory=EvolutionMemory()

        self.performance=PerformanceTracker()

        self.optimizer=RuleOptimizer()

        self.mutator=StrategyMutator()



    def evolve(self,prediction,result):


        error=round(
            abs(prediction-result),
            4
        )


        self.performance.add(
            1-error
        )


        self.memory.store(
            {
                "prediction":prediction,
                "result":result,
                "error":error
            }
        )


        rule=self.optimizer.optimize(error)


        strategy=self.mutator.mutate(
            "default"
        )


        return {

            "error":error,

            "rule":rule,

            "strategy":strategy,

            "score":
            self.performance.average()
        }
