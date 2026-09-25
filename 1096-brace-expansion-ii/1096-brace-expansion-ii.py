class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parseExpr(i):
            # returns (set of strings, next index)
            result = {""}
            while i < len(expression) and expression[i] not in ',}':
                factor_set, i = parseFactor(i)
                new_result = set()
                for a in result:
                    for b in factor_set:
                        new_result.add(a + b)
                result = new_result
            return result, i
        
        def parseFactor(i):
            if expression[i] == '{':
                return parseBrace(i)
            else:
                return {expression[i]}, i + 1
        
        def parseBrace(i):
            # expression[i] == '{'
            i += 1
            result = set()
            while True:
                expr_set, i = parseExpr(i)
                result |= expr_set
                if expression[i] == ',':
                    i += 1
                else:  # '}'
                    i += 1
                    break
            return result, i
        
        result_set, _ = parseExpr(0)
        return sorted(result_set)