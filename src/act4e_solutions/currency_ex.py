import act4e_interfaces as I


class SolCurrencyOptimization(I.CurrencyOptimization):
    def compute_optimal_conversion(
        self,
        available: I.SemiCategory[I.RichObject[str], I.RichMorphism[I.CurrencyExchanger]],
        source: str,
        amount: float,
        target: str,
    ) -> I.OptimalSolution:
        pass
