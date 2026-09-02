class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        total = 0

        for i in range(len(details)):

            detail = details[i]
            age = int(detail[11:13])

            if age > 60:
                total += 1
        
        return total